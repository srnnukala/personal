# API Comparison Tools - Quick Start Guide

## Overview

This repository contains tools for analyzing and managing API comparison data between SAAS and Legacy systems.

## Available Tools

### 1. API Comparison Tool (`api_comparison_tool.py`)

Generates comprehensive comparison reports between SAAS and Legacy API responses.

**Usage:**
```bash
python api_comparison_tool.py
```

**Output:**
- `api_comparison_report.xlsx` - Excel report with multiple sheets (one per API)
- `api_comparison_csv/` - Directory with individual CSV files
- `all_apis_combined.csv` - Combined CSV with all API comparisons

**Documentation:** See `API_COMPARISON_README.md`

### 2. User Comments Tool (`add_user_comments.py`)

Allows team members to add, edit, and manage comments in the API comparison report.

**Interactive Mode:**
```bash
python add_user_comments.py api_comparison_report.xlsx
```

**Non-Interactive Mode:**
```bash
python add_user_comments.py api_comparison_report.xlsx \
    --api "course-activity-detail" \
    --field "courseActivityScore" \
    --comment "Priority: HIGH - Critical field for activity tracking"
```

**Documentation:** See `USER_COMMENTS_README.md`

## Workflow

### Step 1: Generate Comparison Report

```bash
# Generate initial comparison report
python api_comparison_tool.py
```

This creates `api_comparison_report.xlsx` with all field comparisons.

### Step 2: Add Team Comments

Use the User Comments Tool to add migration notes, priorities, and decisions:

```bash
# Interactive mode - best for collaborative review sessions
python add_user_comments.py api_comparison_report.xlsx

# Or use command-line for batch updates
python add_user_comments.py api_comparison_report.xlsx \
    --api "instructor-config" \
    --field "settings.autoSave" \
    --comment "Default to true for new users"
```

### Step 3: Review and Plan Migration

Open the commented report in Excel to:
- Review field-by-field differences
- Read team comments and decisions
- Plan migration strategies
- Create test cases

## Quick Examples

### Example 1: Adding High-Priority Comments

```bash
python add_user_comments.py api_comparison_report.xlsx \
    --api "course-activity-detail" \
    --field "courseActivityScore" \
    --comment "Priority: HIGH - Core metric for student progress"
```

### Example 2: Interactive Review Session

```bash
# Start interactive mode
python add_user_comments.py api_comparison_report.xlsx

# Then use menu to:
# 1. List all APIs
# 2. View fields in an API
# 3. Add comments with full field context
# 4. Search across all APIs
# 5. Save when done
```

### Example 3: Batch Comment Updates

Create a script for common comment patterns:

```bash
#!/bin/bash

REPORT="api_comparison_report.xlsx"

# Add priority comments
python add_user_comments.py $REPORT \
    --api "roster-enrollments-cu" \
    --field "studentId" \
    --comment "Priority: CRITICAL - Primary key field"

python add_user_comments.py $REPORT \
    --api "gradebook-assigments-all" \
    --field "totalPoints" \
    --comment "Priority: HIGH - Required for grade calculations"
```

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Install Dependencies

```bash
pip install pandas openpyxl
```

## File Structure

```
.
├── api_comparison_tool.py          # Main comparison tool
├── add_user_comments.py             # User comments tool
├── demo_comments.sh                 # Demo script
├── api_comparison_report.xlsx       # Generated report
├── API_COMPARISON_README.md         # Detailed comparison tool docs
├── USER_COMMENTS_README.md          # Detailed comments tool docs
├── FIELD_MAPPING_FIX.md            # Field mapping fix documentation
└── comparision/                     # Input JSON files (SAAS/Legacy)
    ├── course-activity-detail/
    │   ├── saas.json
    │   └── legacy.json
    └── ...
```

## Tips and Best Practices

### For Team Collaboration

1. **Coordinate Sessions**: Avoid multiple people editing the same API simultaneously
2. **Use Descriptive Comments**: Be specific about decisions and rationale
3. **Backup Regularly**: Save copies after major commenting sessions
4. **Use Consistent Prefixes**: E.g., "Priority:", "TODO:", "Migration:", "QA:"

### For Migration Planning

1. **Start with High-Priority APIs**: Focus on critical paths first
2. **Document Edge Cases**: Note special handling requirements
3. **Reference Stakeholders**: Mention teams or people involved in decisions
4. **Track Dependencies**: Note when fields depend on other fields

### For Development

1. **Use TODO Comments**: Mark items that need implementation work
2. **Note Format Differences**: Document data type conversions needed
3. **Flag Complex Cases**: Highlight fields needing special attention
4. **Link to Requirements**: Reference tickets or documentation

## Common Use Cases

### Migration Priority Marking

```bash
python add_user_comments.py api_comparison_report.xlsx \
    --api "authentication" \
    --field "userId" \
    --comment "Priority: CRITICAL - Must migrate first, blocking other APIs"
```

### Technical Implementation Notes

```bash
python add_user_comments.py api_comparison_report.xlsx \
    --api "gradebook-export" \
    --field "exportDate" \
    --comment "TODO: Convert from Unix timestamp to ISO 8601 format"
```

### Business Requirements

```bash
python add_user_comments.py api_comparison_report.xlsx \
    --api "course-settings" \
    --field "notifications.email" \
    --comment "Business requirement: Default to true per product team decision"
```

### QA Testing Requirements

```bash
python add_user_comments.py api_comparison_report.xlsx \
    --api "user-profile" \
    --field "status" \
    --comment "QA: Test all status values - Active, Inactive, Suspended, Deleted"
```

## Troubleshooting

### Problem: "Module not found" error

**Solution:** Install required dependencies
```bash
pip install pandas openpyxl
```

### Problem: "File not found" error

**Solution:** Make sure you're in the correct directory and the report exists
```bash
# Generate the report first
python api_comparison_tool.py

# Then add comments
python add_user_comments.py api_comparison_report.xlsx
```

### Problem: "Field not found" error

**Solution:** Check the exact field name in the Excel report or use search
```bash
# Start interactive mode and use search (command 4)
python add_user_comments.py api_comparison_report.xlsx
```

## Next Steps

1. **Generate Report**: Run `api_comparison_tool.py` to create the initial report
2. **Review Systematically**: Go through each API in the interactive mode
3. **Add Comments**: Document decisions, priorities, and notes
4. **Share with Team**: Distribute the commented report for review
5. **Update Regularly**: As decisions are made, keep the comments current

## Support and Documentation

- **API Comparison Tool**: See `API_COMPARISON_README.md`
- **User Comments Tool**: See `USER_COMMENTS_README.md`
- **Field Mapping Fix**: See `FIELD_MAPPING_FIX.md`

---

**Last Updated:** January 2026
