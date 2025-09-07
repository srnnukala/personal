# roster-enrollments-flexpath API Analysis
**Legacy vs SaaS Comparison**

## Executive Summary

- **52 new fields** added in SaaS
- **18 fields** removed from Legacy (missing in SaaS)
- **7 potential field renames** detected
- **4 fields** have type changes

## Overview
| Metric | Legacy | SaaS | Change |
|--------|--------|------|--------|
| Total Fields | 41 | 75 | +34 |
| New Fields | - | 52 | +52 |
| Removed Fields | 18 | - | -18 |
| Common Fields | 23 | 23 | 0 |
| Type Changes | - | 4 | 4 |

## 🆕 New Fields Added in SaaS
These fields are present in SaaS but not in Legacy:

| Field Name | Type | Notes |
|------------|------|-------|
| `[0].activeExtension` | int | New functionality |
| `[0].activityScore` | float | New functionality |
| `[0].activityScoreBand` | int | New functionality |
| `[0].activityScoreTrend` | int | New functionality |
| `[0].ada` | str | New functionality |
| `[0].advisor` | str | New functionality |
| `[0].censusDt` | NoneType | New functionality |
| `[0].courseCategory` | str | New functionality |
| `[0].coursePk` | int | New functionality |
| `[0].courseSisId` | str | New functionality |
| `[0].courseStartDate` | NoneType | New functionality |
| `[0].csEngDt` | str | New functionality |
| `[0].currentMilestone` | NoneType | New functionality |
| `[0].email` | str | New functionality |
| `[0].endDt` | str | New functionality |
| `[0].enrolledDays` | NoneType | New functionality |
| `[0].enrollmentDt` | str | New functionality |
| `[0].facultyId` | str | New functionality |
| `[0].firstTerm` | str | New functionality |
| `[0].futureDropDt` | str | New functionality |
| `[0].gradeFinal` | NoneType | New functionality |
| `[0].gradeMidterm` | str | New functionality |
| `[0].isActiveCourse` | bool | New functionality |
| `[0].isCourseStarted` | bool | New functionality |
| `[0].isJWMI` | bool | New functionality |
| `[0].lastAssessmentDt` | NoneType | New functionality |
| `[0].lastEngDiff` | int | New functionality |
| `[0].lastOutreachDt` | NoneType | New functionality |
| `[0].learnerId` | str | New functionality |
| `[0].letterGrade` | str | New functionality |
| `[0].nsoNotComplete` | str | New functionality |
| `[0].nsoOutreachDt` | NoneType | New functionality |
| `[0].numDays` | int | New functionality |
| `[0].oeeInd` | NoneType | New functionality |
| `[0].outreachCountToday` | int | New functionality |
| `[0].overdue50Count` | int | New functionality |
| `[0].overdueCount` | int | New functionality |
| `[0].phoneType` | str | New functionality |
| `[0].priorityPilotGroup` | NoneType | New functionality |
| `[0].priorityRiskLevel` | NoneType | New functionality |
| `[0].regBlocker` | bool | New functionality |
| `[0].retake` | str | New functionality |
| `[0].startDt` | str | New functionality |
| `[0].studentHash` | str | New functionality |
| `[0].submittedAssignments` | NoneType | New functionality |
| `[0].suppressEngFlag` | NoneType | New functionality |
| `[0].tags[0].tagId` | int | New functionality |
| `[0].tags[0].tagName` | str | New functionality |
| `[0].totalAssignments` | NoneType | New functionality |
| `[0].totalPoints` | str | New functionality |
| `[0].visiting` | str | New functionality |
| `[0].weeksInMilestone` | NoneType | New functionality |

## ❌ Fields Removed from Legacy
These fields were present in Legacy but are missing in SaaS:

| Field Name | Type | Impact |
|------------|------|--------|
| `[0].HASH` | str | Functionality removed/changed |
| `[0].advisorName` | str | Functionality removed/changed |
| `[0].coursePkId` | int | Functionality removed/changed |
| `[0].courseRoom` | NoneType | Functionality removed/changed |
| `[0].droppedOutDate` | NoneType | Functionality removed/changed |
| `[0].emailAddress` | str | Functionality removed/changed |
| `[0].employeeId` | str | Functionality removed/changed |
| `[0].endDate` | str | Functionality removed/changed |
| `[0].enrollmentDate` | str | Functionality removed/changed |
| `[0].fullName` | str | Functionality removed/changed |
| `[0].isCanvas` | bool | Functionality removed/changed |
| `[0].lastOutreachDate` | str | Functionality removed/changed |
| `[0].longCourseId` | str | Functionality removed/changed |
| `[0].mobileNumber` | str | Functionality removed/changed |
| `[0].overDueCount` | int | Functionality removed/changed |
| `[0].phone[0].number` | str | Functionality removed/changed |
| `[0].phone[0].type` | str | Functionality removed/changed |
| `[0].startDate` | str | Functionality removed/changed |

## 🔄 Fields with Type Changes
These fields exist in both but have different data types:

| Field Name | Legacy Type | SaaS Type | Impact |
|------------|-------------|-----------|--------|
| `[0].courseTextNumber` | str | NoneType | ⚠️ Breaking change |
| `[0].phone` | list | str | ⚠️ Breaking change |
| `[0].advisorEmail` | NoneType | str | ⚠️ Breaking change |
| `[0].priorityScore` | NoneType | float | ⚠️ Breaking change |

## 🏷️ Potential Field Renames
These appear to be renamed fields (similar names/types):

| Legacy Field | SaaS Field | Legacy Type | SaaS Type | Confidence |
|--------------|------------|-------------|-----------|------------|
| `[0].advisorName` | `[0].advisor` | str | str | High |
| `[0].startDate` | `[0].courseStartDate` | str | NoneType | Medium |
| `[0].coursePkId` | `[0].coursePk` | int | int | High |
| `[0].phone[0].type` | `[0].phoneType` | str | str | High |
| `[0].HASH` | `[0].studentHash` | str | str | High |
| `[0].overDueCount` | `[0].overdueCount` | int | int | High |
| `[0].emailAddress` | `[0].email` | str | str | High |

## Sample Data Structure

### Legacy Sample
```json
[
  {
    "firstName": "Kelly",
    "lastName": "Kemp",
    "fullName": "Kelly Kemp",
    "emailAddress": "kkemp84@gmail.example.com",
    "employeeId": "2425704",
    "userName": "KKEMP22",
    "HASH": "d3lDZlJTbUZXN1k5akhWKy9GQm5aQT09OjoP/w6FklZT20sdVBqBe/qk",
    "city": "Milford",
    "state": "CT",
    "phone": [
      {
        "number": "203/202-4859",
        "type": "CELL"
      }
    ],
    "mobileNumber": "+12032024859",
    "courseName": "BUS3007 - Jan 08 2024 to Mar 15 2024 - Section PI",
    "longCourseId": "BUS3007_006845_1_1241_1_PI",
    "coursePkId": 5176,
    "courseRoom": null,
    "startDate": "2024-01-08T00:00:00-06:00",
    "endDate": "2024-03-15T00:00:00-05:00",
    "droppedOutDate": null,
    "advisorName": "Chad Barthelemy",
    "advisorEmail": null,
    "advisorPhone": "855/482-2080",
    "tags": [],
    "enrollmentDate": "2/21/24",
    "hasMilestones": false,
    "isCanvas": true,
    "courseTextNumber": "+19665528366",
    "lastAcadEngDt": "",
    "lastOutr...
```

### SaaS Sample
```json
[
  {
    "firstName": "Guivenson",
    "studentHash": "A4DPe4KHFyXfAqRfOvkW/6n/uyCQ20ZPhzwQ55wcOYPOUiDPdYf0n8zuDThUwjWFO4CiCy01YmOuTAgkoWDJtw==::BWEYzoi8d9HC5vrNxhxMoA==",
    "lastName": "Lassegue",
    "email": "GLASSEGUE@nonprod.strategiced.com",
    "phone": "+13219995756",
    "phoneType": "Cell",
    "city": "Spotsylvania",
    "state": "VA",
    "courseSisId": "ACC100486VA001-1256-001",
    "coursePk": 21944,
    "courseName": "ACC100-486-1256",
    "facultyId": "56003",
    "learnerId": "200861687",
    "startDt": "2025-07-07T00:00:00Z",
    "courseStartDate": null,
    "endDt": "2025-09-22T00:00:00Z",
    "advisor": "Robin Laning",
    "advisorPhone": "+1 912 9212906",
    "advisorEmail": "robin.laning@nonprod.strategiced.com",
    "courseTextNumber": null,
    "role": "PI",
    "lastOutreachDt": null,
    "nsoOutreachDt": null,
    "outreachCount": 0,
    "activeExtension": 0,
    "systemTags": [],
    "tags": [
      {
        "tagId": 717,
        "tagName": "test tag"
   ...
```

## Recommendations

1. **Review new fields**: 52 new fields have been added. Ensure consuming applications can handle these additions.
2. **Handle removed fields**: 18 fields are no longer available. Update consuming applications accordingly.
3. **Address type changes**: 4 fields have changed types. This may require data parsing updates.
4. **Verify renames**: 7 potential field renames detected. Confirm these are intentional changes.
