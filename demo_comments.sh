#!/bin/bash

# Demo script for the User Comments Tool
# This script demonstrates various uses of the add_user_comments.py tool

echo "=========================================="
echo "User Comments Tool - Demo Script"
echo "=========================================="
echo ""

# Check if the report exists
if [ ! -f "api_comparison_report.xlsx" ]; then
    echo "❌ Error: api_comparison_report.xlsx not found"
    exit 1
fi

echo "✓ Found api_comparison_report.xlsx"
echo ""

# Create a working copy for testing
echo "Creating a test copy of the report..."
cp api_comparison_report.xlsx demo_report.xlsx
echo "✓ Created demo_report.xlsx"
echo ""

# Example 1: Add a high-priority migration comment
echo "Example 1: Adding a HIGH priority comment"
python add_user_comments.py demo_report.xlsx \
    --api "course-activity-detail" \
    --field "courseActivityScore" \
    --comment "Priority: HIGH - Core activity metric, critical for student progress tracking"
echo ""

# Example 2: Add a technical implementation note
echo "Example 2: Adding a technical implementation note"
python add_user_comments.py demo_report.xlsx \
    --api "course-activity-detail" \
    --field "avgGrade" \
    --comment "TODO: Verify precision handling - legacy uses 2 decimals, SAAS uses 4"
echo ""

# Example 3: Add a business requirement comment
echo "Example 3: Adding a business requirement"
python add_user_comments.py demo_report.xlsx \
    --api "instructor-config" \
    --field "generalProperties" \
    --comment "Business requirement: Review all general properties with product team"
echo ""

# Example 4: Add a migration strategy comment
echo "Example 4: Adding a migration strategy"
python add_user_comments.py demo_report.xlsx \
    --api "gradebook-assigments-all" \
    --field "ACC100.assignments" \
    --comment "Migration: Verify assignment data structure matches new schema"
echo ""

# Example 5: Add a QA testing note
echo "Example 5: Adding a QA testing requirement"
python add_user_comments.py demo_report.xlsx \
    --api "roster-enrollments-cu" \
    --field "message[0].HASH" \
    --comment "QA: Verify hash generation algorithm matches legacy system"
echo ""

echo "=========================================="
echo "Demo Complete!"
echo "=========================================="
echo ""
echo "✅ Added 5 sample comments to demo_report.xlsx"
echo ""
echo "You can now:"
echo "  1. Open demo_report.xlsx in Excel to see the comments"
echo "  2. Run: python add_user_comments.py demo_report.xlsx (for interactive mode)"
echo "  3. Delete demo_report.xlsx when done testing"
echo ""
