# Legacy to SAAS API Migration Analysis Report

## Executive Summary

**Analysis Date**: September 05, 2025

### 🚨 Critical Findings

This comprehensive analysis of **21 API endpoints** reveals significant differences between Legacy and SAAS implementations that require immediate attention:

- **20/21 APIs** have fields missing in SAAS responses
- **11 APIs** have structural response format changes
- **257 unique fields** are present in Legacy but missing in SAAS
- **399 unique fields** are new in SAAS responses
- **436 potential field mappings** identified for investigation

### 🎯 Impact Assessment

The migration from Legacy to SAAS has introduced substantial changes that could impact:
- **Frontend applications** expecting specific field names or structures
- **Integration systems** relying on complete data sets
- **Business logic** dependent on wrapper fields (code, status, message)
- **Error handling** mechanisms expecting wrapped responses

### ⚠️ Immediate Action Required

Fields missing in SAAS could cause application failures. See detailed analysis below for specific recommendations per API.

---
## 📊 Summary Statistics

| Metric | Count | Percentage |
|--------|-------|------------|
| Total APIs Analyzed | 21 | 100% |
| APIs with Missing Fields | 20 | 95.2% |
| APIs with New Fields | 19 | 90.5% |
| APIs with Structural Changes | 11 | 52.4% |
| Total Unique Missing Fields | 257 | - |
| Total Unique New Fields | 399 | - |
| Potential Field Mappings | 436 | - |

---
## 🔥 Critical Issues Requiring Immediate Attention

### High-Impact APIs (Most Missing Fields)

- **kaltura-video-my-media**: 72 fields missing in SAAS
- **roster-enrollments-su**: 50 fields missing in SAAS
- **roster-enrollments-cu**: 46 fields missing in SAAS
- **roster-enrollments-flexpath**: 46 fields missing in SAAS
- **gradebook-assigments-all**: 27 fields missing in SAAS
- **needs-grading-cu**: 20 fields missing in SAAS
- **needs-grading-su**: 20 fields missing in SAAS
- **discussion**: 16 fields missing in SAAS
- **messages-templates-faculty-templates**: 15 fields missing in SAAS
- **messages-notification**: 14 fields missing in SAAS

### Response Wrapper Removal

The following APIs had their response wrappers removed in SAAS (breaking structural change):

- **course-activity**
- **discussion**
- **gradebook-assigments-all**
- **kaltura-video-my-media**
- **messages-ask-instructor**
- **messages-course-message**
- **messages-sms-inbox**
- **messages-templates-faculty-templates**
- **needs-grading-cu**
- **needs-grading-su**
- **roster-drops**
- **roster-enrollments-cu**
- **roster-enrollments-flexpath**
- **roster-enrollments-su**

---
## 🔍 Detailed API Analysis

### 🟠 HIGH course-activity

**Field Changes**: 8 → 5 fields | **Missing**: 8 | **New**: 5

⚠️ **Structural Change**: Response type changed from `dict` to `list`

⚠️ **Wrapper Removed**: Legacy wrapped response with fields: `message, status, code`

#### 🚨 Missing in SAAS (Critical)

- `code`
- `message`
- `message[].activityScore`
- `message[].activityScoreTrend`
- `message[].courseName`
- `message[].facultyComparison`
- `message[].sectionCount`
- `status`

#### ✅ New in SAAS

- `[].activityScore`
- `[].activityScoreTrend`
- `[].courseName`
- `[].facultyComparison`
- `[].sectionCount`

#### 🔄 Potential Field Mappings

**High Confidence**:
- `message[].activityScoreTrend` → `[].activityScoreTrend`
- `message[].sectionCount` → `[].sectionCount`
- `message[].courseName` → `[].courseName`
- `message[].facultyComparison` → `[].facultyComparison`
- `message[].activityScore` → `[].activityScore`

**Medium Confidence**:
- `message[].activityScoreTrend` → `[].activityScore`
- `message[].activityScore` → `[].activityScoreTrend`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "code": 200,
  "status": "success",
  "message": [
    "..."
  ]
}
```

**SAAS Sample**:
```json
[
  {
    "courseName": "...",
    "sectionCount": "...",
    "activityScore": "...",
    "...": "(2 more fields)"
  },
  "... (4 more items)"
]
```

---

### 🔴 CRITICAL discussion

**Field Changes**: 16 → 12 fields | **Missing**: 16 | **New**: 12

⚠️ **Structural Change**: Response type changed from `dict` to `list`

⚠️ **Wrapper Removed**: Legacy wrapped response with fields: `message, status, code`

#### 🚨 Missing in SAAS (Critical)

- `code`
- `message`
- `message[].assignmentPk`
- `message[].attemptPk`
- `message[].courseId`
- `message[].coursePk`
- `message[].discussionId`
- `message[].discussionLink`
- `message[].discussionTitle`
- `message[].employeeId`
- `message[].escalated`
- `message[].escalationReason`
- `message[].group`
- `message[].reply_id`
- `message[].submittedDate`
- `status`

#### ✅ New in SAAS

- `[].assignmentPk`
- `[].attemptPk`
- `[].discussionId`
- `[].discussionTitle`
- `[].discussionlink`
- `[].escalated`
- `[].escalationReason`
- `[].group`
- `[].isHidden`
- `[].replyId`
- `[].studentHash`
- `[].submittedDate`

#### 🔄 Potential Field Mappings

**High Confidence**:
- `message[].group` → `[].group`
- `message[].discussionTitle` → `[].discussionTitle`
- `message[].escalationReason` → `[].escalationReason`
- `message[].submittedDate` → `[].submittedDate`
- `message[].discussionLink` → `[].discussionlink`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "code": 200,
  "status": "success",
  "message": [
    "...",
    "... (29 more items)"
  ]
}
```

**SAAS Sample**:
```json
[
  {
    "studentHash": "...",
    "assignmentPk": "...",
    "group": "...",
    "...": "(9 more fields)"
  },
  "... (499 more items)"
]
```

---

### 🟡 MEDIUM faculty-info-cu

**Field Changes**: 13 → 15 fields | **Missing**: 1 | **New**: 3

#### 🚨 Missing in SAAS (Critical)

- `courseActivity`

#### ✅ New in SAAS

- `discussionCount`
- `globalInbox[]`
- `needsGrading`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "loginId": "MAHMOUD.ELHARAZI",
  "firstName": "Mahmoud",
  "lastName": "Elharazi",
  "...": "(5 more fields)"
}
```

**SAAS Sample**:
```json
{
  "loginId": "Nayeli.GOODWIN",
  "firstName": "Nayeli",
  "lastName": "Goodwin",
  "...": "(6 more fields)"
}
```

---

### 🔴 CRITICAL gradebook-assigments-all

**Field Changes**: 27 → 16 fields | **Missing**: 27 | **New**: 16

⚠️ **Wrapper Removed**: Legacy wrapped response with fields: `message, status, code`

#### 🚨 Missing in SAAS (Critical)

- `code`
- `message`
- `message.BUS380`
- `message.BUS380.assignments`
- `message.BUS380.assignments[].assignmentId`
- `message.BUS380.assignments[].assignmentTitle`
- `message.BUS380.assignments[].dueDate`
- `message.BUS380.assignments[].overdueCount`
- `message.BUS380.assignments[].points`
- `message.BUS380.sectionCount`
- `message.BUS435`
- `message.BUS435.assignments`
- `message.BUS435.assignments[].assignmentId`
- `message.BUS435.assignments[].assignmentTitle`
- `message.BUS435.assignments[].dueDate`
- `message.BUS435.assignments[].overdueCount`
- `message.BUS435.assignments[].points`
- `message.BUS435.sectionCount`
- `message.BUS437`
- `message.BUS437.assignments`
- `message.BUS437.assignments[].assignmentId`
- `message.BUS437.assignments[].assignmentTitle`
- `message.BUS437.assignments[].dueDate`
- `message.BUS437.assignments[].overdueCount`
- `message.BUS437.assignments[].points`
- `message.BUS437.sectionCount`
- `status`

#### ✅ New in SAAS

- `ACC100`
- `ACC100.assignments`
- `ACC100.assignments[].assignmentId`
- `ACC100.assignments[].assignmentTitle`
- `ACC100.assignments[].dueDate`
- `ACC100.assignments[].overdueCount`
- `ACC100.assignments[].points`
- `ACC100.sectionCount`
- `ACC556`
- `ACC556.assignments`
- `ACC556.assignments[].assignmentId`
- `ACC556.assignments[].assignmentTitle`
- `ACC556.assignments[].dueDate`
- `ACC556.assignments[].overdueCount`
- `ACC556.assignments[].points`
- `ACC556.sectionCount`

#### 🔄 Potential Field Mappings

**High Confidence**:
- `message.BUS435.sectionCount` → `ACC100.sectionCount`
- `message.BUS435.sectionCount` → `ACC556.sectionCount`
- `message.BUS435.assignments[].dueDate` → `ACC556.assignments[].dueDate`
- `message.BUS435.assignments[].dueDate` → `ACC100.assignments[].dueDate`
- `message.BUS435.assignments` → `ACC100.assignments`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "code": 200,
  "status": "success",
  "message": {
    "BUS435": "...",
    "BUS437": "...",
    "BUS380": "..."
  }
}
```

**SAAS Sample**:
```json
{
  "ACC100": {
    "sectionCount": "...",
    "assignments": "..."
  },
  "ACC556": {
    "sectionCount": "...",
    "assignments": "..."
  }
}
```

---

### 🔴 CRITICAL gradebook-export-status

**Field Changes**: 12 → 5 fields | **Missing**: 11 | **New**: 4

#### 🚨 Missing in SAAS (Critical)

- `code`
- `message`
- `message.errorCode`
- `message.errorString`
- `message.response`
- `message.response.errorDescription`
- `message.response.fileKey`
- `message.response.requestDate`
- `message.response.requestId`
- `message.response.status`
- `message.status`

#### ✅ New in SAAS

- `errorDescription`
- `fileKey`
- `requestDate`
- `requestId`

#### 🔄 Potential Field Mappings

**High Confidence**:
- `message.response.requestId` → `requestId`
- `message.response.requestDate` → `requestDate`
- `message.response.fileKey` → `fileKey`
- `message.response.errorDescription` → `errorDescription`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "code": 200,
  "status": "success",
  "message": {
    "response": "...",
    "status": "...",
    "errorCode": "...",
    "...": "(1 more fields)"
  }
}
```

**SAAS Sample**:
```json
{
  "status": null,
  "requestId": null,
  "requestDate": null,
  "...": "(2 more fields)"
}
```

---

### 🟡 MEDIUM instructor-config

**Field Changes**: 1 → 152 fields | **Missing**: 1 | **New**: 152

#### 🚨 Missing in SAAS (Critical)

- `Missing`

#### ✅ New in SAAS

- `generalProperties`
- `generalProperties.adaAlertText`
- `generalProperties.adaAlertText.addExtensionForm`
- `generalProperties.adaAlertText.overviewTab`
- `generalProperties.adaEmail`
- `generalProperties.createCaseUrl`
- `generalProperties.emailTrainingLink`
- `generalProperties.exportCsv`
- `generalProperties.showLetterGrade`
- `generalProperties.smsTrainingLink`
- `generalProperties.terms`
- `generalProperties.terms.accommodation`
- `generalProperties.terms.accommodationAbv`
- `generalProperties.terms.student`
- `generalProperties.timezone`
- `generalProperties.timezoneIdentifier`
- `generalProperties.trainingLink`
- `nav`
- `nav[].conditional`
- `nav[].count`
- `nav[].cssClass`
- `nav[].link`
- `nav[].name`
- `nav[].page`
- `nav[].page[].name`
- `nav[].page[].route`
- `nav[].title`
- `outreachCategories`
- `outreachCategories[].category`
- `outreachCategories[].categoryType`
- `outreachCategories[].id`
- `outreachTypes`
- `outreachTypes[].id`
- `outreachTypes[].name`
- `placeHolders`
- `placeHolders.email`
- `placeHolders.email[]`
- `placeHolders.sms`
- `placeHolders.sms[]`
- `tableColumns`
- `tableColumns.ayi`
- `tableColumns.ayi[].columnName`
- `tableColumns.ayi[].default`
- `tableColumns.ayi[].filterBy`
- `tableColumns.ayi[].mobile`
- `tableColumns.ayi[].propName`
- `tableColumns.ayi[].show`
- `tableColumns.ayi[].sortable`
- `tableColumns.ayi[].type`
- `tableColumns.courseActivity`
- `tableColumns.courseActivity[].mobile`
- `tableColumns.courseActivity[].propName`
- `tableColumns.courseActivity[].selectAll`
- `tableColumns.courseActivity[].show`
- `tableColumns.courseActivity[].sortable`
- `tableColumns.courseActivity[].type`
- `tableColumns.courseRoster`
- `tableColumns.courseRoster[].batchId`
- `tableColumns.courseRoster[].mobile`
- `tableColumns.courseRoster[].propName`
- `tableColumns.courseRoster[].selectAll`
- `tableColumns.courseRoster[].show`
- `tableColumns.courseRoster[].sortable`
- `tableColumns.courseRoster[].type`
- `tableColumns.discussions`
- `tableColumns.discussions[].columnName`
- `tableColumns.discussions[].filterBy`
- `tableColumns.discussions[].mobile`
- `tableColumns.discussions[].propName`
- `tableColumns.discussions[].show`
- `tableColumns.discussions[].sortable`
- `tableColumns.discussions[].type`
- `tableColumns.dropped`
- `tableColumns.dropped[].columnName`
- `tableColumns.dropped[].mobile`
- `tableColumns.dropped[].propName`
- `tableColumns.dropped[].show`
- `tableColumns.dropped[].sortable`
- `tableColumns.dropped[].type`
- `tableColumns.needsGrading`
- `tableColumns.needsGrading[].columnName`
- `tableColumns.needsGrading[].filterBy`
- `tableColumns.needsGrading[].mobile`
- `tableColumns.needsGrading[].propName`
- `tableColumns.needsGrading[].show`
- `tableColumns.needsGrading[].sortable`
- `tableColumns.needsGrading[].type`
- `tableColumns.pilotUsers`
- `tableColumns.pilotUsers[].columnName`
- `tableColumns.pilotUsers[].mobile`
- `tableColumns.pilotUsers[].propName`
- `tableColumns.pilotUsers[].show`
- `tableColumns.pilotUsers[].sortable`
- `tableColumns.pilotUsers[].type`
- `tableColumns.search`
- `tableColumns.search[].columnName`
- `tableColumns.search[].default`
- `tableColumns.search[].filterBy`
- `tableColumns.search[].mobile`
- `tableColumns.search[].propName`
- `tableColumns.search[].show`
- `tableColumns.search[].sortable`
- `tableColumns.search[].type`
- `tableColumns.submitGrades`
- `tableColumns.submitGrades[].columnName`
- `tableColumns.submitGrades[].default`
- `tableColumns.submitGrades[].mobile`
- `tableColumns.submitGrades[].propName`
- `tableColumns.submitGrades[].show`
- `tableColumns.submitGrades[].sortable`
- `tableColumns.submitGrades[].type`
- `tableColumns.templates`
- `tableColumns.templates[].columnName`
- `tableColumns.templates[].default`
- `tableColumns.templates[].isToggle`
- `tableColumns.templates[].mobile`
- `tableColumns.templates[].propName`
- `tableColumns.templates[].show`
- `tableColumns.templates[].sortable`
- `tableColumns.templates[].type`
- `userFeatures`
- `userFeatures.alerts`
- `userFeatures.allAttemptsValid`
- `userFeatures.askYourProfessor`
- `userFeatures.compass`
- `userFeatures.courseActivityMenu`
- `userFeatures.courseRoster`
- `userFeatures.discussions`
- `userFeatures.dropped`
- `userFeatures.email`
- `userFeatures.email.read`
- `userFeatures.email.write`
- `userFeatures.exportGradebook`
- `userFeatures.extensions`
- `userFeatures.extensions.read`
- `userFeatures.extensions.write`
- `userFeatures.facHelp`
- `userFeatures.gradebook`
- `userFeatures.gradebookDetails`
- `userFeatures.gradebookInProgress`
- `userFeatures.gradebookScore`
- `userFeatures.grading`
- `userFeatures.messaging`
- `userFeatures.needsGrading`
- `userFeatures.notificationContent`
- `userFeatures.notifications`
- `userFeatures.outreachTab`
- `userFeatures.roster`
- `userFeatures.submitGrades`
- `userFeatures.textMessage`
- `userFeatures.textMessage.read`
- `userFeatures.textMessage.write`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "Missing": "No api info available "
}
```

**SAAS Sample**:
```json
{
  "nav": [
    "...",
    "... (5 more items)"
  ],
  "userFeatures": {
    "email": "...",
    "alerts": "...",
    "roster": "...",
    "...": "(22 more fields)"
  },
  "generalProperties": {
    "adaEmail": "...",
    "adaAlertText": "...",
    "timezoneIdentifier": "...",
    "...": "(8 more fields)"
  },
  "...": "(4 more fields)"
}
```

---

### 🔴 CRITICAL kaltura-video-my-media

**Field Changes**: 72 → 73 fields | **Missing**: 72 | **New**: 73

⚠️ **Wrapper Removed**: Legacy wrapped response with fields: `message, status, code`

#### 🚨 Missing in SAAS (Critical)

- `code`
- `message`
- `message.objects`
- `message.objects[].accessControlId`
- `message.objects[].adminTags`
- `message.objects[].capabilities`
- `message.objects[].categories`
- `message.objects[].categoriesIds`
- `message.objects[].conversionProfileId`
- `message.objects[].conversionQuality`
- `message.objects[].createdAt`
- `message.objects[].creatorId`
- `message.objects[].creditUrl`
- `message.objects[].creditUserName`
- `message.objects[].dataUrl`
- `message.objects[].description`
- `message.objects[].displayInSearch`
- `message.objects[].downloadUrl`
- `message.objects[].duration`
- `message.objects[].durationType`
- `message.objects[].endDate`
- `message.objects[].entitledUsersEdit`
- `message.objects[].entitledUsersPublish`
- `message.objects[].entitledUsersView`
- `message.objects[].flavorParamsIds`
- `message.objects[].groupId`
- `message.objects[].height`
- `message.objects[].id`
- `message.objects[].isTrimDisabled`
- `message.objects[].lastPlayedAt`
- `message.objects[].licenseType`
- `message.objects[].mediaDate`
- `message.objects[].mediaType`
- `message.objects[].moderationCount`
- `message.objects[].moderationStatus`
- `message.objects[].msDuration`
- `message.objects[].name`
- `message.objects[].operationAttributes`
- `message.objects[].parentEntryId`
- `message.objects[].partnerData`
- `message.objects[].partnerId`
- `message.objects[].partnerSortValue`
- `message.objects[].plays`
- `message.objects[].rank`
- `message.objects[].redirectEntryId`
- `message.objects[].referenceId`
- `message.objects[].relatedObjects`
- `message.objects[].replacedEntryId`
- `message.objects[].replacementStatus`
- `message.objects[].replacingEntryId`
- `message.objects[].rootEntryId`
- `message.objects[].searchProviderId`
- `message.objects[].searchProviderType`
- `message.objects[].searchText`
- `message.objects[].sourceType`
- `message.objects[].startDate`
- `message.objects[].status`
- `message.objects[].streams`
- `message.objects[].tags`
- `message.objects[].templateEntryId`
- `message.objects[].thumbnailUrl`
- `message.objects[].totalRank`
- `message.objects[].type`
- `message.objects[].updatedAt`
- `message.objects[].userId`
- `message.objects[].version`
- `message.objects[].views`
- `message.objects[].votes`
- `message.objects[].width`
- `message.relatedObjects`
- `message.totalCount`
- `status`

#### ✅ New in SAAS

- `objects`
- `objects[].accessControlId`
- `objects[].adminTags`
- `objects[].application`
- `objects[].applicationVersion`
- `objects[].blockAutoTranscript`
- `objects[].capabilities`
- `objects[].categories`
- `objects[].categoriesIds`
- `objects[].conversionProfileId`
- `objects[].conversionQuality`
- `objects[].createdAt`
- `objects[].creatorId`
- `objects[].creditUrl`
- `objects[].creditUserName`
- `objects[].dataUrl`
- `objects[].description`
- `objects[].displayInSearch`
- `objects[].downloadUrl`
- `objects[].duration`
- `objects[].durationType`
- `objects[].embedUrl`
- `objects[].endDate`
- `objects[].entitledUsersEdit`
- `objects[].entitledUsersPublish`
- `objects[].entitledUsersView`
- `objects[].flavorParamsIds`
- `objects[].groupId`
- `objects[].height`
- `objects[].id`
- `objects[].isTrimDisabled`
- `objects[].lastPlayedAt`
- `objects[].licenseType`
- `objects[].mediaDate`
- `objects[].mediaType`
- `objects[].moderationCount`
- `objects[].moderationStatus`
- `objects[].msDuration`
- `objects[].name`
- `objects[].operationAttributes`
- `objects[].parentEntryId`
- `objects[].partnerData`
- `objects[].partnerId`
- `objects[].partnerSortValue`
- `objects[].plays`
- `objects[].rank`
- `objects[].redirectEntryId`
- `objects[].referenceId`
- `objects[].relatedObjects`
- `objects[].replacedEntryId`
- `objects[].replacementStatus`
- `objects[].replacingEntryId`
- `objects[].rootEntryId`
- `objects[].searchProviderId`
- `objects[].searchProviderType`
- `objects[].searchText`
- `objects[].sourceType`
- `objects[].sourceVersion`
- `objects[].startDate`
- `objects[].status`
- `objects[].streams`
- `objects[].tags`
- `objects[].templateEntryId`
- `objects[].thumbnailUrl`
- `objects[].totalRank`
- `objects[].type`
- `objects[].updatedAt`
- `objects[].userId`
- `objects[].version`
- `objects[].views`
- `objects[].votes`
- `objects[].width`
- `totalCount`

#### 🔄 Potential Field Mappings

**High Confidence**:
- `message.objects[].partnerData` → `objects[].partnerData`
- `message.objects[].status` → `objects[].status`
- `message.objects[].moderationStatus` → `objects[].moderationStatus`
- `message.objects[].mediaType` → `objects[].mediaType`
- `message.objects[].parentEntryId` → `objects[].parentEntryId`

**Medium Confidence**:
- `message.objects[].status` → `objects[].replacementStatus`
- `message.objects[].status` → `objects[].moderationStatus`
- `message.objects[].moderationStatus` → `objects[].status`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "code": 200,
  "status": "success",
  "message": {
    "objects": "...",
    "totalCount": "...",
    "relatedObjects": "..."
  }
}
```

**SAAS Sample**:
```json
{
  "objects": [
    "...",
    "... (7 more items)"
  ],
  "totalCount": 8
}
```

---

### 🔴 CRITICAL messages-ask-instructor

**Field Changes**: 11 → 6 fields | **Missing**: 11 | **New**: 6

⚠️ **Wrapper Removed**: Legacy wrapped response with fields: `message, status, code`

#### 🚨 Missing in SAAS (Critical)

- `code`
- `message`
- `message.discussionSummary`
- `message.discussionSummary[].courseId`
- `message.discussionSummary[].courseName`
- `message.discussionSummary[].coursePk`
- `message.discussionSummary[].link`
- `message.discussionSummary[].newPosts`
- `message.discussionSummary[].replies`
- `message.totalPosts`
- `status`

#### ✅ New in SAAS

- `discussionSummary`
- `discussionSummary[].courseName`
- `discussionSummary[].link`
- `discussionSummary[].newPosts`
- `discussionSummary[].replies`
- `totalPosts`

#### 🔄 Potential Field Mappings

**High Confidence**:
- `message.totalPosts` → `totalPosts`
- `message.discussionSummary` → `discussionSummary`
- `message.discussionSummary[].newPosts` → `discussionSummary[].newPosts`
- `message.discussionSummary[].replies` → `discussionSummary[].replies`
- `message.discussionSummary[].courseName` → `discussionSummary[].courseName`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "code": 200,
  "status": "success",
  "message": {
    "totalPosts": "...",
    "discussionSummary": "..."
  }
}
```

**SAAS Sample**:
```json
{
  "totalPosts": 10,
  "discussionSummary": [
    "...",
    "... (3 more items)"
  ]
}
```

---

### 🟠 HIGH messages-course-message

**Field Changes**: 10 → 6 fields | **Missing**: 10 | **New**: 6

⚠️ **Wrapper Removed**: Legacy wrapped response with fields: `message, status, code`

#### 🚨 Missing in SAAS (Critical)

- `code`
- `message`
- `message.messageSummary`
- `message.messageSummary[].courseId`
- `message.messageSummary[].courseName`
- `message.messageSummary[].coursePk`
- `message.messageSummary[].link`
- `message.messageSummary[].unreadMessages`
- `message.totalUnreadMessages`
- `status`

#### ✅ New in SAAS

- `messageSummary`
- `messageSummary[].courseName`
- `messageSummary[].link`
- `messageSummary[].newPosts`
- `messageSummary[].replies`
- `totalUnreadMessages`

#### 🔄 Potential Field Mappings

**High Confidence**:
- `message.messageSummary[].courseName` → `messageSummary[].courseName`
- `message.totalUnreadMessages` → `totalUnreadMessages`
- `message.messageSummary` → `messageSummary`
- `message.messageSummary[].link` → `messageSummary[].link`

**Medium Confidence**:
- `message` → `messageSummary`
- `message` → `totalUnreadMessages`
- `message.messageSummary[].unreadMessages` → `totalUnreadMessages`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "code": 200,
  "status": "success",
  "message": {
    "totalUnreadMessages": "...",
    "messageSummary": "..."
  }
}
```

**SAAS Sample**:
```json
{
  "totalUnreadMessages": 5,
  "messageSummary": [
    "...",
    "... (2 more items)"
  ]
}
```

---

### 🔴 CRITICAL messages-notification

**Field Changes**: 15 → 1 fields | **Missing**: 14 | **New**: 0

#### 🚨 Missing in SAAS (Critical)

- `code`
- `message.notifications`
- `message.notificationsTotalLength`
- `message.notifications[].notificationActive`
- `message.notifications[].notificationEnd`
- `message.notifications[].notificationId`
- `message.notifications[].notificationLinkText`
- `message.notifications[].notificationLinkUrl`
- `message.notifications[].notificationMessage`
- `message.notifications[].notificationRemoved`
- `message.notifications[].notificationStart`
- `message.notifications[].notificationTitle`
- `message.notifications[].notificationType`
- `status`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "code": 200,
  "status": "success",
  "message": {
    "notificationsTotalLength": "...",
    "notifications": "..."
  }
}
```

**SAAS Sample**:
```json
{
  "message": "missing api response"
}
```

---

### 🟠 HIGH messages-sms-inbox

**Field Changes**: 8 → 13 fields | **Missing**: 8 | **New**: 13

⚠️ **Structural Change**: Response type changed from `dict` to `list`

⚠️ **Wrapper Removed**: Legacy wrapped response with fields: `message, status, code`

#### 🚨 Missing in SAAS (Critical)

- `code`
- `message`
- `message[].hash`
- `message[].message`
- `message[].read_status`
- `message[].send_status`
- `message[].timestamp`
- `status`

#### ✅ New in SAAS

- `[].body`
- `[].email`
- `[].firstName`
- `[].inbox`
- `[].lastName`
- `[].messageType`
- `[].phone`
- `[].rank`
- `[].readStatus`
- `[].sendStatus`
- `[].studentHash`
- `[].timestamp`
- `[].unreadCount`

#### 🔄 Potential Field Mappings

**High Confidence**:
- `message[].timestamp` → `[].timestamp`

**Medium Confidence**:
- `message` → `[].messageType`
- `message[].hash` → `[].studentHash`
- `status` → `[].readStatus`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "code": 200,
  "status": "success",
  "message": [
    "..."
  ]
}
```

**SAAS Sample**:
```json
[
  {
    "studentHash": "...",
    "firstName": "...",
    "lastName": "...",
    "...": "(10 more fields)"
  },
  "... (99 more items)"
]
```

---

### 🟢 LOW messages-template-by-id

**Field Changes**: 1 → 1 fields | **Missing**: 0 | **New**: 0

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "missing": "No api response available"
}
```

**SAAS Sample**:
```json
{
  "missing": "No api response available"
}
```

---

### 🔴 CRITICAL messages-templates-faculty-templates

**Field Changes**: 15 → 10 fields | **Missing**: 15 | **New**: 10

⚠️ **Structural Change**: Response type changed from `dict` to `list`

⚠️ **Wrapper Removed**: Legacy wrapped response with fields: `message, status, code`

#### 🚨 Missing in SAAS (Critical)

- `code`
- `message`
- `message[].CATEGORY`
- `message[].CONTENT`
- `message[].FACULTY_ID`
- `message[].ID`
- `message[].IS_DEFAULT`
- `message[].ROW_CREATED_TIME`
- `message[].ROW_MODIFIED_TIME`
- `message[].SUBJECT`
- `message[].TEMPLATE`
- `message[].TEMPLATE_TYPE`
- `message[].TITLE`
- `message[].VIDEO_ID`
- `status`

#### ✅ New in SAAS

- `[].category`
- `[].content`
- `[].isDefault`
- `[].rowCreatedTime`
- `[].rowModifiedTime`
- `[].subject`
- `[].template`
- `[].templateId`
- `[].templateType`
- `[].title`

#### 🔄 Potential Field Mappings

**High Confidence**:
- `message[].TEMPLATE` → `[].template`
- `message[].TITLE` → `[].title`
- `message[].CONTENT` → `[].content`
- `message[].SUBJECT` → `[].subject`
- `message[].CATEGORY` → `[].category`

**Medium Confidence**:
- `message[].TEMPLATE` → `[].templateType`
- `message[].TEMPLATE` → `[].templateId`
- `message[].ID` → `[].templateId`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "code": 200,
  "status": "success",
  "message": [
    "...",
    "... (26 more items)"
  ]
}
```

**SAAS Sample**:
```json
[
  {
    "templateId": "...",
    "title": "...",
    "template": "...",
    "...": "(7 more fields)"
  },
  "... (5 more items)"
]
```

---

### 🔴 CRITICAL needs-grading-cu

**Field Changes**: 20 → 15 fields | **Missing**: 20 | **New**: 15

⚠️ **Structural Change**: Response type changed from `dict` to `list`

⚠️ **Wrapper Removed**: Legacy wrapped response with fields: `message, status, code`

#### 🚨 Missing in SAAS (Critical)

- `code`
- `message`
- `message.assignments`
- `message.assignments[].assignmentPk`
- `message.assignments[].attempts`
- `message.assignments[].attempts[].assignmentLink`
- `message.assignments[].attempts[].assignmentTitle`
- `message.assignments[].attempts[].attemptOrder`
- `message.assignments[].attempts[].attemptPk`
- `message.assignments[].attempts[].escalated`
- `message.assignments[].attempts[].escalationReason`
- `message.assignments[].attempts[].gradeDetailsUrl`
- `message.assignments[].attempts[].submittedDate`
- `message.assignments[].coursePk`
- `message.assignments[].employeeId`
- `message.assignments[].group`
- `message.assignments[].is10x`
- `message.assignments[].learnerPk`
- `message.assignments[].previousGrade`
- `status`

#### ✅ New in SAAS

- `[].assignmentPk`
- `[].attempts`
- `[].attempts[].assignmentLink`
- `[].attempts[].assignmentTitle`
- `[].attempts[].attemptOrder`
- `[].attempts[].attemptPk`
- `[].attempts[].escalated`
- `[].attempts[].escalationReason`
- `[].attempts[].gradeDetailsUrl`
- `[].attempts[].status`
- `[].attempts[].submittedDate`
- `[].gradeGroup`
- `[].is10x`
- `[].previousGrade`
- `[].studentHash`

#### 🔄 Potential Field Mappings

**High Confidence**:
- `message.assignments[].attempts[].escalationReason` → `[].attempts[].escalationReason`
- `message.assignments[].previousGrade` → `[].previousGrade`
- `message.assignments[].attempts[].submittedDate` → `[].attempts[].submittedDate`
- `message.assignments[].attempts[].escalated` → `[].attempts[].escalated`
- `message.assignments[].is10x` → `[].is10x`

**Medium Confidence**:
- `message.assignments[].group` → `[].gradeGroup`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "code": 200,
  "status": "success",
  "message": {
    "assignments": "..."
  }
}
```

**SAAS Sample**:
```json
[
  {
    "studentHash": "...",
    "assignmentPk": "...",
    "is10x": "...",
    "...": "(3 more fields)"
  },
  "... (7 more items)"
]
```

---

### 🔴 CRITICAL needs-grading-su

**Field Changes**: 20 → 15 fields | **Missing**: 20 | **New**: 15

⚠️ **Structural Change**: Response type changed from `dict` to `list`

⚠️ **Wrapper Removed**: Legacy wrapped response with fields: `message, status, code`

#### 🚨 Missing in SAAS (Critical)

- `code`
- `message`
- `message.assignments`
- `message.assignments[].assignmentPk`
- `message.assignments[].attempts`
- `message.assignments[].attempts[].assignmentLink`
- `message.assignments[].attempts[].assignmentTitle`
- `message.assignments[].attempts[].attemptOrder`
- `message.assignments[].attempts[].attemptPk`
- `message.assignments[].attempts[].gradeDetailsUrl`
- `message.assignments[].attempts[].submittedDate`
- `message.assignments[].coursePk`
- `message.assignments[].employeeId`
- `message.assignments[].escalated`
- `message.assignments[].escalationReason`
- `message.assignments[].group`
- `message.assignments[].is10x`
- `message.assignments[].learnerPk`
- `message.assignments[].previousGrade`
- `status`

#### ✅ New in SAAS

- `[].assignmentPk`
- `[].attempts`
- `[].attempts[].assignmentLink`
- `[].attempts[].assignmentTitle`
- `[].attempts[].attemptOrder`
- `[].attempts[].attemptPk`
- `[].attempts[].escalated`
- `[].attempts[].escalationReason`
- `[].attempts[].gradeDetailsUrl`
- `[].attempts[].status`
- `[].attempts[].submittedDate`
- `[].gradeGroup`
- `[].is10x`
- `[].previousGrade`
- `[].studentHash`

#### 🔄 Potential Field Mappings

**High Confidence**:
- `message.assignments[].previousGrade` → `[].previousGrade`
- `message.assignments[].attempts[].submittedDate` → `[].attempts[].submittedDate`
- `message.assignments[].is10x` → `[].is10x`
- `message.assignments[].attempts[].assignmentTitle` → `[].attempts[].assignmentTitle`
- `message.assignments[].attempts` → `[].attempts`

**Medium Confidence**:
- `message.assignments[].group` → `[].gradeGroup`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "code": 200,
  "status": "success",
  "message": {
    "assignments": "..."
  }
}
```

**SAAS Sample**:
```json
[
  {
    "studentHash": "...",
    "assignmentPk": "...",
    "is10x": "...",
    "...": "(3 more fields)"
  },
  "... (7 more items)"
]
```

---

### 🔴 CRITICAL roster-drops

**Field Changes**: 14 → 5 fields | **Missing**: 14 | **New**: 5

⚠️ **Structural Change**: Response type changed from `dict` to `list`

⚠️ **Wrapper Removed**: Legacy wrapped response with fields: `message, status, code`

#### 🚨 Missing in SAAS (Critical)

- `code`
- `message`
- `message.courses`
- `message.courses[].courseId`
- `message.courses[].courseName`
- `message.courses[].coursePk`
- `message.courses[].learners`
- `message.courses[].learners[].droppedOutDate`
- `message.courses[].learners[].emailId`
- `message.courses[].learners[].employeeID`
- `message.courses[].learners[].firstName`
- `message.courses[].learners[].lastName`
- `message.courses[].learners[].learnerPk`
- `status`

#### ✅ New in SAAS

- `[].courseName`
- `[].students`
- `[].students[].dropDate`
- `[].students[].firstName`
- `[].students[].lastName`

#### 🔄 Potential Field Mappings

**High Confidence**:
- `message.courses[].courseName` → `[].courseName`
- `message.courses[].learners[].firstName` → `[].students[].firstName`
- `message.courses[].learners[].lastName` → `[].students[].lastName`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "code": 200,
  "status": "success",
  "message": {
    "courses": "..."
  }
}
```

**SAAS Sample**:
```json
[
  {
    "courseName": "...",
    "students": "..."
  },
  "... (15 more items)"
]
```

---

### 🔴 CRITICAL roster-enrollments-cu

**Field Changes**: 46 → 76 fields | **Missing**: 46 | **New**: 76

⚠️ **Structural Change**: Response type changed from `dict` to `list`

⚠️ **Wrapper Removed**: Legacy wrapped response with fields: `message, status, code`

#### 🚨 Missing in SAAS (Critical)

- `code`
- `message`
- `message[].HASH`
- `message[].advisorEmail`
- `message[].advisorName`
- `message[].advisorPhone`
- `message[].alerts`
- `message[].alertsCount`
- `message[].alerts[]`
- `message[].city`
- `message[].courseName`
- `message[].coursePkId`
- `message[].courseRoom`
- `message[].courseTextNumber`
- `message[].daysToDrop`
- `message[].dropDt`
- `message[].droppedOutDate`
- `message[].emailAddress`
- `message[].employeeId`
- `message[].endDate`
- `message[].enrollmentDate`
- `message[].firstName`
- `message[].fullName`
- `message[].grade`
- `message[].hasMilestones`
- `message[].isCanvas`
- `message[].lastAcadEngDt`
- `message[].lastAccessDt`
- `message[].lastName`
- `message[].lastOutreachDate`
- `message[].longCourseId`
- `message[].mobileNumber`
- `message[].outreachCount`
- `message[].overDueCount`
- `message[].phone`
- `message[].phone[].number`
- `message[].phone[].type`
- `message[].priorityScore`
- `message[].role`
- `message[].startDate`
- `message[].state`
- `message[].systemTags`
- `message[].systemTags[]`
- `message[].tags`
- `message[].userName`
- `status`

#### ✅ New in SAAS

- `[].activeExtension`
- `[].activityScore`
- `[].activityScoreBand`
- `[].activityScoreTrend`
- `[].ada`
- `[].advisor`
- `[].advisorEmail`
- `[].advisorPhone`
- `[].alerts`
- `[].alertsCount`
- `[].alerts[]`
- `[].censusDt`
- `[].city`
- `[].courseCategory`
- `[].courseName`
- `[].coursePk`
- `[].courseSisId`
- `[].courseStartDate`
- `[].courseTextNumber`
- `[].csEngDt`
- `[].currentMilestone`
- `[].daysToDrop`
- `[].dropDt`
- `[].email`
- `[].endDt`
- `[].enrolledDays`
- `[].enrollmentDt`
- `[].facultyId`
- `[].firstName`
- `[].firstTerm`
- `[].futureDropDt`
- `[].grade`
- `[].gradeFinal`
- `[].gradeMidterm`
- `[].hasMilestones`
- `[].isActiveCourse`
- `[].isCourseStarted`
- `[].isJWMI`
- `[].lastAcadEngDt`
- `[].lastAccessDt`
- `[].lastAssessmentDt`
- `[].lastEngDiff`
- `[].lastName`
- `[].lastOutreachDt`
- `[].learnerId`
- `[].letterGrade`
- `[].nsoNotComplete`
- `[].nsoOutreachDt`
- `[].numDays`
- `[].oeeInd`
- `[].outreachCount`
- `[].outreachCountToday`
- `[].overdue50Count`
- `[].overdueCount`
- `[].phone`
- `[].phoneType`
- `[].priorityPilotGroup`
- `[].priorityRiskLevel`
- `[].priorityScore`
- `[].regBlocker`
- `[].retake`
- `[].role`
- `[].startDt`
- `[].state`
- `[].studentHash`
- `[].submittedAssignments`
- `[].suppressEngFlag`
- `[].systemTags`
- `[].tags`
- `[].tags[].tagId`
- `[].tags[].tagName`
- `[].totalAssignments`
- `[].totalPoints`
- `[].userName`
- `[].visiting`
- `[].weeksInMilestone`

#### 🔄 Potential Field Mappings

**High Confidence**:
- `message[].priorityScore` → `[].priorityScore`
- `message[].courseName` → `[].courseName`
- `message[].hasMilestones` → `[].hasMilestones`
- `message[].outreachCount` → `[].outreachCount`
- `message[].systemTags` → `[].systemTags`

**Medium Confidence**:
- `message[].advisorName` → `[].advisor`
- `message[].phone[].type` → `[].phoneType`
- `message[].phone[].number` → `[].courseTextNumber`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "code": 200,
  "status": "success",
  "message": [
    "...",
    "... (36 more items)"
  ]
}
```

**SAAS Sample**:
```json
[
  {
    "firstName": "...",
    "studentHash": "...",
    "lastName": "...",
    "...": "(70 more fields)"
  },
  "... (22 more items)"
]
```

---

### 🔴 CRITICAL roster-enrollments-flexpath

**Field Changes**: 46 → 76 fields | **Missing**: 46 | **New**: 76

⚠️ **Structural Change**: Response type changed from `dict` to `list`

⚠️ **Wrapper Removed**: Legacy wrapped response with fields: `message, status, code`

#### 🚨 Missing in SAAS (Critical)

- `code`
- `message`
- `message[].HASH`
- `message[].advisorEmail`
- `message[].advisorName`
- `message[].advisorPhone`
- `message[].alerts`
- `message[].alertsCount`
- `message[].alerts[]`
- `message[].city`
- `message[].courseName`
- `message[].coursePkId`
- `message[].courseRoom`
- `message[].courseTextNumber`
- `message[].daysToDrop`
- `message[].dropDt`
- `message[].droppedOutDate`
- `message[].emailAddress`
- `message[].employeeId`
- `message[].endDate`
- `message[].enrollmentDate`
- `message[].firstName`
- `message[].fullName`
- `message[].grade`
- `message[].hasMilestones`
- `message[].isCanvas`
- `message[].lastAcadEngDt`
- `message[].lastAccessDt`
- `message[].lastName`
- `message[].lastOutreachDate`
- `message[].longCourseId`
- `message[].mobileNumber`
- `message[].outreachCount`
- `message[].overDueCount`
- `message[].phone`
- `message[].phone[].number`
- `message[].phone[].type`
- `message[].priorityScore`
- `message[].role`
- `message[].startDate`
- `message[].state`
- `message[].systemTags`
- `message[].systemTags[]`
- `message[].tags`
- `message[].userName`
- `status`

#### ✅ New in SAAS

- `[].activeExtension`
- `[].activityScore`
- `[].activityScoreBand`
- `[].activityScoreTrend`
- `[].ada`
- `[].advisor`
- `[].advisorEmail`
- `[].advisorPhone`
- `[].alerts`
- `[].alertsCount`
- `[].alerts[]`
- `[].censusDt`
- `[].city`
- `[].courseCategory`
- `[].courseName`
- `[].coursePk`
- `[].courseSisId`
- `[].courseStartDate`
- `[].courseTextNumber`
- `[].csEngDt`
- `[].currentMilestone`
- `[].daysToDrop`
- `[].dropDt`
- `[].email`
- `[].endDt`
- `[].enrolledDays`
- `[].enrollmentDt`
- `[].facultyId`
- `[].firstName`
- `[].firstTerm`
- `[].futureDropDt`
- `[].grade`
- `[].gradeFinal`
- `[].gradeMidterm`
- `[].hasMilestones`
- `[].isActiveCourse`
- `[].isCourseStarted`
- `[].isJWMI`
- `[].lastAcadEngDt`
- `[].lastAccessDt`
- `[].lastAssessmentDt`
- `[].lastEngDiff`
- `[].lastName`
- `[].lastOutreachDt`
- `[].learnerId`
- `[].letterGrade`
- `[].nsoNotComplete`
- `[].nsoOutreachDt`
- `[].numDays`
- `[].oeeInd`
- `[].outreachCount`
- `[].outreachCountToday`
- `[].overdue50Count`
- `[].overdueCount`
- `[].phone`
- `[].phoneType`
- `[].priorityPilotGroup`
- `[].priorityRiskLevel`
- `[].priorityScore`
- `[].regBlocker`
- `[].retake`
- `[].role`
- `[].startDt`
- `[].state`
- `[].studentHash`
- `[].submittedAssignments`
- `[].suppressEngFlag`
- `[].systemTags`
- `[].tags`
- `[].tags[].tagId`
- `[].tags[].tagName`
- `[].totalAssignments`
- `[].totalPoints`
- `[].userName`
- `[].visiting`
- `[].weeksInMilestone`

#### 🔄 Potential Field Mappings

**High Confidence**:
- `message[].priorityScore` → `[].priorityScore`
- `message[].courseName` → `[].courseName`
- `message[].hasMilestones` → `[].hasMilestones`
- `message[].outreachCount` → `[].outreachCount`
- `message[].systemTags` → `[].systemTags`

**Medium Confidence**:
- `message[].advisorName` → `[].advisor`
- `message[].phone[].type` → `[].phoneType`
- `message[].phone[].number` → `[].courseTextNumber`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "code": 200,
  "status": "success",
  "message": [
    "...",
    "... (36 more items)"
  ]
}
```

**SAAS Sample**:
```json
[
  {
    "firstName": "...",
    "studentHash": "...",
    "lastName": "...",
    "...": "(70 more fields)"
  },
  "... (22 more items)"
]
```

---

### 🔴 CRITICAL roster-enrollments-su

**Field Changes**: 50 → 76 fields | **Missing**: 50 | **New**: 76

⚠️ **Structural Change**: Response type changed from `dict` to `list`

⚠️ **Wrapper Removed**: Legacy wrapped response with fields: `message, status, code`

#### 🚨 Missing in SAAS (Critical)

- `code`
- `message`
- `message[].HASH`
- `message[].activityScore`
- `message[].activityScoreBand`
- `message[].activityScoreTrend`
- `message[].advisorEmail`
- `message[].advisorName`
- `message[].advisorPhone`
- `message[].alerts`
- `message[].alertsCount`
- `message[].city`
- `message[].courseName`
- `message[].coursePkId`
- `message[].courseRoom`
- `message[].courseTextNumber`
- `message[].daysToDrop`
- `message[].deanEmail`
- `message[].deanName`
- `message[].deanPhone`
- `message[].dropDt`
- `message[].emailAddress`
- `message[].employeeId`
- `message[].endDate`
- `message[].enrollmentDate`
- `message[].firstName`
- `message[].fullName`
- `message[].grade`
- `message[].isCanvas`
- `message[].lastAcadEngDt`
- `message[].lastAccessDt`
- `message[].lastName`
- `message[].lastOutreachDate`
- `message[].letterGrade`
- `message[].longCourseId`
- `message[].mobileNumber`
- `message[].outreachCount`
- `message[].overDue50Count`
- `message[].overDueCount`
- `message[].phone`
- `message[].phone[].number`
- `message[].phone[].type`
- `message[].role`
- `message[].startDate`
- `message[].state`
- `message[].systemTags`
- `message[].systemTags[]`
- `message[].tags`
- `message[].totalPoints`
- `status`

#### ✅ New in SAAS

- `[].activeExtension`
- `[].activityScore`
- `[].activityScoreBand`
- `[].activityScoreTrend`
- `[].ada`
- `[].advisor`
- `[].advisorEmail`
- `[].advisorPhone`
- `[].alerts`
- `[].alertsCount`
- `[].alerts[]`
- `[].censusDt`
- `[].city`
- `[].courseCategory`
- `[].courseName`
- `[].coursePk`
- `[].courseSisId`
- `[].courseStartDate`
- `[].courseTextNumber`
- `[].csEngDt`
- `[].currentMilestone`
- `[].daysToDrop`
- `[].dropDt`
- `[].email`
- `[].endDt`
- `[].enrolledDays`
- `[].enrollmentDt`
- `[].facultyId`
- `[].firstName`
- `[].firstTerm`
- `[].futureDropDt`
- `[].grade`
- `[].gradeFinal`
- `[].gradeMidterm`
- `[].hasMilestones`
- `[].isActiveCourse`
- `[].isCourseStarted`
- `[].isJWMI`
- `[].lastAcadEngDt`
- `[].lastAccessDt`
- `[].lastAssessmentDt`
- `[].lastEngDiff`
- `[].lastName`
- `[].lastOutreachDt`
- `[].learnerId`
- `[].letterGrade`
- `[].nsoNotComplete`
- `[].nsoOutreachDt`
- `[].numDays`
- `[].oeeInd`
- `[].outreachCount`
- `[].outreachCountToday`
- `[].overdue50Count`
- `[].overdueCount`
- `[].phone`
- `[].phoneType`
- `[].priorityPilotGroup`
- `[].priorityRiskLevel`
- `[].priorityScore`
- `[].regBlocker`
- `[].retake`
- `[].role`
- `[].startDt`
- `[].state`
- `[].studentHash`
- `[].submittedAssignments`
- `[].suppressEngFlag`
- `[].systemTags`
- `[].tags`
- `[].tags[].tagId`
- `[].tags[].tagName`
- `[].totalAssignments`
- `[].totalPoints`
- `[].userName`
- `[].visiting`
- `[].weeksInMilestone`

#### 🔄 Potential Field Mappings

**High Confidence**:
- `message[].courseName` → `[].courseName`
- `message[].totalPoints` → `[].totalPoints`
- `message[].activityScore` → `[].activityScore`
- `message[].outreachCount` → `[].outreachCount`
- `message[].systemTags` → `[].systemTags`

**Medium Confidence**:
- `message[].advisorName` → `[].advisor`
- `message[].phone[].type` → `[].phoneType`
- `message[].deanPhone` → `[].phone`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "code": 200,
  "status": "success",
  "message": [
    "...",
    "... (9 more items)"
  ]
}
```

**SAAS Sample**:
```json
[
  {
    "firstName": "...",
    "studentHash": "...",
    "lastName": "...",
    "...": "(70 more fields)"
  },
  "... (22 more items)"
]
```

---

### 🟡 MEDIUM submit-grades-grade-details

**Field Changes**: 1 → 7 fields | **Missing**: 1 | **New**: 7

⚠️ **Structural Change**: Response type changed from `dict` to `list`

#### 🚨 Missing in SAAS (Critical)

- `missing`

#### ✅ New in SAAS

- `[].courseSisId`
- `[].final`
- `[].gradingScale`
- `[].gradingScale[].calculated_value`
- `[].gradingScale[].name`
- `[].gradingScale[].value`
- `[].midterm`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "missing": "No api response available"
}
```

**SAAS Sample**:
```json
[
  {
    "courseSisId": "...",
    "gradingScale": "...",
    "midterm": "...",
    "...": "(1 more fields)"
  },
  "... (99 more items)"
]
```

---

### 🔴 CRITICAL submit-grades-{{exam}}-course-sis-id-{{course-sis-id}}

**Field Changes**: 13 → 10 fields | **Missing**: 12 | **New**: 9

#### 🚨 Missing in SAAS (Critical)

- `code`
- `message`
- `message.gradeDetails`
- `message.gradeDetails[].employeeId`
- `message.gradeDetails[].gradeLetter`
- `message.gradeDetails[].needsGrading`
- `message.gradeDetails[].submitted`
- `message.gradeDetails[].totalPoints`
- `message.gradeDetails[].totalSubmissions`
- `message.status`
- `message.submittedBy`
- `message.submittedDt`

#### ✅ New in SAAS

- `learnerGrades`
- `learnerGrades[].gradeLetter`
- `learnerGrades[].needsGrading`
- `learnerGrades[].studentHash`
- `learnerGrades[].submitted`
- `learnerGrades[].totalPoints`
- `learnerGrades[].totalSubmissions`
- `submittedBy`
- `submittedDt`

#### 🔄 Potential Field Mappings

**High Confidence**:
- `message.submittedDt` → `submittedDt`
- `message.gradeDetails[].submitted` → `learnerGrades[].submitted`
- `message.gradeDetails[].gradeLetter` → `learnerGrades[].gradeLetter`
- `message.gradeDetails[].totalSubmissions` → `learnerGrades[].totalSubmissions`
- `message.gradeDetails[].totalPoints` → `learnerGrades[].totalPoints`

**Medium Confidence**:
- `message.submittedDt` → `learnerGrades[].submitted`
- `message.gradeDetails[].submitted` → `submittedDt`
- `message.gradeDetails[].submitted` → `submittedBy`

#### 📋 Response Structure Comparison

**Legacy Sample**:
```json
{
  "code": 200,
  "status": "success",
  "message": {
    "status": "...",
    "submittedDt": "...",
    "submittedBy": "...",
    "...": "(1 more fields)"
  }
}
```

**SAAS Sample**:
```json
{
  "status": "NOT_SUBMITTED",
  "submittedDt": null,
  "submittedBy": null,
  "...": "(1 more fields)"
}
```

---

## 🎯 Recommendations & Action Items

### Immediate Actions (Priority 1)

1. **Critical Field Mapping**: Review and map all missing fields identified in high-impact APIs
2. **Response Wrapper Handling**: Update client code to handle unwrapped SAAS responses
3. **Error Handling**: Implement fallback mechanisms for missing fields
4. **Data Validation**: Add validation for required fields in SAAS responses

### Short-term Actions (Priority 2)

1. **Field Mapping Documentation**: Create comprehensive mapping documentation for renamed fields
2. **Client Library Updates**: Update API client libraries to handle structural differences
3. **Integration Testing**: Comprehensive testing of all affected integrations
4. **Monitoring Setup**: Implement monitoring for missing field errors in production

### Long-term Actions (Priority 3)

1. **API Standardization**: Work with SAAS team to standardize response formats
2. **Backward Compatibility**: Implement compatibility layers where feasible
3. **Documentation Updates**: Update all API documentation with new field structures
4. **Migration Guides**: Create detailed migration guides for development teams

### Critical APIs Requiring Immediate Review

Based on the analysis, the following APIs require immediate attention due to significant field losses:

