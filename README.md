# CSV to Excel Converter

A Python utility to combine multiple CSV files into a single Excel workbook, with each CSV file placed on a separate sheet.

## Features

- Combines multiple CSV files into one Excel workbook
- Each CSV file becomes a separate sheet in the workbook
- Automatically handles sheet naming (based on CSV filenames)
- Validates input files and handles errors gracefully
- Supports command-line interface with helpful options

## Requirements

- Python 3.6 or higher
- pandas >= 2.0.0
- openpyxl >= 3.1.0

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python csv_to_excel.py file1.csv file2.csv file3.csv -o output.xlsx
```

### Using Wildcards

```bash
# Combine all CSV files in current directory
python csv_to_excel.py *.csv -o combined_data.xlsx

# Combine all CSV files in a specific directory
python csv_to_excel.py data/*.csv -o combined_data.xlsx
```

### Command Line Options

- `csv_files`: One or more CSV files to combine (required)
- `-o, --output`: Output Excel file name (required)
- `-h, --help`: Show help message

### Examples

1. **Combine specific files:**
```bash
python csv_to_excel.py employees.csv products.csv sales.csv -o company_data.xlsx
```

2. **Combine all CSV files in test_data directory:**
```bash
python csv_to_excel.py test_data/*.csv -o test_results.xlsx
```

## Features Details

### Sheet Naming
- Sheet names are derived from CSV filenames (without extension)
- Sheet names are automatically truncated to 31 characters (Excel limit)
- Invalid characters (`\ / ? * [ ]`) are replaced with underscores
- Duplicate sheet names get numeric suffixes (`_1`, `_2`, etc.)

### Error Handling
- Non-existent files are skipped with warnings
- Non-CSV files are skipped with warnings
- Individual file processing errors don't stop the entire operation
- Output file overwrite confirmation

### Data Preservation
- All data from CSV files is preserved
- Column headers are maintained
- Data types are automatically inferred by pandas

## Sample Test Data

The repository includes sample CSV files in the `test_data/` directory:
- `employees.csv`: Employee information
- `products.csv`: Product catalog
- `financial_data.csv`: Financial records

Test the script with:
```bash
python csv_to_excel.py test_data/*.csv -o sample_output.xlsx
```

## License

This project is available for personal and educational use.