# instructor-config API Analysis
**Legacy vs SaaS Comparison**

## Executive Summary

- **150 new fields** added in SaaS
- **1 fields** removed from Legacy (missing in SaaS)

## Overview
| Metric | Legacy | SaaS | Change |
|--------|--------|------|--------|
| Total Fields | 1 | 150 | +149 |
| New Fields | - | 150 | +150 |
| Removed Fields | 1 | - | -1 |
| Common Fields | 0 | 0 | 0 |
| Type Changes | - | 0 | 0 |

## 🆕 New Fields Added in SaaS
These fields are present in SaaS but not in Legacy:

| Field Name | Type | Notes |
|------------|------|-------|
| `generalProperties` | dict | New functionality |
| `generalProperties.adaAlertText` | dict | New functionality |
| `generalProperties.adaAlertText.addExtensionForm` | bool | New functionality |
| `generalProperties.adaAlertText.overviewTab` | bool | New functionality |
| `generalProperties.adaEmail` | str | New functionality |
| `generalProperties.createCaseUrl` | str | New functionality |
| `generalProperties.emailTrainingLink` | str | New functionality |
| `generalProperties.exportCsv` | bool | New functionality |
| `generalProperties.showLetterGrade` | bool | New functionality |
| `generalProperties.smsTrainingLink` | str | New functionality |
| `generalProperties.terms` | dict | New functionality |
| `generalProperties.terms.accommodation` | str | New functionality |
| `generalProperties.terms.accommodationAbv` | str | New functionality |
| `generalProperties.terms.student` | str | New functionality |
| `generalProperties.timezone` | str | New functionality |
| `generalProperties.timezoneIdentifier` | str | New functionality |
| `generalProperties.trainingLink` | str | New functionality |
| `nav` | list | New functionality |
| `nav[0].conditional` | str | New functionality |
| `nav[0].count` | NoneType | New functionality |
| `nav[0].cssClass` | NoneType | New functionality |
| `nav[0].link` | NoneType | New functionality |
| `nav[0].name` | str | New functionality |
| `nav[0].page` | list | New functionality |
| `nav[0].page[0].name` | str | New functionality |
| `nav[0].page[0].route` | str | New functionality |
| `nav[0].title` | NoneType | New functionality |
| `outreachCategories` | list | New functionality |
| `outreachCategories[0].category` | str | New functionality |
| `outreachCategories[0].categoryType` | str | New functionality |
| `outreachCategories[0].id` | int | New functionality |
| `outreachTypes` | list | New functionality |
| `outreachTypes[0].id` | int | New functionality |
| `outreachTypes[0].name` | str | New functionality |
| `placeHolders` | dict | New functionality |
| `placeHolders.email` | list | New functionality |
| `placeHolders.sms` | list | New functionality |
| `tableColumns` | dict | New functionality |
| `tableColumns.ayi` | list | New functionality |
| `tableColumns.ayi[0].columnName` | str | New functionality |
| `tableColumns.ayi[0].default` | int | New functionality |
| `tableColumns.ayi[0].filterBy` | bool | New functionality |
| `tableColumns.ayi[0].mobile` | bool | New functionality |
| `tableColumns.ayi[0].propName` | str | New functionality |
| `tableColumns.ayi[0].show` | bool | New functionality |
| `tableColumns.ayi[0].sortable` | bool | New functionality |
| `tableColumns.ayi[0].type` | str | New functionality |
| `tableColumns.courseActivity` | list | New functionality |
| `tableColumns.courseActivity[0].mobile` | bool | New functionality |
| `tableColumns.courseActivity[0].propName` | str | New functionality |
| `tableColumns.courseActivity[0].selectAll` | bool | New functionality |
| `tableColumns.courseActivity[0].show` | bool | New functionality |
| `tableColumns.courseActivity[0].sortable` | bool | New functionality |
| `tableColumns.courseActivity[0].type` | str | New functionality |
| `tableColumns.courseRoster` | list | New functionality |
| `tableColumns.courseRoster[0].batchId` | str | New functionality |
| `tableColumns.courseRoster[0].mobile` | bool | New functionality |
| `tableColumns.courseRoster[0].propName` | str | New functionality |
| `tableColumns.courseRoster[0].selectAll` | bool | New functionality |
| `tableColumns.courseRoster[0].show` | bool | New functionality |
| `tableColumns.courseRoster[0].sortable` | bool | New functionality |
| `tableColumns.courseRoster[0].type` | str | New functionality |
| `tableColumns.discussions` | list | New functionality |
| `tableColumns.discussions[0].columnName` | str | New functionality |
| `tableColumns.discussions[0].filterBy` | bool | New functionality |
| `tableColumns.discussions[0].mobile` | bool | New functionality |
| `tableColumns.discussions[0].propName` | str | New functionality |
| `tableColumns.discussions[0].show` | bool | New functionality |
| `tableColumns.discussions[0].sortable` | bool | New functionality |
| `tableColumns.discussions[0].type` | str | New functionality |
| `tableColumns.dropped` | list | New functionality |
| `tableColumns.dropped[0].columnName` | str | New functionality |
| `tableColumns.dropped[0].mobile` | bool | New functionality |
| `tableColumns.dropped[0].propName` | str | New functionality |
| `tableColumns.dropped[0].show` | bool | New functionality |
| `tableColumns.dropped[0].sortable` | bool | New functionality |
| `tableColumns.dropped[0].type` | str | New functionality |
| `tableColumns.needsGrading` | list | New functionality |
| `tableColumns.needsGrading[0].columnName` | str | New functionality |
| `tableColumns.needsGrading[0].filterBy` | bool | New functionality |
| `tableColumns.needsGrading[0].mobile` | bool | New functionality |
| `tableColumns.needsGrading[0].propName` | str | New functionality |
| `tableColumns.needsGrading[0].show` | bool | New functionality |
| `tableColumns.needsGrading[0].sortable` | bool | New functionality |
| `tableColumns.needsGrading[0].type` | str | New functionality |
| `tableColumns.pilotUsers` | list | New functionality |
| `tableColumns.pilotUsers[0].columnName` | str | New functionality |
| `tableColumns.pilotUsers[0].mobile` | bool | New functionality |
| `tableColumns.pilotUsers[0].propName` | str | New functionality |
| `tableColumns.pilotUsers[0].show` | bool | New functionality |
| `tableColumns.pilotUsers[0].sortable` | bool | New functionality |
| `tableColumns.pilotUsers[0].type` | str | New functionality |
| `tableColumns.search` | list | New functionality |
| `tableColumns.search[0].columnName` | str | New functionality |
| `tableColumns.search[0].default` | int | New functionality |
| `tableColumns.search[0].filterBy` | bool | New functionality |
| `tableColumns.search[0].mobile` | bool | New functionality |
| `tableColumns.search[0].propName` | str | New functionality |
| `tableColumns.search[0].show` | bool | New functionality |
| `tableColumns.search[0].sortable` | bool | New functionality |
| `tableColumns.search[0].type` | str | New functionality |
| `tableColumns.submitGrades` | list | New functionality |
| `tableColumns.submitGrades[0].columnName` | str | New functionality |
| `tableColumns.submitGrades[0].default` | bool | New functionality |
| `tableColumns.submitGrades[0].mobile` | bool | New functionality |
| `tableColumns.submitGrades[0].propName` | str | New functionality |
| `tableColumns.submitGrades[0].show` | bool | New functionality |
| `tableColumns.submitGrades[0].sortable` | bool | New functionality |
| `tableColumns.submitGrades[0].type` | str | New functionality |
| `tableColumns.templates` | list | New functionality |
| `tableColumns.templates[0].columnName` | str | New functionality |
| `tableColumns.templates[0].default` | int | New functionality |
| `tableColumns.templates[0].isToggle` | bool | New functionality |
| `tableColumns.templates[0].mobile` | bool | New functionality |
| `tableColumns.templates[0].propName` | str | New functionality |
| `tableColumns.templates[0].show` | bool | New functionality |
| `tableColumns.templates[0].sortable` | bool | New functionality |
| `tableColumns.templates[0].type` | str | New functionality |
| `userFeatures` | dict | New functionality |
| `userFeatures.alerts` | bool | New functionality |
| `userFeatures.allAttemptsValid` | bool | New functionality |
| `userFeatures.askYourProfessor` | bool | New functionality |
| `userFeatures.compass` | bool | New functionality |
| `userFeatures.courseActivityMenu` | bool | New functionality |
| `userFeatures.courseRoster` | bool | New functionality |
| `userFeatures.discussions` | bool | New functionality |
| `userFeatures.dropped` | bool | New functionality |
| `userFeatures.email` | dict | New functionality |
| `userFeatures.email.read` | bool | New functionality |
| `userFeatures.email.write` | bool | New functionality |
| `userFeatures.exportGradebook` | bool | New functionality |
| `userFeatures.extensions` | dict | New functionality |
| `userFeatures.extensions.read` | bool | New functionality |
| `userFeatures.extensions.write` | bool | New functionality |
| `userFeatures.facHelp` | bool | New functionality |
| `userFeatures.gradebook` | bool | New functionality |
| `userFeatures.gradebookDetails` | bool | New functionality |
| `userFeatures.gradebookInProgress` | bool | New functionality |
| `userFeatures.gradebookScore` | bool | New functionality |
| `userFeatures.grading` | bool | New functionality |
| `userFeatures.messaging` | bool | New functionality |
| `userFeatures.needsGrading` | bool | New functionality |
| `userFeatures.notificationContent` | bool | New functionality |
| `userFeatures.notifications` | bool | New functionality |
| `userFeatures.outreachTab` | bool | New functionality |
| `userFeatures.roster` | bool | New functionality |
| `userFeatures.submitGrades` | bool | New functionality |
| `userFeatures.textMessage` | dict | New functionality |
| `userFeatures.textMessage.read` | bool | New functionality |
| `userFeatures.textMessage.write` | bool | New functionality |

## ❌ Fields Removed from Legacy
These fields were present in Legacy but are missing in SaaS:

| Field Name | Type | Impact |
|------------|------|--------|
| `Missing` | str | Functionality removed/changed |

## Sample Data Structure

### Legacy Sample
```json
{
  "Missing": "No api info available "
}
```

### SaaS Sample
```json
{
  "nav": [
    {
      "name": "Roster",
      "conditional": "hasCourses",
      "count": null,
      "link": null,
      "title": null,
      "cssClass": null,
      "page": [
        {
          "name": "Course Roster",
          "route": "/roster/course-roster"
        },
        {
          "name": "Dropped",
          "route": "/roster/dropped"
        }
      ]
    },
    {
      "name": "Messaging",
      "conditional": "hasCourses",
      "count": "messagesCountTotal",
      "link": null,
      "title": null,
      "cssClass": null,
      "page": [
        {
          "name": "Text Messages",
          "count": "smsCounter",
          "route": "/messages/text-messages",
          "conditional": "isPI"
        },
        {
          "name": "Ask Your Professor",
          "count": "ayiCounter",
          "route": "/messages/ask-your-instructor"
        }
      ]
    },
    {
      "name": "Grading",
      "conditional": "hasGpCourses",
      "count": "gradingTotal",
      "li...
```

## Recommendations

1. **Review new fields**: 150 new fields have been added. Ensure consuming applications can handle these additions.
2. **Handle removed fields**: 1 fields are no longer available. Update consuming applications accordingly.
