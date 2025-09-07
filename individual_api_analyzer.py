#!/usr/bin/env python3
"""
Individual API Analysis Generator
Creates separate markdown files for each API endpoint comparison
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

def generate_individual_api_markdown(api_name: str, analysis: Dict[str, Any]) -> str:
    """Generate a detailed markdown report for a single API."""
    if "error" in analysis:
        return f"# {api_name} API Analysis\n\n**Error:** {analysis['error']}\n"
    
    md = []
    
    # Header
    md.append(f"# {api_name} API Analysis")
    md.append(f"**Legacy vs SaaS Comparison**")
    md.append("")
    
    # Executive Summary
    md.append("## Executive Summary")
    md.append("")
    
    # Key changes summary
    new_count = len(analysis['new_in_saas'])
    missing_count = len(analysis['missing_from_saas'])
    rename_count = len(analysis['potential_renames'])
    type_change_count = len(analysis['type_changes'])
    
    if new_count > 0:
        md.append(f"- **{new_count} new fields** added in SaaS")
    if missing_count > 0:
        md.append(f"- **{missing_count} fields** removed from Legacy (missing in SaaS)")
    if rename_count > 0:
        md.append(f"- **{rename_count} potential field renames** detected")
    if type_change_count > 0:
        md.append(f"- **{type_change_count} fields** have type changes")
    
    if new_count == 0 and missing_count == 0 and rename_count == 0 and type_change_count == 0:
        md.append("- **No significant changes** detected between Legacy and SaaS")
    
    md.append("")
    
    # Summary table
    md.append("## Overview")
    md.append("| Metric | Legacy | SaaS | Change |")
    md.append("|--------|--------|------|--------|")
    md.append(f"| Total Fields | {analysis['legacy_fields_count']} | {analysis['saas_fields_count']} | {analysis['saas_fields_count'] - analysis['legacy_fields_count']:+d} |")
    md.append(f"| New Fields | - | {new_count} | +{new_count} |")
    md.append(f"| Removed Fields | {missing_count} | - | -{missing_count} |")
    md.append(f"| Common Fields | {len(analysis['common_fields'])} | {len(analysis['common_fields'])} | 0 |")
    md.append(f"| Type Changes | - | {type_change_count} | {type_change_count} |")
    md.append("")
    
    # Detailed sections
    if analysis['new_in_saas']:
        md.append("## 🆕 New Fields Added in SaaS")
        md.append("These fields are present in SaaS but not in Legacy:")
        md.append("")
        md.append("| Field Name | Type | Notes |")
        md.append("|------------|------|-------|")
        for field in analysis['new_in_saas']:
            field_type = analysis['saas_fields'][field]
            md.append(f"| `{field}` | {field_type} | New functionality |")
        md.append("")
    
    if analysis['missing_from_saas']:
        md.append("## ❌ Fields Removed from Legacy")
        md.append("These fields were present in Legacy but are missing in SaaS:")
        md.append("")
        md.append("| Field Name | Type | Impact |")
        md.append("|------------|------|--------|")
        for field in analysis['missing_from_saas']:
            field_type = analysis['legacy_fields'][field]
            md.append(f"| `{field}` | {field_type} | Functionality removed/changed |")
        md.append("")
    
    if analysis['type_changes']:
        md.append("## 🔄 Fields with Type Changes")
        md.append("These fields exist in both but have different data types:")
        md.append("")
        md.append("| Field Name | Legacy Type | SaaS Type | Impact |")
        md.append("|------------|-------------|-----------|--------|")
        for field, types in analysis['type_changes'].items():
            impact = "⚠️ Breaking change" if types['legacy_type'] != types['saas_type'] else "Minor change"
            md.append(f"| `{field}` | {types['legacy_type']} | {types['saas_type']} | {impact} |")
        md.append("")
    
    if analysis['potential_renames']:
        md.append("## 🏷️ Potential Field Renames")
        md.append("These appear to be renamed fields (similar names/types):")
        md.append("")
        md.append("| Legacy Field | SaaS Field | Legacy Type | SaaS Type | Confidence |")
        md.append("|--------------|------------|-------------|-----------|------------|")
        for rename in analysis['potential_renames']:
            confidence = "High" if rename['legacy_type'] == rename['saas_type'] else "Medium"
            md.append(f"| `{rename['legacy_field']}` | `{rename['saas_field']}` | {rename['legacy_type']} | {rename['saas_type']} | {confidence} |")
        md.append("")
    
    # Sample data comparison
    md.append("## Sample Data Structure")
    md.append("")
    md.append("### Legacy Sample")
    md.append("```json")
    md.append(json.dumps(analysis['legacy_sample'], indent=2)[:1000] + ("..." if len(json.dumps(analysis['legacy_sample'], indent=2)) > 1000 else ""))
    md.append("```")
    md.append("")
    md.append("### SaaS Sample")
    md.append("```json")
    md.append(json.dumps(analysis['saas_sample'], indent=2)[:1000] + ("..." if len(json.dumps(analysis['saas_sample'], indent=2)) > 1000 else ""))
    md.append("```")
    md.append("")
    
    # Recommendations
    md.append("## Recommendations")
    md.append("")
    if new_count > 0:
        md.append(f"1. **Review new fields**: {new_count} new fields have been added. Ensure consuming applications can handle these additions.")
    if missing_count > 0:
        md.append(f"2. **Handle removed fields**: {missing_count} fields are no longer available. Update consuming applications accordingly.")
    if type_change_count > 0:
        md.append(f"3. **Address type changes**: {type_change_count} fields have changed types. This may require data parsing updates.")
    if rename_count > 0:
        md.append(f"4. **Verify renames**: {rename_count} potential field renames detected. Confirm these are intentional changes.")
    
    if new_count == 0 and missing_count == 0 and rename_count == 0 and type_change_count == 0:
        md.append("1. **No action required**: The API structure is identical between Legacy and SaaS.")
    
    md.append("")
    
    return "\n".join(md)

def main():
    comparison_dir = "/home/runner/work/personal/personal/comparision"
    output_dir = "/home/runner/work/personal/personal/api_analysis"
    
    if not os.path.exists(comparison_dir):
        print(f"Error: {comparison_dir} not found")
        sys.exit(1)
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all API folders
    api_folders = []
    for item in os.listdir(comparison_dir):
        folder_path = os.path.join(comparison_dir, item)
        if os.path.isdir(folder_path):
            api_folders.append(item)
    
    api_folders.sort()
    
    # Generate individual analysis for each API
    summary_data = []
    
    for folder in api_folders:
        print(f"Analyzing {folder}...")
        folder_path = os.path.join(comparison_dir, folder)
        analysis = analyze_api_folder(folder_path)
        
        # Generate individual markdown
        api_markdown = generate_individual_api_markdown(folder, analysis)
        
        # Write individual file
        safe_filename = folder.replace("{{", "").replace("}}", "").replace(" ", "_")
        output_file = os.path.join(output_dir, f"{safe_filename}_analysis.md")
        with open(output_file, 'w') as f:
            f.write(api_markdown)
        
        # Collect summary data
        if "error" not in analysis:
            summary_data.append({
                "api": folder,
                "file": f"{safe_filename}_analysis.md",
                "new": len(analysis['new_in_saas']),
                "missing": len(analysis['missing_from_saas']),
                "renames": len(analysis['potential_renames']),
                "type_changes": len(analysis['type_changes']),
                "total_legacy": analysis['legacy_fields_count'],
                "total_saas": analysis['saas_fields_count']
            })
    
    # Generate master index
    index_md = []
    index_md.append("# API Comparison Analysis Index")
    index_md.append("")
    index_md.append("This directory contains detailed analysis for each API endpoint comparing Legacy and SaaS implementations.")
    index_md.append("")
    index_md.append("## Summary Overview")
    index_md.append("")
    index_md.append("| API Endpoint | New Fields | Removed Fields | Renames | Type Changes | Analysis File |")
    index_md.append("|--------------|------------|----------------|---------|--------------|---------------|")
    
    total_new = total_missing = total_renames = total_type_changes = 0
    
    for data in summary_data:
        emoji = "✅" if data['new'] == 0 and data['missing'] == 0 and data['renames'] == 0 and data['type_changes'] == 0 else "⚠️"
        index_md.append(f"| {emoji} {data['api']} | {data['new']} | {data['missing']} | {data['renames']} | {data['type_changes']} | [{data['file']}](./{data['file']}) |")
        
        total_new += data['new']
        total_missing += data['missing'] 
        total_renames += data['renames']
        total_type_changes += data['type_changes']
    
    index_md.append(f"| **TOTALS** | **{total_new}** | **{total_missing}** | **{total_renames}** | **{total_type_changes}** | - |")
    index_md.append("")
    
    # Key findings
    index_md.append("## Key Findings")
    index_md.append("")
    index_md.append(f"- **{total_new}** total new fields added across all APIs")
    index_md.append(f"- **{total_missing}** total fields removed from Legacy")
    index_md.append(f"- **{total_renames}** potential field renames detected")
    index_md.append(f"- **{total_type_changes}** fields with type changes")
    index_md.append("")
    
    # APIs with most changes
    high_change_apis = [d for d in summary_data if (d['new'] + d['missing'] + d['type_changes']) > 10]
    if high_change_apis:
        index_md.append("## APIs with Significant Changes")
        index_md.append("")
        for api_data in sorted(high_change_apis, key=lambda x: x['new'] + x['missing'] + x['type_changes'], reverse=True):
            total_changes = api_data['new'] + api_data['missing'] + api_data['type_changes']
            index_md.append(f"- **{api_data['api']}**: {total_changes} total changes")
        index_md.append("")
    
    # Write index file
    index_file = os.path.join(output_dir, "README.md")
    with open(index_file, 'w') as f:
        f.write("\n".join(index_md))
    
    print(f"\nAnalysis complete!")
    print(f"📁 Output directory: {output_dir}")
    print(f"📄 Individual analysis files: {len(summary_data)}")
    print(f"📋 Master index: {index_file}")
    print(f"\n🔍 Summary: +{total_new} new, -{total_missing} missing, ~{total_renames} renames, !{total_type_changes} type changes")

if __name__ == "__main__":
    main()