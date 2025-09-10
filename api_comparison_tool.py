#!/usr/bin/env python3
"""
API Comparison Tool - Senior Analyst Level

This tool compares SAAS and Legacy API responses to generate a comprehensive
comparison report in CSV format with multiple sheets.

Created for analyzing API responses in the comparision directory.
"""

import json
import os
import pandas as pd
from typing import Dict, List, Any, Tuple, Set
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class APIComparisonAnalyzer:
    def __init__(self, comparison_dir: str):
        self.comparison_dir = Path(comparison_dir)
        self.comparison_data = {}
        
    def get_type_description(self, value: Any) -> str:
        """Get detailed type description for a value"""
        if value is None:
            return "null"
        elif isinstance(value, bool):
            return "boolean"
        elif isinstance(value, int):
            return "integer"
        elif isinstance(value, float):
            return "float"
        elif isinstance(value, str):
            if not value:
                return "string (empty)"
            return "string"
        elif isinstance(value, list):
            if not value:
                return "array (empty)"
            # Get types of first few elements to understand array content
            sample_types = set()
            for i, item in enumerate(value[:3]):  # Sample first 3 elements
                sample_types.add(self.get_type_description(item))
            if len(sample_types) == 1:
                return f"array of {list(sample_types)[0]}"
            else:
                return f"array of mixed types: {', '.join(sample_types)}"
        elif isinstance(value, dict):
            if not value:
                return "object (empty)"
            return "object"
        else:
            return f"unknown ({type(value).__name__})"
    
    def extract_field_paths(self, data: Any, path: str = "", max_depth: int = 10) -> Dict[str, Any]:
        """Recursively extract all field paths from JSON data with their values"""
        if max_depth <= 0:
            return {path: "... (max depth reached)"}
        
        paths = {}
        
        if isinstance(data, dict):
            if not data:
                paths[path if path else "root"] = {}
            for key, value in data.items():
                current_path = f"{path}.{key}" if path else key
                paths[current_path] = value
                if isinstance(value, (dict, list)) and value:
                    paths.update(self.extract_field_paths(value, current_path, max_depth - 1))
        
        elif isinstance(data, list):
            if not data:
                paths[path] = []
            else:
                # For arrays, analyze first element structure
                paths[f"{path}[0]"] = data[0] if data else None
                if data and isinstance(data[0], (dict, list)):
                    paths.update(self.extract_field_paths(data[0], f"{path}[0]", max_depth - 1))
                
                # If there are multiple elements with different structures, note it
                if len(data) > 1:
                    first_type = type(data[0])
                    has_different_types = any(type(item) != first_type for item in data[1:3])
                    if has_different_types:
                        paths[f"{path}[*]"] = "Mixed types in array elements"
        
        else:
            paths[path] = data
            
        return paths
    
    def normalize_field_path(self, field_path: str) -> str:
        """Normalize field paths by removing common wrapper prefixes like 'message[0]' -> '[0]'"""
        # Remove common wrapper prefixes to match equivalent inner fields
        if field_path.startswith('message[0].'):
            return field_path.replace('message[0].', '[0].')
        elif field_path == 'message[0]':
            return '[0]'
        elif field_path.startswith('message.'):
            return field_path.replace('message.', '')
        elif field_path == 'message':
            return 'root_array'  # Normalize message array to a common name
        return field_path

    def analyze_api_differences(self, saas_paths: Dict, legacy_paths: Dict, api_name: str) -> List[Dict]:
        """Analyze differences between SAAS and Legacy APIs"""
        # Create normalized path mappings
        saas_normalized = {}
        legacy_normalized = {}
        
        for path, value in saas_paths.items():
            norm_path = self.normalize_field_path(path)
            saas_normalized[norm_path] = (path, value)
            
        for path, value in legacy_paths.items():
            norm_path = self.normalize_field_path(path)
            legacy_normalized[norm_path] = (path, value)
        
        # Get all normalized paths and their corresponding original paths
        all_normalized_paths = set(saas_normalized.keys()) | set(legacy_normalized.keys())
        comparison_results = []
        
        # Skip wrapper fields that should be ignored as per the issue description
        ignored_fields = {'code', 'status', 'message', 'root_array'}
        
        for norm_path in sorted(all_normalized_paths):
            # Skip ignored wrapper fields
            if norm_path in ignored_fields:
                continue
                
            saas_present = norm_path in saas_normalized
            legacy_present = norm_path in legacy_normalized
            
            # Get original paths and values
            saas_original_path = saas_normalized[norm_path][0] if saas_present else norm_path
            legacy_original_path = legacy_normalized[norm_path][0] if legacy_present else norm_path
            
            saas_value = saas_normalized[norm_path][1] if saas_present else None
            legacy_value = legacy_normalized[norm_path][1] if legacy_present else None
            
            # Use the more descriptive original path for display
            display_path = legacy_original_path if legacy_present else saas_original_path
            
            saas_type = self.get_type_description(saas_value) if saas_present else ""
            legacy_type = self.get_type_description(legacy_value) if legacy_present else ""
            
            # Generate analytical notes
            notes = []
            
            if saas_present and not legacy_present:
                notes.append("Field only exists in SAAS - new feature or additional data")
            elif not saas_present and legacy_present:
                notes.append("Field only exists in Legacy - potentially deprecated or moved")
            elif saas_present and legacy_present:
                if saas_type != legacy_type:
                    notes.append(f"Type mismatch: SAAS has {saas_type}, Legacy has {legacy_type}")
                
                # Value-based analysis for specific types
                if isinstance(saas_value, str) and isinstance(legacy_value, str):
                    if saas_value != legacy_value:
                        notes.append("String values differ between systems")
                elif isinstance(saas_value, (int, float)) and isinstance(legacy_value, (int, float)):
                    if saas_value != legacy_value:
                        notes.append("Numeric values differ between systems")
                elif saas_type == legacy_type and saas_type in ["object", "array"]:
                    notes.append("Complex structure - requires deeper analysis")
                
                # Format differences
                if display_path.endswith("Date") or "date" in display_path.lower():
                    if saas_value and legacy_value and str(saas_value) != str(legacy_value):
                        notes.append("Date format may differ between systems")
                
                if display_path.endswith("Url") or display_path.endswith("Link"):
                    if saas_value and legacy_value:
                        notes.append("URL structure comparison needed")
            
            # Additional structural analysis
            if norm_path.endswith("[0]") and saas_present and legacy_present:
                notes.append("Array structure - verify all elements have consistent schema")
            
            if not notes:
                if saas_present and legacy_present:
                    notes.append("Field exists in both systems with same type")
                else:
                    notes.append("Standard field comparison")
            
            comparison_results.append({
                'Field Path': display_path,
                'Present in SAAS': 'Yes' if saas_present else 'No',
                'Present in Legacy': 'Yes' if legacy_present else 'No',
                'Type in SAAS': saas_type,
                'Type in Legacy': legacy_type,
                'Notes': '; '.join(notes),
                'Team Comments': ''  # Left empty for team review
            })
        
        return comparison_results
    
    def load_json_file(self, file_path: Path) -> Tuple[Any, str]:
        """Load JSON file and return data with any loading notes"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data, ""
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error in {file_path}: {e}")
            return None, f"JSON parsing error: {str(e)}"
        except FileNotFoundError:
            logger.warning(f"File not found: {file_path}")
            return None, "File not found"
        except Exception as e:
            logger.error(f"Error loading {file_path}: {e}")
            return None, f"Loading error: {str(e)}"
    
    def process_api_folder(self, api_folder: Path) -> List[Dict]:
        """Process a single API folder and return comparison results"""
        api_name = api_folder.name
        logger.info(f"Processing API: {api_name}")
        
        saas_file = api_folder / "saas.json"
        legacy_file = api_folder / "legacy.json"
        
        # Load JSON files
        saas_data, saas_notes = self.load_json_file(saas_file)
        legacy_data, legacy_notes = self.load_json_file(legacy_file)
        
        # Handle loading errors
        if saas_data is None and legacy_data is None:
            return [{
                'Field Path': 'FILE_LOADING_ERROR',
                'Present in SAAS': 'No',
                'Present in Legacy': 'No',
                'Type in SAAS': '',
                'Type in Legacy': '',
                'Notes': f'Both files failed to load. SAAS: {saas_notes}, Legacy: {legacy_notes}',
                'Team Comments': ''
            }]
        
        # Extract field paths
        saas_paths = {}
        legacy_paths = {}
        
        if saas_data is not None:
            saas_paths = self.extract_field_paths(saas_data)
        
        if legacy_data is not None:
            legacy_paths = self.extract_field_paths(legacy_data)
        
        # Add file loading notes if any
        results = self.analyze_api_differences(saas_paths, legacy_paths, api_name)
        
        if saas_notes or legacy_notes:
            file_status = {
                'Field Path': 'FILE_STATUS',
                'Present in SAAS': 'Info' if saas_data is not None else 'Error',
                'Present in Legacy': 'Info' if legacy_data is not None else 'Error',
                'Type in SAAS': '',
                'Type in Legacy': '',
                'Notes': f'File loading status - SAAS: {saas_notes or "OK"}, Legacy: {legacy_notes or "OK"}',
                'Team Comments': ''
            }
            results.insert(0, file_status)
        
        return results
    
    def generate_comparison_report(self, output_file: str = "api_comparison_report.xlsx"):
        """Generate comprehensive comparison report"""
        logger.info("Starting API comparison analysis...")
        
        # Get all API folders
        api_folders = [d for d in self.comparison_dir.iterdir() 
                      if d.is_dir() and not d.name.startswith('.')]
        
        if not api_folders:
            logger.error(f"No API folders found in {self.comparison_dir}")
            return
        
        logger.info(f"Found {len(api_folders)} API folders to analyze")
        
        # Create Excel writer
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            summary_data = []
            
            for api_folder in sorted(api_folders):
                api_name = api_folder.name
                logger.info(f"Analyzing {api_name}...")
                
                # Process the API folder
                comparison_results = self.process_api_folder(api_folder)
                
                # Create DataFrame for this API
                df = pd.DataFrame(comparison_results)
                
                # Create summary statistics
                total_fields = len([r for r in comparison_results if r['Field Path'] != 'FILE_STATUS'])
                saas_only = len([r for r in comparison_results 
                               if r['Present in SAAS'] == 'Yes' and r['Present in Legacy'] == 'No'])
                legacy_only = len([r for r in comparison_results 
                                 if r['Present in SAAS'] == 'No' and r['Present in Legacy'] == 'Yes'])
                common_fields = len([r for r in comparison_results 
                                   if r['Present in SAAS'] == 'Yes' and r['Present in Legacy'] == 'Yes'])
                type_mismatches = len([r for r in comparison_results 
                                     if 'Type mismatch' in r['Notes']])
                
                summary_data.append({
                    'API Name': api_name,
                    'Total Fields': total_fields,
                    'SAAS Only': saas_only,
                    'Legacy Only': legacy_only,
                    'Common Fields': common_fields,
                    'Type Mismatches': type_mismatches,
                    'Analysis Status': 'Complete' if total_fields > 0 else 'Error'
                })
                
                # Clean up sheet name (Excel has limitations)
                sheet_name = api_name[:31] if len(api_name) > 31 else api_name
                sheet_name = sheet_name.replace('/', '_').replace('\\', '_').replace('*', '_')
                sheet_name = sheet_name.replace('[', '(').replace(']', ')')
                
                # Write to Excel sheet
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                
                # Auto-adjust column widths
                worksheet = writer.sheets[sheet_name]
                for column in worksheet.columns:
                    max_length = 0
                    column_letter = column[0].column_letter
                    for cell in column:
                        try:
                            if len(str(cell.value)) > max_length:
                                max_length = len(str(cell.value))
                        except:
                            pass
                    adjusted_width = min(max_length + 2, 50)  # Cap at 50 characters
                    worksheet.column_dimensions[column_letter].width = adjusted_width
            
            # Create summary sheet
            summary_df = pd.DataFrame(summary_data)
            summary_df.to_excel(writer, sheet_name='Summary', index=False)
            
            # Auto-adjust summary sheet columns
            summary_worksheet = writer.sheets['Summary']
            for column in summary_worksheet.columns:
                max_length = 0
                column_letter = column[0].column_letter
                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(str(cell.value))
                    except:
                        pass
                adjusted_width = max_length + 2
                summary_worksheet.column_dimensions[column_letter].width = adjusted_width
        
        logger.info(f"Comparison report generated: {output_file}")
        logger.info(f"Total APIs analyzed: {len(api_folders)}")

def main():
    """Main function to run the API comparison analysis"""
    comparison_dir = "/home/runner/work/personal/personal/comparision"
    output_file = "/home/runner/work/personal/personal/api_comparison_report.xlsx"
    
    if not os.path.exists(comparison_dir):
        logger.error(f"Comparison directory not found: {comparison_dir}")
        return
    
    analyzer = APIComparisonAnalyzer(comparison_dir)
    analyzer.generate_comparison_report(output_file)
    
    print(f"\n✅ API Comparison Report Generated: {output_file}")
    print("📊 The report includes:")
    print("   - Summary sheet with overview statistics")
    print("   - Individual sheets for each API comparison")
    print("   - Detailed field path analysis")
    print("   - Type comparisons between SAAS and Legacy")
    print("   - Senior analyst observations and notes")
    print("   - Empty 'Team Comments' column for review")

if __name__ == "__main__":
    main()