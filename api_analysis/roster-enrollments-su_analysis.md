# roster-enrollments-su API Analysis
**Legacy vs SaaS Comparison**

## Executive Summary

- **50 new fields** added in SaaS
- **21 fields** removed from Legacy (missing in SaaS)
- **9 potential field renames** detected
- **6 fields** have type changes

## Overview
| Metric | Legacy | SaaS | Change |
|--------|--------|------|--------|
| Total Fields | 46 | 75 | +29 |
| New Fields | - | 50 | +50 |
| Removed Fields | 21 | - | -21 |
| Common Fields | 25 | 25 | 0 |
| Type Changes | - | 6 | 6 |

## 🆕 New Fields Added in SaaS
These fields are present in SaaS but not in Legacy:

| Field Name | Type | Notes |
|------------|------|-------|
| `[0].activeExtension` | int | New functionality |
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
| `[0].hasMilestones` | bool | New functionality |
| `[0].isActiveCourse` | bool | New functionality |
| `[0].isCourseStarted` | bool | New functionality |
| `[0].isJWMI` | bool | New functionality |
| `[0].lastAssessmentDt` | NoneType | New functionality |
| `[0].lastEngDiff` | int | New functionality |
| `[0].lastOutreachDt` | NoneType | New functionality |
| `[0].learnerId` | str | New functionality |
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
| `[0].priorityScore` | float | New functionality |
| `[0].regBlocker` | bool | New functionality |
| `[0].retake` | str | New functionality |
| `[0].startDt` | str | New functionality |
| `[0].studentHash` | str | New functionality |
| `[0].submittedAssignments` | NoneType | New functionality |
| `[0].suppressEngFlag` | NoneType | New functionality |
| `[0].tags[0].tagId` | int | New functionality |
| `[0].tags[0].tagName` | str | New functionality |
| `[0].totalAssignments` | NoneType | New functionality |
| `[0].userName` | str | New functionality |
| `[0].visiting` | str | New functionality |
| `[0].weeksInMilestone` | NoneType | New functionality |

## ❌ Fields Removed from Legacy
These fields were present in Legacy but are missing in SaaS:

| Field Name | Type | Impact |
|------------|------|--------|
| `[0].HASH` | str | Functionality removed/changed |
| `[0].advisorName` | str | Functionality removed/changed |
| `[0].coursePkId` | str | Functionality removed/changed |
| `[0].courseRoom` | str | Functionality removed/changed |
| `[0].deanEmail` | str | Functionality removed/changed |
| `[0].deanName` | str | Functionality removed/changed |
| `[0].deanPhone` | str | Functionality removed/changed |
| `[0].emailAddress` | str | Functionality removed/changed |
| `[0].employeeId` | str | Functionality removed/changed |
| `[0].endDate` | str | Functionality removed/changed |
| `[0].enrollmentDate` | str | Functionality removed/changed |
| `[0].fullName` | str | Functionality removed/changed |
| `[0].isCanvas` | bool | Functionality removed/changed |
| `[0].lastOutreachDate` | str | Functionality removed/changed |
| `[0].longCourseId` | str | Functionality removed/changed |
| `[0].mobileNumber` | str | Functionality removed/changed |
| `[0].overDue50Count` | int | Functionality removed/changed |
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
| `[0].dropDt` | NoneType | str | ⚠️ Breaking change |
| `[0].letterGrade` | NoneType | str | ⚠️ Breaking change |
| `[0].totalPoints` | NoneType | str | ⚠️ Breaking change |
| `[0].daysToDrop` | NoneType | int | ⚠️ Breaking change |

## 🏷️ Potential Field Renames
These appear to be renamed fields (similar names/types):

| Legacy Field | SaaS Field | Legacy Type | SaaS Type | Confidence |
|--------------|------------|-------------|-----------|------------|
| `[0].deanEmail` | `[0].email` | str | str | High |
| `[0].overDueCount` | `[0].overdueCount` | int | int | High |
| `[0].phone[0].type` | `[0].phoneType` | str | str | High |
| `[0].startDate` | `[0].courseStartDate` | str | NoneType | Medium |
| `[0].coursePkId` | `[0].coursePk` | str | int | Medium |
| `[0].HASH` | `[0].studentHash` | str | str | High |
| `[0].emailAddress` | `[0].email` | str | str | High |
| `[0].advisorName` | `[0].advisor` | str | str | High |
| `[0].overDue50Count` | `[0].overdue50Count` | int | int | High |

## Sample Data Structure

### Legacy Sample
```json
[
  {
    "firstName": "Jasmine",
    "lastName": "Snoddy",
    "fullName": "Jasmine Snoddy",
    "emailAddress": "jasmine.snoddy303@nonprod.strayer.edu",
    "employeeId": "200029946",
    "HASH": "RURtcFhUN2xqWHVmRHFaSm5reHZTZz09Ojoa+99fej6F7grcQ9yF4i2P",
    "city": "Hyattsville",
    "state": "MD",
    "phone": [
      {
        "number": "240/758-6431",
        "type": "Cell"
      }
    ],
    "mobileNumber": "+12407586431",
    "courseName": "BUS505-004-1242",
    "longCourseId": "BUS505004VA016-1242-001",
    "coursePkId": "6501",
    "startDate": "2024-01-02T00:00:00+00:00",
    "endDate": "2024-03-18T00:00:00+00:00",
    "advisorName": "Charlene Avery-Ford",
    "advisorEmail": "charlene.averyford@nonprod.strayer.edu",
    "advisorPhone": "844/727-4357",
    "deanName": "Camilla Craig",
    "deanEmail": "camilla.craig@nonprod.strayer.edu",
    "deanPhone": "540/846-8679",
    "lastOutreachDate": "2024-03-15T13:57:32+00:00",
    "outreachCount": 11,
    "tags": [],
    "enroll...
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

1. **Review new fields**: 50 new fields have been added. Ensure consuming applications can handle these additions.
2. **Handle removed fields**: 21 fields are no longer available. Update consuming applications accordingly.
3. **Address type changes**: 6 fields have changed types. This may require data parsing updates.
4. **Verify renames**: 9 potential field renames detected. Confirm these are intentional changes.
