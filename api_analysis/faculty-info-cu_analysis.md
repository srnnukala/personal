# faculty-info-cu API Analysis
**Legacy vs SaaS Comparison**

## Executive Summary

- **2 new fields** added in SaaS
- **1 fields** removed from Legacy (missing in SaaS)

## Overview
| Metric | Legacy | SaaS | Change |
|--------|--------|------|--------|
| Total Fields | 13 | 14 | +1 |
| New Fields | - | 2 | +2 |
| Removed Fields | 1 | - | -1 |
| Common Fields | 12 | 12 | 0 |
| Type Changes | - | 0 | 0 |

## 🆕 New Fields Added in SaaS
These fields are present in SaaS but not in Legacy:

| Field Name | Type | Notes |
|------------|------|-------|
| `discussionCount` | int | New functionality |
| `needsGrading` | int | New functionality |

## ❌ Fields Removed from Legacy
These fields were present in Legacy but are missing in SaaS:

| Field Name | Type | Impact |
|------------|------|--------|
| `courseActivity` | bool | Functionality removed/changed |

## Sample Data Structure

### Legacy Sample
```json
{
  "loginId": "MAHMOUD.ELHARAZI",
  "firstName": "Mahmoud",
  "lastName": "Elharazi",
  "email": "mahmoud.elharazi@nonprod.strategiced.com",
  "courseActivity": true,
  "globalInbox": [],
  "courses": [
    {
      "courseId": "ACC100486VA001-1256-001",
      "role": "PI"
    },
    {
      "courseId": "ACC556105VA001-1256-001",
      "role": "PI"
    }
  ],
  "allCourses": [
    {
      "courses": "COURSE_1256_S08",
      "strm": "1256",
      "sessionCode": "S08"
    },
    {
      "courses": "COURSE_1256_S07",
      "strm": "1256",
      "sessionCode": "S07"
    },
    {
      "courses": "COURSE_1256_001",
      "strm": "1256",
      "sessionCode": "001"
    },
    {
      "courses": "COURSE_1256_MN2",
      "strm": "1256",
      "sessionCode": "MN2"
    }
  ]
}
```

### SaaS Sample
```json
{
  "loginId": "Nayeli.GOODWIN",
  "firstName": "Nayeli",
  "lastName": "Goodwin",
  "email": "Micheal_Ferry@yahoo.com",
  "globalInbox": [
    "Earlene.Buckridge37@hotmail.com",
    "Walton_Walter94@yahoo.com"
  ],
  "courses": [
    {
      "courseId": "POL430_972897_02",
      "role": "PI"
    },
    {
      "courseId": "STA280_753182_02",
      "role": "TA"
    },
    {
      "courseId": "DAN960_343418_03",
      "role": "TA"
    },
    {
      "courseId": "STA280_404578_04",
      "role": "PI"
    },
    {
      "courseId": "POL430_406732_03",
      "role": "PI"
    },
    {
      "courseId": "STA280_139796_03",
      "role": "PI"
    },
    {
      "courseId": "POL430_972897_02",
      "role": "PI"
    },
    {
      "courseId": "DAN410_534904_04",
      "role": "PI"
    },
    {
      "courseId": "POL430_406732_03",
      "role": "PI"
    },
    {
      "courseId": "POL430_406732_03",
      "role": "PI"
    },
    {
      "courseId": "STA280_139796_03",
      "role": "PI"
    },...
```

## Recommendations

1. **Review new fields**: 2 new fields have been added. Ensure consuming applications can handle these additions.
2. **Handle removed fields**: 1 fields are no longer available. Update consuming applications accordingly.
