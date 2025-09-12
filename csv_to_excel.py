#!/usr/bin/env python3
"""
CSV to Excel Converter

This script combines multiple CSV files into a single Excel workbook,
with each CSV file placed on a separate sheet.

Usage:
    python csv_to_excel.py file1.csv file2.csv file3.csv -o output.xlsx
    python csv_to_excel.py *.csv -o combined_data.xlsx
"""

import argparse
import os
import sys
from pathlib import Path
from typing import List

try:
    import pandas as pd
except ImportError:
    print("Error: pandas is required. Install it with: pip install pandas")
    sys.exit(1)

try:
    import openpyxl
except ImportError:
    print("Error: openpyxl is required. Install it with: pip install openpyxl")
    sys.exit(1)


def validate_csv_files(csv_files: List[str]) -> List[str]:
    """Validate that all provided files exist and are CSV files."""
    valid_files = []
    for file_path in csv_files:
        if not os.path.exists(file_path):
            print(f"Warning: File '{file_path}' does not exist. Skipping.")
            continue
        if not file_path.lower().endswith('.csv'):
            print(f"Warning: File '{file_path}' is not a CSV file. Skipping.")
            continue
        valid_files.append(file_path)
    return valid_files


def get_sheet_name(file_path: str) -> str:
    """Generate a valid Excel sheet name from a file path."""
    # Get filename without extension
    name = Path(file_path).stem
    
    # Excel sheet names cannot be longer than 31 characters
    if len(name) > 31:
        name = name[:31]
    
    # Excel sheet names cannot contain: \ / ? * [ ]
    invalid_chars = ['\\', '/', '?', '*', '[', ']']
    for char in invalid_chars:
        name = name.replace(char, '_')
    
    return name


def combine_csv_to_excel(csv_files: List[str], output_file: str) -> None:
    """Combine multiple CSV files into a single Excel workbook."""
    
    # Validate input files
    valid_files = validate_csv_files(csv_files)
    
    if not valid_files:
        print("Error: No valid CSV files found.")
        sys.exit(1)
    
    print(f"Processing {len(valid_files)} CSV files...")
    
    # Create Excel writer
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        sheet_names_used = set()
        
        for i, csv_file in enumerate(valid_files):
            try:
                print(f"Processing: {csv_file}")
                
                # Read CSV file
                df = pd.read_csv(csv_file)
                
                # Generate sheet name
                sheet_name = get_sheet_name(csv_file)
                
                # Ensure unique sheet name
                original_name = sheet_name
                counter = 1
                while sheet_name in sheet_names_used:
                    if len(original_name) > 28:  # Leave room for counter
                        sheet_name = f"{original_name[:28]}_{counter}"
                    else:
                        sheet_name = f"{original_name}_{counter}"
                    counter += 1
                
                sheet_names_used.add(sheet_name)
                
                # Write to Excel sheet
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                
                print(f"  -> Added to sheet '{sheet_name}' ({len(df)} rows, {len(df.columns)} columns)")
                
            except Exception as e:
                print(f"Error processing {csv_file}: {str(e)}")
                continue
    
    print(f"\nSuccessfully created Excel file: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Combine multiple CSV files into a single Excel workbook",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s file1.csv file2.csv file3.csv -o output.xlsx
  %(prog)s data/*.csv -o combined_data.xlsx
  %(prog)s *.csv -o workbook.xlsx
        """
    )
    
    parser.add_argument(
        'csv_files',
        nargs='+',
        help='One or more CSV files to combine'
    )
    
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Output Excel file name (e.g., output.xlsx)'
    )
    
    args = parser.parse_args()
    
    # Ensure output file has .xlsx extension
    if not args.output.lower().endswith('.xlsx'):
        args.output += '.xlsx'
    
    # Check if output file already exists
    if os.path.exists(args.output):
        response = input(f"File '{args.output}' already exists. Overwrite? (y/N): ")
        if response.lower() not in ['y', 'yes']:
            print("Operation cancelled.")
            sys.exit(0)
    
    try:
        combine_csv_to_excel(args.csv_files, args.output)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()