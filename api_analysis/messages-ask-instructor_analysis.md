# messages-ask-instructor API Analysis
**Legacy vs SaaS Comparison**

## Executive Summary

- **2 fields** removed from Legacy (missing in SaaS)

## Overview
| Metric | Legacy | SaaS | Change |
|--------|--------|------|--------|
| Total Fields | 8 | 6 | -2 |
| New Fields | - | 0 | +0 |
| Removed Fields | 2 | - | -2 |
| Common Fields | 6 | 6 | 0 |
| Type Changes | - | 0 | 0 |

## ❌ Fields Removed from Legacy
These fields were present in Legacy but are missing in SaaS:

| Field Name | Type | Impact |
|------------|------|--------|
| `discussionSummary[0].courseId` | str | Functionality removed/changed |
| `discussionSummary[0].coursePk` | str | Functionality removed/changed |

## Sample Data Structure

### Legacy Sample
```json
{
  "totalPosts": 2,
  "discussionSummary": [
    {
      "newPosts": 0,
      "replies": 2,
      "courseId": "BUS407030VA016-1196-001",
      "coursePk": "_244395_1",
      "link": "https://dvsu.strayer.edu/webapps/discussionboard/do/forum?action=list_threads&course_id=_244395_1&nav=discussion_board_entry&conf_id=_210712_1&forum_id=_2908587_1",
      "courseName": "Training and Development"
    }
  ]
}
```

### SaaS Sample
```json
{
  "totalPosts": 10,
  "discussionSummary": [
    {
      "newPosts": 5,
      "replies": 4,
      "link": "https://devcanvas.strayer.edu/courses/96462/discussion_topics/32017",
      "courseName": "Jewelry 394"
    },
    {
      "newPosts": 0,
      "replies": 10,
      "link": "https://devcanvas.strayer.edu/courses/14694/discussion_topics/46453",
      "courseName": "Toys 498"
    },
    {
      "newPosts": 4,
      "replies": 2,
      "link": "https://devcanvas.strayer.edu/courses/14029/discussion_topics/71889",
      "courseName": "Industrial 284"
    },
    {
      "newPosts": 1,
      "replies": 2,
      "link": "https://devcanvas.strayer.edu/courses/78657/discussion_topics/17196",
      "courseName": "Outdoors 270"
    }
  ]
}
```

## Recommendations

2. **Handle removed fields**: 2 fields are no longer available. Update consuming applications accordingly.
