# messages-course-message API Analysis
**Legacy vs SaaS Comparison**

## Executive Summary

- **2 new fields** added in SaaS
- **3 fields** removed from Legacy (missing in SaaS)

## Overview
| Metric | Legacy | SaaS | Change |
|--------|--------|------|--------|
| Total Fields | 7 | 6 | -1 |
| New Fields | - | 2 | +2 |
| Removed Fields | 3 | - | -3 |
| Common Fields | 4 | 4 | 0 |
| Type Changes | - | 0 | 0 |

## 🆕 New Fields Added in SaaS
These fields are present in SaaS but not in Legacy:

| Field Name | Type | Notes |
|------------|------|-------|
| `messageSummary[0].newPosts` | int | New functionality |
| `messageSummary[0].replies` | int | New functionality |

## ❌ Fields Removed from Legacy
These fields were present in Legacy but are missing in SaaS:

| Field Name | Type | Impact |
|------------|------|--------|
| `messageSummary[0].courseId` | str | Functionality removed/changed |
| `messageSummary[0].coursePk` | str | Functionality removed/changed |
| `messageSummary[0].unreadMessages` | int | Functionality removed/changed |

## Sample Data Structure

### Legacy Sample
```json
{
  "totalUnreadMessages": 3,
  "messageSummary": [
    {
      "unreadMessages": 1,
      "courseId": "TEST-FP6003_007576_1_1187_OEE_01",
      "coursePk": "_149936_1",
      "link": "https://dvsc.capella.edu/webapps/BBC-000-DeepLinks-BBLEARN/deeplink?landingpage=coursemessage&course_id=_149936_1",
      "courseName": "TEST-FP6003 - Fall 2018 - Section 01"
    },
    {
      "unreadMessages": 1,
      "courseId": "TEST-FP6003_007576_1_1191_OEE_01",
      "coursePk": "_169985_1",
      "link": "https://dvsc.capella.edu/webapps/BBC-000-DeepLinks-BBLEARN/deeplink?landingpage=coursemessage&course_id=_169985_1",
      "courseName": "TEST-FP6003 - Winter 2019 - Section 01"
    },
    {
      "unreadMessages": 1,
      "courseId": "TESTSUB1333_006294_1_1191_1_01",
      "coursePk": "_168536_1",
      "link": "https://dvsc.capella.edu/webapps/BBC-000-DeepLinks-BBLEARN/deeplink?landingpage=coursemessage&course_id=_168536_1",
      "courseName": "TESTSUB1333 - Jan 07 2019 to Apr 07 2019 - Secti...
```

### SaaS Sample
```json
{
  "totalUnreadMessages": 5,
  "messageSummary": [
    {
      "newPosts": 0,
      "replies": 7,
      "link": "https://devcanvas.strayer.edu/courses/64477/discussion_topics/79357",
      "courseName": "Outdoors 159"
    },
    {
      "newPosts": 5,
      "replies": 7,
      "link": "https://devcanvas.strayer.edu/courses/23794/discussion_topics/29288",
      "courseName": "Clothing 295"
    },
    {
      "newPosts": 0,
      "replies": 10,
      "link": "https://devcanvas.strayer.edu/courses/44927/discussion_topics/94176",
      "courseName": "Movies 258"
    }
  ]
}
```

## Recommendations

1. **Review new fields**: 2 new fields have been added. Ensure consuming applications can handle these additions.
2. **Handle removed fields**: 3 fields are no longer available. Update consuming applications accordingly.
