# User Comments Tool for API Comparison Reports

## Overview

The User Comments Tool allows team members to add, edit, and manage comments in the API comparison report's "Team Comments" column. This tool provides both interactive and non-interactive modes for efficiently documenting migration strategies, decisions, and observations for each field in the API comparison.

## Features

- **Interactive CLI Interface**: Browse APIs, view fields, and add comments interactively
- **Non-Interactive Mode**: Add comments via command-line for automation or scripting
- **Field Search**: Search for fields across all APIs
- **Comment Management**: Add, update, and view comments for specific fields
- **Safe File Handling**: Option to save to a new file without overwriting the original
- **Progress Tracking**: See which fields already have comments at a glance

## Installation

The tool requires Python 3.6+ and the following dependencies:

```bash
pip install pandas openpyxl
```

## Usage

### Interactive Mode

The interactive mode provides a menu-driven interface for managing comments:

```bash
python add_user_comments.py api_comparison_report.xlsx
```

**Available Commands:**

1. **List APIs** - View all available APIs with field counts and comment statistics
2. **View fields for an API** - Display all fields in a specific API
3. **Add/edit comment for a field** - Add or update a comment with full field context
4. **Search for a field** - Search for fields across all APIs by name
5. **Save and exit** - Save changes and close the tool
6. **Exit without saving** - Close without saving changes

### Non-Interactive Mode

For scripting or automation, use command-line arguments:

```bash
# Add a single comment
python add_user_comments.py api_comparison_report.xlsx \
    --api "course-activity-detail" \
    --field "courseActivityScore" \
    --comment "Migration priority: HIGH - Critical field for activity tracking"

# Save to a different file
python add_user_comments.py api_comparison_report.xlsx \
    --api "instructor-config" \
    --field "settings.notifications" \
    --comment "Review with UX team before migration" \
    --output updated_report.xlsx
```

## Examples

### Example 1: Interactive Session

```
$ python add_user_comments.py api_comparison_report.xlsx

======================================================================
API Comparison Report - User Comments Tool
======================================================================

Available commands:
  1. List APIs
  2. View fields for an API
  3. Add/edit comment for a field
  4. Search for a field
  5. Save and exit
  6. Exit without saving

Enter command number: 1

📋 Found 24 APIs:
  1. assignment-extension (45 fields, 0 with comments)
  2. course-activity-detail (89 fields, 0 with comments)
  3. course-activity-overview (67 fields, 0 with comments)
  ...

Enter command number: 3

Enter API name: course-activity-detail
Enter field path: courseActivityScore

📋 Field Information:
  Field Path: courseActivityScore
  Present in SAAS: Yes
  Present in Legacy: Yes
  Type in SAAS: string
  Type in Legacy: string
  Notes: String values differ between systems
  Current Comment: (empty)

Enter new comment (or press Enter to keep current):
> Critical field - must maintain precision during migration

✅ Comment added successfully!
```

### Example 2: Batch Adding Comments

Create a shell script to add multiple comments:

```bash
#!/bin/bash

# Migration priority comments
python add_user_comments.py api_comparison_report.xlsx \
    --api "course-activity-detail" \
    --field "courseActivityScore" \
    --comment "Priority: HIGH - Core activity metric"

python add_user_comments.py api_comparison_report.xlsx \
    --api "gradebook-assignments-all" \
    --field "totalPoints" \
    --comment "Priority: HIGH - Critical for grade calculations"

python add_user_comments.py api_comparison_report.xlsx \
    --api "roster-enrollments-cu" \
    --field "enrollmentStatus" \
    --comment "Priority: MEDIUM - Verify status mapping with registrar"
```

### Example 3: Searching for Fields

```
Enter command number: 4

Enter search term: activity

🔍 Searching for 'activity'...

✓ Found 12 matches:
  1. [course-activity-detail] activityScoreDist
  2. [course-activity-detail] courseActivityScore
  3. [course-activity-overview] activityScore ✓
  4. [course-activity-section] sectionActivity
  ...
```

## Use Cases

### For Migration Planning

Document migration priorities and strategies:

```
"Migration priority: HIGH - User authentication critical path"
"Map to new SAAS field: user.profile.avatar_url"
"Deprecate in SAAS - functionality moved to settings API"
```

### For Development Teams

Add implementation notes:

```
"TODO: Verify date format conversion in transformer"
"Uses legacy encoding - requires UTF-8 conversion"
"Complex nested structure - break into separate queries"
```

### For QA Teams

Document testing requirements:

```
"Edge case: Handle null values from legacy system"
"Test with max string length: 500 characters"
"Verify timezone conversion for all date fields"
```

### For Business Analysts

Track feature decisions:

```
"Confirmed with product: Keep both formats during transition"
"Business requirement: Maintain backwards compatibility"
"User training needed: Field name changing from 'score' to 'grade'"
```

## Best Practices

1. **Be Specific**: Write clear, actionable comments that others can understand
2. **Use Consistent Format**: Consider using prefixes like "Priority:", "TODO:", "Note:"
3. **Reference Stakeholders**: Mention teams or people when decisions involve them
4. **Track Decisions**: Document why choices were made for future reference
5. **Regular Backups**: Save copies of the report after major commenting sessions
6. **Team Review**: Encourage team members to review and add comments collaboratively

## File Management

- **Original File Preservation**: Always use `--output` to save to a new file during initial testing
- **Version Control**: Consider tracking the Excel reports in git (though they're binary)
- **Backup Strategy**: Keep dated backups before major comment sessions
- **Merge Strategy**: When multiple team members are commenting, coordinate to avoid conflicts

## Command Reference

### Command-Line Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `excel_file` | Yes | Path to the API comparison Excel report |
| `--api` | No* | API name (required for non-interactive mode) |
| `--field` | No* | Field path (required for non-interactive mode) |
| `--comment` | No* | Comment text (required for non-interactive mode) |
| `--output`, `-o` | No | Output file path (default: overwrites input file) |

*Required together for non-interactive mode

### Interactive Mode Commands

| Number | Command | Description |
|--------|---------|-------------|
| 1 | List APIs | Show all APIs with statistics |
| 2 | View fields | Display fields for a specific API |
| 3 | Add/edit comment | Add or update a field comment |
| 4 | Search | Find fields across all APIs |
| 5 | Save and exit | Save changes and close |
| 6 | Exit without saving | Close without saving |

## Troubleshooting

### "API not found" Error

Make sure you're using the exact API name as shown in the Excel sheet tabs. Use command 1 in interactive mode to see the exact names.

### "Field not found" Error

Field paths are case-sensitive and must match exactly. Use command 2 to view all fields in an API, or command 4 to search for fields.

### Excel File Locked

If you get a permission error, make sure the Excel file isn't open in another application.

### Memory Issues with Large Reports

For very large reports, the tool loads all sheets into memory. Consider commenting on one API at a time using the `--output` flag to create incremental backups.

## Tips and Tricks

1. **Quick Comment Updates**: Use the `--output` flag to create a new file, verify changes, then rename it
2. **Search Before Adding**: Use the search feature (command 4) to find related fields that might need similar comments
3. **Collaborative Commenting**: Have different team members focus on different APIs to avoid conflicts
4. **Template Comments**: Keep a file of standard comments for common patterns (e.g., "Priority: HIGH", "Needs review")
5. **Export Comments**: The updated Excel file can be exported to CSV for further analysis or reporting

## Integration with Existing Workflow

This tool is designed to complement the existing API comparison workflow:

1. **Initial Analysis**: Run `api_comparison_tool.py` to generate the comparison report
2. **Team Review**: Use `add_user_comments.py` to add comments during team review sessions
3. **Migration Planning**: Reference the commented report to plan field-by-field migration strategies
4. **Implementation**: Developers reference comments during actual migration work
5. **Testing**: QA teams use comments to create targeted test cases

## Future Enhancements

Potential improvements that could be added:

- Export comments to a separate CSV file
- Import comments from a CSV file
- Filter fields by presence (SAAS only, Legacy only, both)
- Comment templates for common scenarios
- Bulk comment updates via CSV import
- Comment history tracking
- Multi-user conflict detection

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the examples for common use cases
3. Use the `--help` flag for command reference
4. Check the log output for detailed error messages

---

**Tool Version**: 1.0  
**Compatible Report Format**: API Comparison Report v1.0 (generated by api_comparison_tool.py)  
**Last Updated**: January 2026
