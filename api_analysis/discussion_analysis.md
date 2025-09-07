# discussion API Analysis
**Legacy vs SaaS Comparison**

## Executive Summary

- **4 new fields** added in SaaS
- **5 fields** removed from Legacy (missing in SaaS)
- **2 potential field renames** detected
- **5 fields** have type changes

## Overview
| Metric | Legacy | SaaS | Change |
|--------|--------|------|--------|
| Total Fields | 13 | 12 | -1 |
| New Fields | - | 4 | +4 |
| Removed Fields | 5 | - | -5 |
| Common Fields | 8 | 8 | 0 |
| Type Changes | - | 5 | 5 |

## 🆕 New Fields Added in SaaS
These fields are present in SaaS but not in Legacy:

| Field Name | Type | Notes |
|------------|------|-------|
| `[0].discussionlink` | NoneType | New functionality |
| `[0].isHidden` | bool | New functionality |
| `[0].replyId` | int | New functionality |
| `[0].studentHash` | str | New functionality |

## ❌ Fields Removed from Legacy
These fields were present in Legacy but are missing in SaaS:

| Field Name | Type | Impact |
|------------|------|--------|
| `[0].courseId` | str | Functionality removed/changed |
| `[0].coursePk` | str | Functionality removed/changed |
| `[0].discussionLink` | str | Functionality removed/changed |
| `[0].employeeId` | str | Functionality removed/changed |
| `[0].reply_id` | str | Functionality removed/changed |

## 🔄 Fields with Type Changes
These fields exist in both but have different data types:

| Field Name | Legacy Type | SaaS Type | Impact |
|------------|-------------|-----------|--------|
| `[0].discussionId` | str | int | ⚠️ Breaking change |
| `[0].attemptPk` | str | NoneType | ⚠️ Breaking change |
| `[0].assignmentPk` | str | int | ⚠️ Breaking change |
| `[0].escalationReason` | str | NoneType | ⚠️ Breaking change |
| `[0].group` | str | NoneType | ⚠️ Breaking change |

## 🏷️ Potential Field Renames
These appear to be renamed fields (similar names/types):

| Legacy Field | SaaS Field | Legacy Type | SaaS Type | Confidence |
|--------------|------------|-------------|-----------|------------|
| `[0].reply_id` | `[0].replyId` | str | int | Medium |
| `[0].discussionLink` | `[0].discussionlink` | str | NoneType | Medium |

## Sample Data Structure

### Legacy Sample
```json
[
  {
    "employeeId": "200818094",
    "coursePk": "3352",
    "assignmentPk": "34509",
    "group": "A",
    "attemptPk": "716203.1",
    "courseId": "BUS520260VA001-1238-001",
    "discussionId": "12291",
    "submittedDate": "2023-10-13 03:12:34",
    "discussionLink": "https://qacanvas.strayer.edu/courses/sis_course_id:BUS520260VA001-1238-001/gradebook/speed_grader?assignment_id=34509&student_id=55106",
    "discussionTitle": "Week 2 Discussion - Difficult Decisions",
    "escalated": true,
    "escalationReason": "xxx1111",
    "reply_id": "1544"
  },
  {
    "employeeId": "200818094",
    "coursePk": "3352",
    "assignmentPk": "34509",
    "group": "A",
    "attemptPk": "716203.1",
    "courseId": "BUS520260VA001-1238-001",
    "discussionId": "12291",
    "submittedDate": "2023-11-03 05:08:17",
    "discussionLink": "https://qacanvas.strayer.edu/courses/sis_course_id:BUS520260VA001-1238-001/gradebook/speed_grader?assignment_id=34509&student_id=55106",
    "discussionTitle": "...
```

### SaaS Sample
```json
[
  {
    "studentHash": "YzI0YWI3NTUtNDkyNS00ZDg4LThmYWYtYzAwZjU3ZjFjODk5::NzgwMTg5N2YtZmVhMS00ODQxLWFmYmQtYzc2NzI3YjBkY2I1",
    "assignmentPk": 562944,
    "group": null,
    "attemptPk": null,
    "discussionId": 562944,
    "submittedDate": "Jun 25, 2025, 6:27:17 PM",
    "discussionTitle": "Week 8 Discussion - Creator varius curso ea demitto amo.",
    "replyId": 863,
    "discussionlink": null,
    "escalationReason": null,
    "escalated": false,
    "isHidden": false
  },
  {
    "studentHash": "Zjk0MGRlZGEtZDE0MS00MmFhLWEwZmEtYTQzZjY3M2NlNGZk::MjIxNDNlYzgtYWM5Zi00NDNkLTkxZGItNmVjMzI4ZTVmZTI2",
    "assignmentPk": 562944,
    "group": null,
    "attemptPk": null,
    "discussionId": 562944,
    "submittedDate": "Mar 10, 2025, 3:29:20 AM",
    "discussionTitle": "Week 8 Discussion - Creator varius curso ea demitto amo.",
    "replyId": 957,
    "discussionlink": null,
    "escalationReason": null,
    "escalated": false,
    "isHidden": false
  }
]
```

## Recommendations

1. **Review new fields**: 4 new fields have been added. Ensure consuming applications can handle these additions.
2. **Handle removed fields**: 5 fields are no longer available. Update consuming applications accordingly.
3. **Address type changes**: 5 fields have changed types. This may require data parsing updates.
4. **Verify renames**: 2 potential field renames detected. Confirm these are intentional changes.
