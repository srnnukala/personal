# submit-grades-{{exam}}-course-sis-id-{{course-sis-id}} API Analysis
**Legacy vs SaaS Comparison**

## Executive Summary

- **7 new fields** added in SaaS
- **7 fields** removed from Legacy (missing in SaaS)
- **5 potential field renames** detected

## Overview
| Metric | Legacy | SaaS | Change |
|--------|--------|------|--------|
| Total Fields | 10 | 10 | +0 |
| New Fields | - | 7 | +7 |
| Removed Fields | 7 | - | -7 |
| Common Fields | 3 | 3 | 0 |
| Type Changes | - | 0 | 0 |

## 🆕 New Fields Added in SaaS
These fields are present in SaaS but not in Legacy:

| Field Name | Type | Notes |
|------------|------|-------|
| `learnerGrades` | list | New functionality |
| `learnerGrades[0].gradeLetter` | str | New functionality |
| `learnerGrades[0].needsGrading` | bool | New functionality |
| `learnerGrades[0].studentHash` | str | New functionality |
| `learnerGrades[0].submitted` | int | New functionality |
| `learnerGrades[0].totalPoints` | float | New functionality |
| `learnerGrades[0].totalSubmissions` | int | New functionality |

## ❌ Fields Removed from Legacy
These fields were present in Legacy but are missing in SaaS:

| Field Name | Type | Impact |
|------------|------|--------|
| `gradeDetails` | list | Functionality removed/changed |
| `gradeDetails[0].employeeId` | str | Functionality removed/changed |
| `gradeDetails[0].gradeLetter` | str | Functionality removed/changed |
| `gradeDetails[0].needsGrading` | bool | Functionality removed/changed |
| `gradeDetails[0].submitted` | int | Functionality removed/changed |
| `gradeDetails[0].totalPoints` | float | Functionality removed/changed |
| `gradeDetails[0].totalSubmissions` | int | Functionality removed/changed |

## 🏷️ Potential Field Renames
These appear to be renamed fields (similar names/types):

| Legacy Field | SaaS Field | Legacy Type | SaaS Type | Confidence |
|--------------|------------|-------------|-----------|------------|
| `gradeDetails[0].needsGrading` | `learnerGrades[0].needsGrading` | bool | bool | High |
| `gradeDetails[0].totalSubmissions` | `learnerGrades[0].totalSubmissions` | int | int | High |
| `gradeDetails[0].totalPoints` | `learnerGrades[0].totalPoints` | float | float | High |
| `gradeDetails[0].gradeLetter` | `learnerGrades[0].gradeLetter` | str | str | High |
| `gradeDetails[0].submitted` | `learnerGrades[0].submitted` | int | int | High |

## Sample Data Structure

### Legacy Sample
```json
{
  "status": "NOT_SUBMITTED",
  "submittedDt": null,
  "submittedBy": null,
  "gradeDetails": [
    {
      "employeeId": "200861690",
      "gradeLetter": "C",
      "needsGrading": true,
      "totalPoints": 702.3,
      "submitted": 15,
      "totalSubmissions": 18
    },
    {
      "employeeId": "200836155",
      "gradeLetter": "F",
      "needsGrading": false,
      "totalPoints": 140,
      "submitted": 1,
      "totalSubmissions": 18
    },
    {
      "employeeId": "200550064",
      "gradeLetter": "F",
      "needsGrading": true,
      "totalPoints": 150,
      "submitted": 9,
      "totalSubmissions": 18
    },
    {
      "employeeId": "200860388",
      "gradeLetter": "F",
      "needsGrading": true,
      "totalPoints": 149.52,
      "submitted": 3,
      "totalSubmissions": 18
    },
    {
      "employeeId": "200495059",
      "gradeLetter": "F",
      "needsGrading": false,
      "totalPoints": 232,
      "submitted": 3,
      "totalSubmissions": 18
    },
    {
    ...
```

### SaaS Sample
```json
{
  "status": "NOT_SUBMITTED",
  "submittedDt": null,
  "submittedBy": null,
  "learnerGrades": [
    {
      "studentHash": "obul297jmR2eQTucz8M8/RPiXAeeUw4M2vhKBWp2C6TZN3EiLWpmTaLhzDLGkw1hD7DJQjLARwiBrQuNEAK/kQ==::QskExaXBjeGGER4vJ1SfGQ==",
      "gradeLetter": "A",
      "needsGrading": true,
      "totalPoints": 397.29,
      "submitted": 13,
      "totalSubmissions": 24
    },
    {
      "studentHash": "IvrJsMi++WETPs+DmPWbZAVgONdlrfXN9fLRExmcuhh+Cbg8FH94fnuccE3PROaxUl1Z+cUHgwwvVXJmRZjEjg==::psMwHBLhV+WXthahST23zg==",
      "gradeLetter": "A",
      "needsGrading": true,
      "totalPoints": 394.01,
      "submitted": 12,
      "totalSubmissions": 24
    },
    {
      "studentHash": "6CErWjU9T6a6ihTMaMVI5NuNXJbQAj/uImNx0XyxEoyVf0yz7hROwLiKBaN4aZABJm0MMoRO4rkuPXKGXrBTxQ==::bWOvgCUIUI6rUdoMuJnJjg==",
      "gradeLetter": "A",
      "needsGrading": true,
      "totalPoints": 393.62,
      "submitted": 12,
      "totalSubmissions": 24
    },
    {
      "studentHash": "EUsXZHIQC25Mt...
```

## Recommendations

1. **Review new fields**: 7 new fields have been added. Ensure consuming applications can handle these additions.
2. **Handle removed fields**: 7 fields are no longer available. Update consuming applications accordingly.
4. **Verify renames**: 5 potential field renames detected. Confirm these are intentional changes.
