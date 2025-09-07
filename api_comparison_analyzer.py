#!/usr/bin/env python3
"""
API Comparison Analyzer
Compares legacy.json and saas.json files in each folder to identify:
1. New fields added in SaaS
2. Fields missing from legacy 
3. Renamed fields
4. Type changes
"""

import json
import os
import sys
from typing import Dict, Any, List, Set, Tuple
from collections import defaultdict

def get_field_info(data: Any, path: str = "") -> Dict[str, str]:
    """Recursively extract field names and their types from JSON data."""
    fields = {}
    
    if isinstance(data, dict):
        for key, value in data.items():
            current_path = f"{path}.{key}" if path else key
            fields[current_path] = type(value).__name__
            
            # Recursively process nested objects
            if isinstance(value, (dict, list)):
                nested_fields = get_field_info(value, current_path)
                fields.update(nested_fields)
                
    elif isinstance(data, list) and data:
        # Process first item in array to get structure
        if data:
            nested_fields = get_field_info(data[0], f"{path}[0]")
            fields.update(nested_fields)
            
    return fields

def extract_data_from_legacy(legacy_data: Any) -> Any:
    """Extract the actual data from legacy format, ignoring wrapper."""
    if isinstance(legacy_data, dict):
        # Skip the wrapper fields as requested
        if "message" in legacy_data:
            return legacy_data["message"]
        elif "data" in legacy_data:
            return legacy_data["data"]
        else:
            # If no wrapper, return as-is but filter out code/status
            filtered = {k: v for k, v in legacy_data.items() 
                       if k not in ["code", "status"]}
            return filtered
    return legacy_data

def analyze_api_folder(folder_path: str) -> Dict[str, Any]:
    """Analyze a single API folder comparing legacy.json and saas.json."""
    legacy_path = os.path.join(folder_path, "legacy.json")
    saas_path = os.path.join(folder_path, "saas.json")
    
    if not os.path.exists(legacy_path) or not os.path.exists(saas_path):
        return {"error": f"Missing files in {folder_path}"}
    
    try:
        with open(legacy_path, 'r') as f:
            legacy_raw = json.load(f)
        with open(saas_path, 'r') as f:
            saas_data = json.load(f)
            
        # Extract actual data from legacy (removing wrapper)
        legacy_data = extract_data_from_legacy(legacy_raw)
        
        # Get field information
        legacy_fields = get_field_info(legacy_data)
        saas_fields = get_field_info(saas_data)
        
        # Compare fields
        legacy_field_names = set(legacy_fields.keys())
        saas_field_names = set(saas_fields.keys())
        
        # Find differences
        new_in_saas = saas_field_names - legacy_field_names
        missing_from_saas = legacy_field_names - saas_field_names
        common_fields = legacy_field_names & saas_field_names
        
        # Check for type changes in common fields
        type_changes = {}
        for field in common_fields:
            if legacy_fields[field] != saas_fields[field]:
                type_changes[field] = {
                    "legacy_type": legacy_fields[field],
                    "saas_type": saas_fields[field]
                }
        
        # Detect potential renames (fields with similar names)
        potential_renames = []
        for missing_field in missing_from_saas:
            for new_field in new_in_saas:
                # Simple heuristic: similar field names
                missing_base = missing_field.split('.')[-1].lower()
                new_base = new_field.split('.')[-1].lower()
                
                # Check for various rename patterns
                if (missing_base in new_base or new_base in missing_base or
                    missing_base.replace('_', '') == new_base.replace('_', '') or
                    missing_base.replace('_', '').replace('-', '') == new_base.replace('_', '').replace('-', '')):
                    potential_renames.append({
                        "legacy_field": missing_field,
                        "saas_field": new_field,
                        "legacy_type": legacy_fields[missing_field],
                        "saas_type": saas_fields[new_field]
                    })
        
        return {
            "legacy_fields_count": len(legacy_fields),
            "saas_fields_count": len(saas_fields),
            "legacy_fields": legacy_fields,
            "saas_fields": saas_fields,
            "new_in_saas": sorted(list(new_in_saas)),
            "missing_from_saas": sorted(list(missing_from_saas)),
            "common_fields": sorted(list(common_fields)),
            "type_changes": type_changes,
            "potential_renames": potential_renames,
            "legacy_sample": legacy_data[:2] if isinstance(legacy_data, list) else legacy_data,
            "saas_sample": saas_data[:2] if isinstance(saas_data, list) else saas_data
        }
        
    except Exception as e:
        return {"error": f"Error processing {folder_path}: {str(e)}"}

def generate_markdown_table(analysis: Dict[str, Any]) -> str:
    """Generate a markdown table for a single API analysis."""
    if "error" in analysis:
        return f"**Error:** {analysis['error']}\n\n"
    
    md = []
    
    # Summary table
    md.append("### Summary")
    md.append("| Metric | Value |")
    md.append("|--------|-------|")
    md.append(f"| Legacy Fields Count | {analysis['legacy_fields_count']} |")
    md.append(f"| SaaS Fields Count | {analysis['saas_fields_count']} |")
    md.append(f"| New Fields in SaaS | {len(analysis['new_in_saas'])} |")
    md.append(f"| Missing from SaaS | {len(analysis['missing_from_saas'])} |")
    md.append(f"| Common Fields | {len(analysis['common_fields'])} |")
    md.append(f"| Type Changes | {len(analysis['type_changes'])} |")
    md.append(f"| Potential Renames | {len(analysis['potential_renames'])} |")
    md.append("")
    
    # New fields in SaaS
    if analysis['new_in_saas']:
        md.append("### New Fields Added in SaaS")
        md.append("| Field Name | Type |")
        md.append("|------------|------|")
        for field in analysis['new_in_saas']:
            field_type = analysis['saas_fields'][field]
            md.append(f"| `{field}` | {field_type} |")
        md.append("")
    
    # Missing from SaaS (present in legacy)
    if analysis['missing_from_saas']:
        md.append("### Fields Missing from SaaS (Present in Legacy)")
        md.append("| Field Name | Type |")
        md.append("|------------|------|")
        for field in analysis['missing_from_saas']:
            field_type = analysis['legacy_fields'][field]
            md.append(f"| `{field}` | {field_type} |")
        md.append("")
    
    # Type changes
    if analysis['type_changes']:
        md.append("### Fields with Type Changes")
        md.append("| Field Name | Legacy Type | SaaS Type |")
        md.append("|------------|-------------|-----------|")
        for field, types in analysis['type_changes'].items():
            md.append(f"| `{field}` | {types['legacy_type']} | {types['saas_type']} |")
        md.append("")
    
    # Potential renames
    if analysis['potential_renames']:
        md.append("### Potential Field Renames")
        md.append("| Legacy Field | SaaS Field | Legacy Type | SaaS Type |")
        md.append("|--------------|------------|-------------|-----------|")
        for rename in analysis['potential_renames']:
            md.append(f"| `{rename['legacy_field']}` | `{rename['saas_field']}` | {rename['legacy_type']} | {rename['saas_type']} |")
        md.append("")
    
    return "\n".join(md)

def main():
    comparison_dir = "/home/runner/work/personal/personal/comparision"
    
    if not os.path.exists(comparison_dir):
        print(f"Error: {comparison_dir} not found")
        sys.exit(1)
    
    # Get all API folders
    api_folders = []
    for item in os.listdir(comparison_dir):
        folder_path = os.path.join(comparison_dir, item)
        if os.path.isdir(folder_path):
            api_folders.append(item)
    
    api_folders.sort()
    
    # Generate main summary markdown
    summary_md = []
    summary_md.append("# API Legacy vs SaaS Comparison Analysis")
    summary_md.append("")
    summary_md.append("This document provides a detailed comparison between Legacy and SaaS API responses for each endpoint.")
    summary_md.append("")
    summary_md.append("## Table of Contents")
    
    for folder in api_folders:
        summary_md.append(f"- [{folder}](#{folder.replace('-', '-').replace('{{', '').replace('}}', '')})")
    
    summary_md.append("")
    
    # Analyze each API
    all_analyses = {}
    for folder in api_folders:
        print(f"Analyzing {folder}...")
        folder_path = os.path.join(comparison_dir, folder)
        analysis = analyze_api_folder(folder_path)
        all_analyses[folder] = analysis
        
        # Add to markdown
        summary_md.append(f"## {folder}")
        summary_md.append("")
        summary_md.append(generate_markdown_table(analysis))
        summary_md.append("---")
        summary_md.append("")
    
    # Write summary file
    output_file = "/home/runner/work/personal/personal/API_COMPARISON_ANALYSIS.md"
    with open(output_file, 'w') as f:
        f.write("\n".join(summary_md))
    
    print(f"\nAnalysis complete! Results saved to: {output_file}")
    
    # Print quick summary
    print("\n=== QUICK SUMMARY ===")
    total_new = 0
    total_missing = 0
    total_renames = 0
    total_type_changes = 0
    
    for folder, analysis in all_analyses.items():
        if "error" not in analysis:
            new_count = len(analysis['new_in_saas'])
            missing_count = len(analysis['missing_from_saas'])
            rename_count = len(analysis['potential_renames'])
            type_change_count = len(analysis['type_changes'])
            
            total_new += new_count
            total_missing += missing_count
            total_renames += rename_count
            total_type_changes += type_change_count
            
            print(f"{folder}: +{new_count} new, -{missing_count} missing, ~{rename_count} renames, !{type_change_count} type changes")
    
    print(f"\nTOTALS: +{total_new} new, -{total_missing} missing, ~{total_renames} renames, !{total_type_changes} type changes")

if __name__ == "__main__":
    main()