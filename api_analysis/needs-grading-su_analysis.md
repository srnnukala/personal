# needs-grading-su API Analysis
**Legacy vs SaaS Comparison**

## Executive Summary

- **15 new fields** added in SaaS
- **17 fields** removed from Legacy (missing in SaaS)
- **13 potential field renames** detected

## Overview
| Metric | Legacy | SaaS | Change |
|--------|--------|------|--------|
| Total Fields | 17 | 15 | -2 |
| New Fields | - | 15 | +15 |
| Removed Fields | 17 | - | -17 |
| Common Fields | 0 | 0 | 0 |
| Type Changes | - | 0 | 0 |

## 🆕 New Fields Added in SaaS
These fields are present in SaaS but not in Legacy:

| Field Name | Type | Notes |
|------------|------|-------|
| `[0].assignmentPk` | int | New functionality |
| `[0].attempts` | list | New functionality |
| `[0].attempts[0].assignmentLink` | str | New functionality |
| `[0].attempts[0].assignmentTitle` | str | New functionality |
| `[0].attempts[0].attemptOrder` | int | New functionality |
| `[0].attempts[0].attemptPk` | int | New functionality |
| `[0].attempts[0].escalated` | NoneType | New functionality |
| `[0].attempts[0].escalationReason` | NoneType | New functionality |
| `[0].attempts[0].gradeDetailsUrl` | str | New functionality |
| `[0].attempts[0].status` | str | New functionality |
| `[0].attempts[0].submittedDate` | str | New functionality |
| `[0].gradeGroup` | str | New functionality |
| `[0].is10x` | bool | New functionality |
| `[0].previousGrade` | NoneType | New functionality |
| `[0].studentHash` | str | New functionality |

## ❌ Fields Removed from Legacy
These fields were present in Legacy but are missing in SaaS:

| Field Name | Type | Impact |
|------------|------|--------|
| `assignments` | list | Functionality removed/changed |
| `assignments[0].assignmentPk` | str | Functionality removed/changed |
| `assignments[0].attempts` | list | Functionality removed/changed |
| `assignments[0].attempts[0].assignmentLink` | str | Functionality removed/changed |
| `assignments[0].attempts[0].assignmentTitle` | str | Functionality removed/changed |
| `assignments[0].attempts[0].attemptOrder` | int | Functionality removed/changed |
| `assignments[0].attempts[0].attemptPk` | str | Functionality removed/changed |
| `assignments[0].attempts[0].gradeDetailsUrl` | str | Functionality removed/changed |
| `assignments[0].attempts[0].submittedDate` | str | Functionality removed/changed |
| `assignments[0].coursePk` | str | Functionality removed/changed |
| `assignments[0].employeeId` | str | Functionality removed/changed |
| `assignments[0].escalated` | bool | Functionality removed/changed |
| `assignments[0].escalationReason` | NoneType | Functionality removed/changed |
| `assignments[0].group` | NoneType | Functionality removed/changed |
| `assignments[0].is10x` | bool | Functionality removed/changed |
| `assignments[0].learnerPk` | str | Functionality removed/changed |
| `assignments[0].previousGrade` | str | Functionality removed/changed |

## 🏷️ Potential Field Renames
These appear to be renamed fields (similar names/types):

| Legacy Field | SaaS Field | Legacy Type | SaaS Type | Confidence |
|--------------|------------|-------------|-----------|------------|
| `assignments[0].assignmentPk` | `[0].assignmentPk` | str | int | Medium |
| `assignments[0].is10x` | `[0].is10x` | bool | bool | High |
| `assignments[0].group` | `[0].gradeGroup` | NoneType | str | Medium |
| `assignments[0].attempts[0].assignmentLink` | `[0].attempts[0].assignmentLink` | str | str | High |
| `assignments[0].escalated` | `[0].attempts[0].escalated` | bool | NoneType | Medium |
| `assignments[0].attempts[0].attemptPk` | `[0].attempts[0].attemptPk` | str | int | Medium |
| `assignments[0].attempts` | `[0].attempts` | list | list | High |
| `assignments[0].previousGrade` | `[0].previousGrade` | str | NoneType | Medium |
| `assignments[0].attempts[0].submittedDate` | `[0].attempts[0].submittedDate` | str | str | High |
| `assignments[0].attempts[0].gradeDetailsUrl` | `[0].attempts[0].gradeDetailsUrl` | str | str | High |
| `assignments[0].attempts[0].attemptOrder` | `[0].attempts[0].attemptOrder` | int | int | High |
| `assignments[0].attempts[0].assignmentTitle` | `[0].attempts[0].assignmentTitle` | str | str | High |
| `assignments[0].escalationReason` | `[0].attempts[0].escalationReason` | NoneType | NoneType | High |

## Sample Data Structure

### Legacy Sample
```json
{
  "assignments": [
    {
      "employeeId": "2562227",
      "learnerPk": "2757",
      "coursePk": "1284",
      "assignmentPk": "20663",
      "previousGrade": "0",
      "is10x": false,
      "escalationReason": null,
      "escalated": false,
      "group": null,
      "attempts": [
        {
          "attemptPk": "138322",
          "attemptOrder": 1,
          "assignmentTitle": "[u05a1] Week 5 Assignment 1: Educational Theories in Practice",
          "submittedDate": "2023-07-05T08:46:11-05:00",
          "gradeDetailsUrl": "https://qacapella.instructure.com/courses/1284/gradebook",
          "assignmentLink": "https://qacapella.instructure.com/courses/1284/gradebook/speed_grader?assignment_id=20663&student_id=2757&facAttempt=1"
        }
      ]
    },
    {
      "employeeId": "2573717",
      "learnerPk": "2604",
      "coursePk": "1284",
      "assignmentPk": "20663",
      "previousGrade": "0",
      "is10x": false,
      "escalationReason": null,
      "escalated": fa...
```

### SaaS Sample
```json
[
  {
    "studentHash": "Pd1q+DdIAG00qWRoBSeXVijuFcdJ5F/alwAMxXXm3dO/qrhrDVgEGNLgHqrAKRZez22scUsqpVTqo9d9h2D+Zg==::nVtx8WMBk3hTo+TaAJSGVA==",
    "assignmentPk": 1198108,
    "is10x": false,
    "gradeGroup": "B",
    "previousGrade": null,
    "attempts": [
      {
        "attemptPk": 42245653,
        "attemptOrder": 1,
        "assignmentTitle": "Week 6 Discussion - Using Financial Statements for Your Life",
        "submittedDate": "2025-08-15T03:55:23Z",
        "gradeDetailsUrl": "https://devcanvas.strayer.edu/courses/21944/gradebook",
        "assignmentLink": "https://devcanvas.strayer.edu/courses/21944/gradebook/speed_grader?assignment_id=1198108&student_id=12813&facAttempt=1",
        "escalationReason": null,
        "escalated": null,
        "status": "SUBMITTED"
      }
    ]
  },
  {
    "studentHash": "obul297jmR2eQTucz8M8/RPiXAeeUw4M2vhKBWp2C6TZN3EiLWpmTaLhzDLGkw1hD7DJQjLARwiBrQuNEAK/kQ==::QskExaXBjeGGER4vJ1SfGQ==",
    "assignmentPk": 1218474,
    "is10x": false,
  ...
```

## Recommendations

1. **Review new fields**: 15 new fields have been added. Ensure consuming applications can handle these additions.
2. **Handle removed fields**: 17 fields are no longer available. Update consuming applications accordingly.
4. **Verify renames**: 13 potential field renames detected. Confirm these are intentional changes.
