# submit-grades-grade-details API Analysis
**Legacy vs SaaS Comparison**

## Executive Summary

- **7 new fields** added in SaaS
- **1 fields** removed from Legacy (missing in SaaS)

## Overview
| Metric | Legacy | SaaS | Change |
|--------|--------|------|--------|
| Total Fields | 1 | 7 | +6 |
| New Fields | - | 7 | +7 |
| Removed Fields | 1 | - | -1 |
| Common Fields | 0 | 0 | 0 |
| Type Changes | - | 0 | 0 |

## 🆕 New Fields Added in SaaS
These fields are present in SaaS but not in Legacy:

| Field Name | Type | Notes |
|------------|------|-------|
| `[0].courseSisId` | str | New functionality |
| `[0].final` | bool | New functionality |
| `[0].gradingScale` | list | New functionality |
| `[0].gradingScale[0].calculated_value` | int | New functionality |
| `[0].gradingScale[0].name` | str | New functionality |
| `[0].gradingScale[0].value` | float | New functionality |
| `[0].midterm` | bool | New functionality |

## ❌ Fields Removed from Legacy
These fields were present in Legacy but are missing in SaaS:

| Field Name | Type | Impact |
|------------|------|--------|
| `missing` | str | Functionality removed/changed |

## Sample Data Structure

### Legacy Sample
```json
{
  "missing": "No api response available"
}
```

### SaaS Sample
```json
[
  {
    "courseSisId": "POL430_972897_02",
    "gradingScale": [
      {
        "name": "A",
        "value": 0.9,
        "calculated_value": 90
      },
      {
        "name": "B",
        "value": 0.8,
        "calculated_value": 80
      },
      {
        "name": "C",
        "value": 0.7,
        "calculated_value": 70
      },
      {
        "name": "D",
        "value": 0.6,
        "calculated_value": 60
      },
      {
        "name": "F",
        "value": 0,
        "calculated_value": 0
      }
    ],
    "midterm": true,
    "final": true
  },
  {
    "courseSisId": "DAN410_460186_01",
    "gradingScale": [
      {
        "name": "A",
        "value": 0.9,
        "calculated_value": 90
      },
      {
        "name": "B",
        "value": 0.8,
        "calculated_value": 80
      },
      {
        "name": "C",
        "value": 0.7,
        "calculated_value": 70
      },
      {
        "name": "D",
        "value": 0.6,
        "calculated_value": 60
      },
  ...
```

## Recommendations

1. **Review new fields**: 7 new fields have been added. Ensure consuming applications can handle these additions.
2. **Handle removed fields**: 1 fields are no longer available. Update consuming applications accordingly.
