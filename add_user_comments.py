#!/usr/bin/env python3
"""
User Comments Tool for API Comparison Reports

This tool allows users to add, edit, and view comments in the API comparison
report's 'Team Comments' column. It provides an interactive CLI interface for
managing comments across all API sheets.
"""

import pandas as pd
import openpyxl
from pathlib import Path
import logging
import sys
from typing import Dict, List, Optional

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class CommentManager:
    def __init__(self, excel_file: str):
        self.excel_file = Path(excel_file)
        self.workbook = None
        self.sheets_data = {}
        
        if not self.excel_file.exists():
            raise FileNotFoundError(f"Excel file not found: {excel_file}")
    
    def load_report(self):
        """Load the Excel report and read all sheets"""
        logger.info(f"Loading report from {self.excel_file}")
        
        try:
            # Load with openpyxl to preserve formatting
            self.workbook = openpyxl.load_workbook(self.excel_file)
            
            # Read all sheets with pandas for easier data manipulation
            excel_data = pd.ExcelFile(self.excel_file)
            for sheet_name in excel_data.sheet_names:
                if sheet_name != 'Summary':  # Skip summary sheet
                    df = pd.read_excel(excel_data, sheet_name=sheet_name)
                    self.sheets_data[sheet_name] = df
            
            logger.info(f"Loaded {len(self.sheets_data)} API sheets")
            return True
        except Exception as e:
            logger.error(f"Error loading report: {e}")
            return False
    
    def list_apis(self) -> List[str]:
        """Get list of all API names in the report"""
        return list(self.sheets_data.keys())
    
    def get_api_fields(self, api_name: str) -> Optional[pd.DataFrame]:
        """Get all fields for a specific API"""
        if api_name in self.sheets_data:
            return self.sheets_data[api_name]
        return None
    
    def add_comment(self, api_name: str, field_path: str, comment: str) -> bool:
        """Add or update a comment for a specific field"""
        if api_name not in self.sheets_data:
            logger.error(f"API '{api_name}' not found")
            return False
        
        df = self.sheets_data[api_name]
        
        # Find the field
        mask = df['Field Path'] == field_path
        if not mask.any():
            logger.error(f"Field '{field_path}' not found in API '{api_name}'")
            return False
        
        # Ensure Team Comments column is string type
        if 'Team Comments' not in df.columns:
            df['Team Comments'] = ''
        df['Team Comments'] = df['Team Comments'].astype(str)
        
        # Update the comment
        df.loc[mask, 'Team Comments'] = comment
        logger.info(f"Comment added to '{field_path}' in '{api_name}'")
        return True
    
    def get_field_info(self, api_name: str, field_path: str) -> Optional[Dict]:
        """Get complete information about a specific field"""
        if api_name not in self.sheets_data:
            return None
        
        df = self.sheets_data[api_name]
        mask = df['Field Path'] == field_path
        
        if not mask.any():
            return None
        
        row = df[mask].iloc[0]
        return row.to_dict()
    
    def save_report(self, output_file: Optional[str] = None):
        """Save the updated report"""
        if output_file is None:
            output_file = self.excel_file
        else:
            output_file = Path(output_file)
        
        logger.info(f"Saving updated report to {output_file}")
        
        try:
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                # Write all API sheets
                for sheet_name, df in self.sheets_data.items():
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
                        adjusted_width = min(max_length + 2, 50)
                        worksheet.column_dimensions[column_letter].width = adjusted_width
                
                # Copy Summary sheet if it exists
                if self.workbook and 'Summary' in self.workbook.sheetnames:
                    summary_df = pd.read_excel(self.excel_file, sheet_name='Summary')
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
            
            logger.info("Report saved successfully")
            return True
        except Exception as e:
            logger.error(f"Error saving report: {e}")
            return False
    
    def interactive_mode(self):
        """Run interactive CLI for adding comments"""
        print("\n" + "="*70)
        print("API Comparison Report - User Comments Tool")
        print("="*70)
        
        while True:
            print("\nAvailable commands:")
            print("  1. List APIs")
            print("  2. View fields for an API")
            print("  3. Add/edit comment for a field")
            print("  4. Search for a field")
            print("  5. Save and exit")
            print("  6. Exit without saving")
            
            choice = input("\nEnter command number: ").strip()
            
            if choice == '1':
                self._list_apis_interactive()
            elif choice == '2':
                self._view_fields_interactive()
            elif choice == '3':
                self._add_comment_interactive()
            elif choice == '4':
                self._search_field_interactive()
            elif choice == '5':
                if self.save_report():
                    print("\n✅ Report saved successfully!")
                    break
                else:
                    print("\n❌ Error saving report")
            elif choice == '6':
                confirm = input("\nAre you sure you want to exit without saving? (yes/no): ").strip().lower()
                if confirm in ['yes', 'y']:
                    print("\nExiting without saving changes.")
                    break
            else:
                print("\n❌ Invalid command. Please try again.")
    
    def _list_apis_interactive(self):
        """List all APIs in interactive mode"""
        apis = self.list_apis()
        print(f"\n📋 Found {len(apis)} APIs:")
        for i, api in enumerate(apis, 1):
            df = self.sheets_data[api]
            total_fields = len(df)
            commented_fields = df['Team Comments'].notna().sum()
            print(f"  {i}. {api} ({total_fields} fields, {commented_fields} with comments)")
    
    def _view_fields_interactive(self):
        """View fields for a specific API in interactive mode"""
        api_name = input("\nEnter API name: ").strip()
        
        df = self.get_api_fields(api_name)
        if df is None:
            print(f"\n❌ API '{api_name}' not found")
            return
        
        print(f"\n📊 Fields in '{api_name}':")
        print(f"{'#':<5} {'Field Path':<50} {'Has Comment':<12}")
        print("-" * 70)
        
        for i, row in df.iterrows():
            field_path = row['Field Path'][:47] + "..." if len(str(row['Field Path'])) > 50 else str(row['Field Path'])
            has_comment = "✓" if pd.notna(row['Team Comments']) and row['Team Comments'] != '' else ""
            print(f"{i:<5} {field_path:<50} {has_comment:<12}")
    
    def _add_comment_interactive(self):
        """Add or edit a comment in interactive mode"""
        api_name = input("\nEnter API name: ").strip()
        
        if api_name not in self.sheets_data:
            print(f"\n❌ API '{api_name}' not found")
            return
        
        field_path = input("Enter field path: ").strip()
        
        # Show current field info
        field_info = self.get_field_info(api_name, field_path)
        if field_info is None:
            print(f"\n❌ Field '{field_path}' not found in API '{api_name}'")
            return
        
        print("\n📋 Field Information:")
        print(f"  Field Path: {field_info['Field Path']}")
        print(f"  Present in SAAS: {field_info['Present in SAAS']}")
        print(f"  Present in Legacy: {field_info['Present in Legacy']}")
        print(f"  Type in SAAS: {field_info['Type in SAAS']}")
        print(f"  Type in Legacy: {field_info['Type in Legacy']}")
        print(f"  Notes: {field_info['Notes']}")
        print(f"  Current Comment: {field_info.get('Team Comments', '(empty)')}")
        
        print("\nEnter new comment (or press Enter to keep current):")
        new_comment = input("> ").strip()
        
        if new_comment:
            if self.add_comment(api_name, field_path, new_comment):
                print("\n✅ Comment added successfully!")
            else:
                print("\n❌ Failed to add comment")
        else:
            print("\n⚠️  No changes made")
    
    def _search_field_interactive(self):
        """Search for fields across all APIs"""
        search_term = input("\nEnter search term: ").strip().lower()
        
        print(f"\n🔍 Searching for '{search_term}'...")
        results = []
        
        for api_name, df in self.sheets_data.items():
            mask = df['Field Path'].str.lower().str.contains(search_term, na=False)
            matches = df[mask]
            
            for _, row in matches.iterrows():
                results.append({
                    'API': api_name,
                    'Field': row['Field Path'],
                    'Has Comment': pd.notna(row['Team Comments']) and row['Team Comments'] != ''
                })
        
        if results:
            print(f"\n✓ Found {len(results)} matches:")
            for i, result in enumerate(results, 1):
                comment_indicator = "✓" if result['Has Comment'] else ""
                print(f"  {i}. [{result['API']}] {result['Field']} {comment_indicator}")
        else:
            print("\n❌ No matches found")


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Add and manage user comments in API comparison reports',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode
  python add_user_comments.py api_comparison_report.xlsx
  
  # Add a single comment (non-interactive)
  python add_user_comments.py api_comparison_report.xlsx --api "course-activity-detail" \\
      --field "message[0].activityScore" --comment "Migration priority: HIGH"
        """
    )
    
    parser.add_argument('excel_file', help='Path to the API comparison Excel report')
    parser.add_argument('--api', help='API name (for non-interactive mode)')
    parser.add_argument('--field', help='Field path (for non-interactive mode)')
    parser.add_argument('--comment', help='Comment text (for non-interactive mode)')
    parser.add_argument('--output', '-o', help='Output file path (default: overwrites input file)')
    
    args = parser.parse_args()
    
    try:
        manager = CommentManager(args.excel_file)
        
        if not manager.load_report():
            print("\n❌ Failed to load report")
            sys.exit(1)
        
        # Non-interactive mode
        if args.api and args.field and args.comment:
            if manager.add_comment(args.api, args.field, args.comment):
                output_file = args.output if args.output else args.excel_file
                if manager.save_report(output_file):
                    print(f"\n✅ Comment added and saved to {output_file}")
                else:
                    print("\n❌ Failed to save report")
                    sys.exit(1)
            else:
                print("\n❌ Failed to add comment")
                sys.exit(1)
        else:
            # Interactive mode
            manager.interactive_mode()
    
    except FileNotFoundError as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        logger.exception("Detailed error:")
        sys.exit(1)


if __name__ == "__main__":
    main()
