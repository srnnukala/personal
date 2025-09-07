# gradebook-assigments-all API Analysis
**Legacy vs SaaS Comparison**

## Executive Summary

- **16 new fields** added in SaaS
- **24 fields** removed from Legacy (missing in SaaS)
- **42 potential field renames** detected

## Overview
| Metric | Legacy | SaaS | Change |
|--------|--------|------|--------|
| Total Fields | 24 | 16 | -8 |
| New Fields | - | 16 | +16 |
| Removed Fields | 24 | - | -24 |
| Common Fields | 0 | 0 | 0 |
| Type Changes | - | 0 | 0 |

## 🆕 New Fields Added in SaaS
These fields are present in SaaS but not in Legacy:

| Field Name | Type | Notes |
|------------|------|-------|
| `ACC100` | dict | New functionality |
| `ACC100.assignments` | list | New functionality |
| `ACC100.assignments[0].assignmentId` | str | New functionality |
| `ACC100.assignments[0].assignmentTitle` | str | New functionality |
| `ACC100.assignments[0].dueDate` | str | New functionality |
| `ACC100.assignments[0].overdueCount` | int | New functionality |
| `ACC100.assignments[0].points` | int | New functionality |
| `ACC100.sectionCount` | int | New functionality |
| `ACC556` | dict | New functionality |
| `ACC556.assignments` | list | New functionality |
| `ACC556.assignments[0].assignmentId` | str | New functionality |
| `ACC556.assignments[0].assignmentTitle` | str | New functionality |
| `ACC556.assignments[0].dueDate` | str | New functionality |
| `ACC556.assignments[0].overdueCount` | int | New functionality |
| `ACC556.assignments[0].points` | int | New functionality |
| `ACC556.sectionCount` | int | New functionality |

## ❌ Fields Removed from Legacy
These fields were present in Legacy but are missing in SaaS:

| Field Name | Type | Impact |
|------------|------|--------|
| `BUS380` | dict | Functionality removed/changed |
| `BUS380.assignments` | list | Functionality removed/changed |
| `BUS380.assignments[0].assignmentId` | str | Functionality removed/changed |
| `BUS380.assignments[0].assignmentTitle` | str | Functionality removed/changed |
| `BUS380.assignments[0].dueDate` | str | Functionality removed/changed |
| `BUS380.assignments[0].overdueCount` | int | Functionality removed/changed |
| `BUS380.assignments[0].points` | int | Functionality removed/changed |
| `BUS380.sectionCount` | int | Functionality removed/changed |
| `BUS435` | dict | Functionality removed/changed |
| `BUS435.assignments` | list | Functionality removed/changed |
| `BUS435.assignments[0].assignmentId` | str | Functionality removed/changed |
| `BUS435.assignments[0].assignmentTitle` | str | Functionality removed/changed |
| `BUS435.assignments[0].dueDate` | str | Functionality removed/changed |
| `BUS435.assignments[0].overdueCount` | int | Functionality removed/changed |
| `BUS435.assignments[0].points` | int | Functionality removed/changed |
| `BUS435.sectionCount` | int | Functionality removed/changed |
| `BUS437` | dict | Functionality removed/changed |
| `BUS437.assignments` | list | Functionality removed/changed |
| `BUS437.assignments[0].assignmentId` | str | Functionality removed/changed |
| `BUS437.assignments[0].assignmentTitle` | str | Functionality removed/changed |
| `BUS437.assignments[0].dueDate` | str | Functionality removed/changed |
| `BUS437.assignments[0].overdueCount` | int | Functionality removed/changed |
| `BUS437.assignments[0].points` | int | Functionality removed/changed |
| `BUS437.sectionCount` | int | Functionality removed/changed |

## 🏷️ Potential Field Renames
These appear to be renamed fields (similar names/types):

| Legacy Field | SaaS Field | Legacy Type | SaaS Type | Confidence |
|--------------|------------|-------------|-----------|------------|
| `BUS437.assignments[0].dueDate` | `ACC100.assignments[0].dueDate` | str | str | High |
| `BUS437.assignments[0].dueDate` | `ACC556.assignments[0].dueDate` | str | str | High |
| `BUS437.assignments[0].points` | `ACC100.assignments[0].points` | int | int | High |
| `BUS437.assignments[0].points` | `ACC556.assignments[0].points` | int | int | High |
| `BUS437.sectionCount` | `ACC556.sectionCount` | int | int | High |
| `BUS437.sectionCount` | `ACC100.sectionCount` | int | int | High |
| `BUS380.assignments` | `ACC100.assignments` | list | list | High |
| `BUS380.assignments` | `ACC556.assignments` | list | list | High |
| `BUS435.assignments` | `ACC100.assignments` | list | list | High |
| `BUS435.assignments` | `ACC556.assignments` | list | list | High |
| `BUS380.assignments[0].assignmentId` | `ACC100.assignments[0].assignmentId` | str | str | High |
| `BUS380.assignments[0].assignmentId` | `ACC556.assignments[0].assignmentId` | str | str | High |
| `BUS380.assignments[0].assignmentTitle` | `ACC100.assignments[0].assignmentTitle` | str | str | High |
| `BUS380.assignments[0].assignmentTitle` | `ACC556.assignments[0].assignmentTitle` | str | str | High |
| `BUS437.assignments[0].overdueCount` | `ACC556.assignments[0].overdueCount` | int | int | High |
| `BUS437.assignments[0].overdueCount` | `ACC100.assignments[0].overdueCount` | int | int | High |
| `BUS380.assignments[0].points` | `ACC100.assignments[0].points` | int | int | High |
| `BUS380.assignments[0].points` | `ACC556.assignments[0].points` | int | int | High |
| `BUS437.assignments[0].assignmentTitle` | `ACC100.assignments[0].assignmentTitle` | str | str | High |
| `BUS437.assignments[0].assignmentTitle` | `ACC556.assignments[0].assignmentTitle` | str | str | High |
| `BUS435.sectionCount` | `ACC556.sectionCount` | int | int | High |
| `BUS435.sectionCount` | `ACC100.sectionCount` | int | int | High |
| `BUS435.assignments[0].assignmentId` | `ACC100.assignments[0].assignmentId` | str | str | High |
| `BUS435.assignments[0].assignmentId` | `ACC556.assignments[0].assignmentId` | str | str | High |
| `BUS435.assignments[0].dueDate` | `ACC100.assignments[0].dueDate` | str | str | High |
| `BUS435.assignments[0].dueDate` | `ACC556.assignments[0].dueDate` | str | str | High |
| `BUS380.assignments[0].overdueCount` | `ACC556.assignments[0].overdueCount` | int | int | High |
| `BUS380.assignments[0].overdueCount` | `ACC100.assignments[0].overdueCount` | int | int | High |
| `BUS437.assignments` | `ACC100.assignments` | list | list | High |
| `BUS437.assignments` | `ACC556.assignments` | list | list | High |
| `BUS380.assignments[0].dueDate` | `ACC100.assignments[0].dueDate` | str | str | High |
| `BUS380.assignments[0].dueDate` | `ACC556.assignments[0].dueDate` | str | str | High |
| `BUS435.assignments[0].assignmentTitle` | `ACC100.assignments[0].assignmentTitle` | str | str | High |
| `BUS435.assignments[0].assignmentTitle` | `ACC556.assignments[0].assignmentTitle` | str | str | High |
| `BUS435.assignments[0].points` | `ACC100.assignments[0].points` | int | int | High |
| `BUS435.assignments[0].points` | `ACC556.assignments[0].points` | int | int | High |
| `BUS435.assignments[0].overdueCount` | `ACC556.assignments[0].overdueCount` | int | int | High |
| `BUS435.assignments[0].overdueCount` | `ACC100.assignments[0].overdueCount` | int | int | High |
| `BUS380.sectionCount` | `ACC556.sectionCount` | int | int | High |
| `BUS380.sectionCount` | `ACC100.sectionCount` | int | int | High |
| `BUS437.assignments[0].assignmentId` | `ACC100.assignments[0].assignmentId` | str | str | High |
| `BUS437.assignments[0].assignmentId` | `ACC556.assignments[0].assignmentId` | str | str | High |

## Sample Data Structure

### Legacy Sample
```json
{
  "BUS435": {
    "sectionCount": 2,
    "assignments": [
      {
        "assignmentId": "V2VlayAxMSBEaXNjdXNzaW9ue3NwbGl0fTIwMjEtMDYtMjEgMDk6MDA6MDB7c3BsaXR9QlVTNDM1",
        "assignmentTitle": "Week 11 Discussion",
        "dueDate": "2021-06-21T09:00:00+00:00",
        "points": 30,
        "overdueCount": 38
      },
      {
        "assignmentId": "V2VlayAxMCBBc3NpZ25tZW50IC0gTGVhZGVyc2hpcCBhbmQgTGVhZGVyc2hpcCBEZXZlbG9wbWVudHtzcGxpdH0yMDIxLTA2LTE0IDA5OjAwOjAwe3NwbGl0fUJVUzQzNQ==",
        "assignmentTitle": "Week 10 Assignment - Leadership and Leadership Development",
        "dueDate": "2021-06-14T09:00:00+00:00",
        "points": 185,
        "overdueCount": 38
      },
      {
        "assignmentId": "V2VlayAxMCBEaXNjdXNzaW9ue3NwbGl0fTIwMjEtMDYtMTQgMDk6MDA6MDB7c3BsaXR9QlVTNDM1",
        "assignmentTitle": "Week 10 Discussion",
        "dueDate": "2021-06-14T09:00:00+00:00",
        "points": 30,
        "overdueCount": 38
      },
      {
        "assignmentId": "V2VlayA5I...
```

### SaaS Sample
```json
{
  "ACC100": {
    "sectionCount": 1,
    "assignments": [
      {
        "assignmentId": "V2VlayAxIERpc2N1c3Npb24gLSBBY2NvdW50aW5nIElzIEFsbCBBcm91bmQgVXM=",
        "assignmentTitle": "Week 1 Discussion - Accounting Is All Around Us",
        "dueDate": "2025-07-14T13:00:00Z",
        "points": 20,
        "overdueCount": 0
      },
      {
        "assignmentId": "V2VlayAxIC0gSG9tZXdvcms6IENoYXB0ZXIgMQ==",
        "assignmentTitle": "Week 1 - Homework: Chapter 1",
        "dueDate": "2025-07-14T13:00:00Z",
        "points": 35,
        "overdueCount": 0
      },
      {
        "assignmentId": "V2VlayAyIC0gSG9tZXdvcms6IENoYXB0ZXIgMg==",
        "assignmentTitle": "Week 2 - Homework: Chapter 2",
        "dueDate": "2025-07-21T13:00:00Z",
        "points": 35,
        "overdueCount": 4
      },
      {
        "assignmentId": "V2VlayAyIERpc2N1c3Npb24gLSBTdHJhdGVnaWVzIGZvciBTdWNjZXNz",
        "assignmentTitle": "Week 2 Discussion - Strategies for Success",
        "dueDate": "2025-07...
```

## Recommendations

1. **Review new fields**: 16 new fields have been added. Ensure consuming applications can handle these additions.
2. **Handle removed fields**: 24 fields are no longer available. Update consuming applications accordingly.
4. **Verify renames**: 42 potential field renames detected. Confirm these are intentional changes.
