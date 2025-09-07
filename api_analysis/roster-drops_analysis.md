# roster-drops API Analysis
**Legacy vs SaaS Comparison**

## Executive Summary

- **5 new fields** added in SaaS
- **11 fields** removed from Legacy (missing in SaaS)
- **3 potential field renames** detected

## Overview
| Metric | Legacy | SaaS | Change |
|--------|--------|------|--------|
| Total Fields | 11 | 5 | -6 |
| New Fields | - | 5 | +5 |
| Removed Fields | 11 | - | -11 |
| Common Fields | 0 | 0 | 0 |
| Type Changes | - | 0 | 0 |

## 🆕 New Fields Added in SaaS
These fields are present in SaaS but not in Legacy:

| Field Name | Type | Notes |
|------------|------|-------|
| `[0].courseName` | str | New functionality |
| `[0].students` | list | New functionality |
| `[0].students[0].dropDate` | str | New functionality |
| `[0].students[0].firstName` | str | New functionality |
| `[0].students[0].lastName` | str | New functionality |

## ❌ Fields Removed from Legacy
These fields were present in Legacy but are missing in SaaS:

| Field Name | Type | Impact |
|------------|------|--------|
| `courses` | list | Functionality removed/changed |
| `courses[0].courseId` | str | Functionality removed/changed |
| `courses[0].courseName` | str | Functionality removed/changed |
| `courses[0].coursePk` | str | Functionality removed/changed |
| `courses[0].learners` | list | Functionality removed/changed |
| `courses[0].learners[0].droppedOutDate` | str | Functionality removed/changed |
| `courses[0].learners[0].emailId` | str | Functionality removed/changed |
| `courses[0].learners[0].employeeID` | str | Functionality removed/changed |
| `courses[0].learners[0].firstName` | str | Functionality removed/changed |
| `courses[0].learners[0].lastName` | str | Functionality removed/changed |
| `courses[0].learners[0].learnerPk` | str | Functionality removed/changed |

## 🏷️ Potential Field Renames
These appear to be renamed fields (similar names/types):

| Legacy Field | SaaS Field | Legacy Type | SaaS Type | Confidence |
|--------------|------------|-------------|-----------|------------|
| `courses[0].learners[0].firstName` | `[0].students[0].firstName` | str | str | High |
| `courses[0].learners[0].lastName` | `[0].students[0].lastName` | str | str | High |
| `courses[0].courseName` | `[0].courseName` | str | str | High |

## Sample Data Structure

### Legacy Sample
```json
{
  "courses": [
    {
      "courseId": "IT1006_007271_1_1195_J02_01",
      "coursePk": "_203002_1",
      "courseName": "IT1006 - Aug 05 2019 to Oct 11 2019 - Section 01",
      "learners": [
        {
          "learnerPk": "_1028574_1",
          "employeeID": "2319736",
          "firstName": "Christopher",
          "lastName": "Milanese",
          "emailId": "CRMILANESE@GMAIL.EXAMPLE.COM",
          "droppedOutDate": "2019-07-31T12:05:04-05:00"
        },
        {
          "learnerPk": "_1101958_1",
          "employeeID": "2361170",
          "firstName": "Domani",
          "lastName": "Reid",
          "emailId": "DOMANI.REID@YAHOO.EXAMPLE.COM",
          "droppedOutDate": "2019-07-31T12:05:04-05:00"
        },
        {
          "learnerPk": "_1090637_1",
          "employeeID": "2356947",
          "firstName": "James",
          "lastName": "Hemsworth",
          "emailId": "JHEMSWORTH13316@OUTLOOK.EXAMPLE.COM",
          "droppedOutDate": "2019-07-31T12:05:04-05:00"
...
```

### SaaS Sample
```json
[
  {
    "courseName": "PHY310 - 10/27/2024 to 12/25/2025 - Section 03",
    "students": [
      {
        "firstName": "Vinnie",
        "lastName": "Runolfsdottir",
        "dropDate": "2025-02-11T09:06:42.767Z"
      },
      {
        "firstName": "Emilie",
        "lastName": "Wiegand",
        "dropDate": "2025-01-20T07:12:42.399Z"
      },
      {
        "firstName": "Rosie",
        "lastName": "O'Reilly",
        "dropDate": "2025-02-01T08:41:30.218Z"
      }
    ]
  },
  {
    "courseName": "ENG430 - 12/19/2024 to 6/15/2026 - Section 03",
    "students": [
      {
        "firstName": "Nils",
        "lastName": "Rempel",
        "dropDate": "2025-02-20T06:59:42.952Z"
      },
      {
        "firstName": "Shayne",
        "lastName": "Buckridge",
        "dropDate": "2025-02-28T00:57:56.814Z"
      },
      {
        "firstName": "Maida",
        "lastName": "Schuppe-Altenwerth",
        "dropDate": "2025-02-14T14:57:30.282Z"
      },
      {
        "firstName": "Mohamed"...
```

## Recommendations

1. **Review new fields**: 5 new fields have been added. Ensure consuming applications can handle these additions.
2. **Handle removed fields**: 11 fields are no longer available. Update consuming applications accordingly.
4. **Verify renames**: 3 potential field renames detected. Confirm these are intentional changes.
