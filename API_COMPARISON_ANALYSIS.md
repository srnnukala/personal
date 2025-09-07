# API Legacy vs SaaS Comparison Analysis

This document provides a detailed comparison between Legacy and SaaS API responses for each endpoint.

## Table of Contents
- [course-activity](#course-activity)
- [discussion](#discussion)
- [faculty-info-cu](#faculty-info-cu)
- [gradebook-assigments-all](#gradebook-assigments-all)
- [gradebook-export-status](#gradebook-export-status)
- [instructor-config](#instructor-config)
- [kaltura-video-my-media](#kaltura-video-my-media)
- [messages-ask-instructor](#messages-ask-instructor)
- [messages-course-message](#messages-course-message)
- [messages-notification](#messages-notification)
- [messages-sms-inbox](#messages-sms-inbox)
- [messages-template-by-id](#messages-template-by-id)
- [messages-templates-faculty-templates](#messages-templates-faculty-templates)
- [needs-grading-cu](#needs-grading-cu)
- [needs-grading-su](#needs-grading-su)
- [roster-drops](#roster-drops)
- [roster-enrollments-cu](#roster-enrollments-cu)
- [roster-enrollments-flexpath](#roster-enrollments-flexpath)
- [roster-enrollments-su](#roster-enrollments-su)
- [submit-grades-grade-details](#submit-grades-grade-details)
- [submit-grades-{{exam}}-course-sis-id-{{course-sis-id}}](#submit-grades-exam-course-sis-id-course-sis-id)

## course-activity

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 5 |
| SaaS Fields Count | 5 |
| New Fields in SaaS | 0 |
| Missing from SaaS | 0 |
| Common Fields | 5 |
| Type Changes | 0 |
| Potential Renames | 0 |

---

## discussion

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 13 |
| SaaS Fields Count | 12 |
| New Fields in SaaS | 4 |
| Missing from SaaS | 5 |
| Common Fields | 8 |
| Type Changes | 5 |
| Potential Renames | 2 |

### New Fields Added in SaaS
| Field Name | Type |
|------------|------|
| `[0].discussionlink` | NoneType |
| `[0].isHidden` | bool |
| `[0].replyId` | int |
| `[0].studentHash` | str |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `[0].courseId` | str |
| `[0].coursePk` | str |
| `[0].discussionLink` | str |
| `[0].employeeId` | str |
| `[0].reply_id` | str |

### Fields with Type Changes
| Field Name | Legacy Type | SaaS Type |
|------------|-------------|-----------|
| `[0].assignmentPk` | str | int |
| `[0].escalationReason` | str | NoneType |
| `[0].attemptPk` | str | NoneType |
| `[0].discussionId` | str | int |
| `[0].group` | str | NoneType |

### Potential Field Renames
| Legacy Field | SaaS Field | Legacy Type | SaaS Type |
|--------------|------------|-------------|-----------|
| `[0].reply_id` | `[0].replyId` | str | int |
| `[0].discussionLink` | `[0].discussionlink` | str | NoneType |

---

## faculty-info-cu

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 13 |
| SaaS Fields Count | 14 |
| New Fields in SaaS | 2 |
| Missing from SaaS | 1 |
| Common Fields | 12 |
| Type Changes | 0 |
| Potential Renames | 0 |

### New Fields Added in SaaS
| Field Name | Type |
|------------|------|
| `discussionCount` | int |
| `needsGrading` | int |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `courseActivity` | bool |

---

## gradebook-assigments-all

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 24 |
| SaaS Fields Count | 16 |
| New Fields in SaaS | 16 |
| Missing from SaaS | 24 |
| Common Fields | 0 |
| Type Changes | 0 |
| Potential Renames | 42 |

### New Fields Added in SaaS
| Field Name | Type |
|------------|------|
| `ACC100` | dict |
| `ACC100.assignments` | list |
| `ACC100.assignments[0].assignmentId` | str |
| `ACC100.assignments[0].assignmentTitle` | str |
| `ACC100.assignments[0].dueDate` | str |
| `ACC100.assignments[0].overdueCount` | int |
| `ACC100.assignments[0].points` | int |
| `ACC100.sectionCount` | int |
| `ACC556` | dict |
| `ACC556.assignments` | list |
| `ACC556.assignments[0].assignmentId` | str |
| `ACC556.assignments[0].assignmentTitle` | str |
| `ACC556.assignments[0].dueDate` | str |
| `ACC556.assignments[0].overdueCount` | int |
| `ACC556.assignments[0].points` | int |
| `ACC556.sectionCount` | int |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `BUS380` | dict |
| `BUS380.assignments` | list |
| `BUS380.assignments[0].assignmentId` | str |
| `BUS380.assignments[0].assignmentTitle` | str |
| `BUS380.assignments[0].dueDate` | str |
| `BUS380.assignments[0].overdueCount` | int |
| `BUS380.assignments[0].points` | int |
| `BUS380.sectionCount` | int |
| `BUS435` | dict |
| `BUS435.assignments` | list |
| `BUS435.assignments[0].assignmentId` | str |
| `BUS435.assignments[0].assignmentTitle` | str |
| `BUS435.assignments[0].dueDate` | str |
| `BUS435.assignments[0].overdueCount` | int |
| `BUS435.assignments[0].points` | int |
| `BUS435.sectionCount` | int |
| `BUS437` | dict |
| `BUS437.assignments` | list |
| `BUS437.assignments[0].assignmentId` | str |
| `BUS437.assignments[0].assignmentTitle` | str |
| `BUS437.assignments[0].dueDate` | str |
| `BUS437.assignments[0].overdueCount` | int |
| `BUS437.assignments[0].points` | int |
| `BUS437.sectionCount` | int |

### Potential Field Renames
| Legacy Field | SaaS Field | Legacy Type | SaaS Type |
|--------------|------------|-------------|-----------|
| `BUS380.assignments[0].points` | `ACC556.assignments[0].points` | int | int |
| `BUS380.assignments[0].points` | `ACC100.assignments[0].points` | int | int |
| `BUS380.assignments[0].overdueCount` | `ACC100.assignments[0].overdueCount` | int | int |
| `BUS380.assignments[0].overdueCount` | `ACC556.assignments[0].overdueCount` | int | int |
| `BUS435.assignments[0].assignmentId` | `ACC556.assignments[0].assignmentId` | str | str |
| `BUS435.assignments[0].assignmentId` | `ACC100.assignments[0].assignmentId` | str | str |
| `BUS437.assignments[0].dueDate` | `ACC100.assignments[0].dueDate` | str | str |
| `BUS437.assignments[0].dueDate` | `ACC556.assignments[0].dueDate` | str | str |
| `BUS437.assignments[0].assignmentId` | `ACC556.assignments[0].assignmentId` | str | str |
| `BUS437.assignments[0].assignmentId` | `ACC100.assignments[0].assignmentId` | str | str |
| `BUS435.sectionCount` | `ACC556.sectionCount` | int | int |
| `BUS435.sectionCount` | `ACC100.sectionCount` | int | int |
| `BUS437.assignments[0].points` | `ACC556.assignments[0].points` | int | int |
| `BUS437.assignments[0].points` | `ACC100.assignments[0].points` | int | int |
| `BUS380.assignments[0].assignmentTitle` | `ACC100.assignments[0].assignmentTitle` | str | str |
| `BUS380.assignments[0].assignmentTitle` | `ACC556.assignments[0].assignmentTitle` | str | str |
| `BUS435.assignments[0].overdueCount` | `ACC100.assignments[0].overdueCount` | int | int |
| `BUS435.assignments[0].overdueCount` | `ACC556.assignments[0].overdueCount` | int | int |
| `BUS380.sectionCount` | `ACC556.sectionCount` | int | int |
| `BUS380.sectionCount` | `ACC100.sectionCount` | int | int |
| `BUS380.assignments[0].dueDate` | `ACC100.assignments[0].dueDate` | str | str |
| `BUS380.assignments[0].dueDate` | `ACC556.assignments[0].dueDate` | str | str |
| `BUS437.sectionCount` | `ACC556.sectionCount` | int | int |
| `BUS437.sectionCount` | `ACC100.sectionCount` | int | int |
| `BUS437.assignments[0].overdueCount` | `ACC100.assignments[0].overdueCount` | int | int |
| `BUS437.assignments[0].overdueCount` | `ACC556.assignments[0].overdueCount` | int | int |
| `BUS435.assignments[0].dueDate` | `ACC100.assignments[0].dueDate` | str | str |
| `BUS435.assignments[0].dueDate` | `ACC556.assignments[0].dueDate` | str | str |
| `BUS380.assignments[0].assignmentId` | `ACC556.assignments[0].assignmentId` | str | str |
| `BUS380.assignments[0].assignmentId` | `ACC100.assignments[0].assignmentId` | str | str |
| `BUS380.assignments` | `ACC100.assignments` | list | list |
| `BUS380.assignments` | `ACC556.assignments` | list | list |
| `BUS435.assignments` | `ACC100.assignments` | list | list |
| `BUS435.assignments` | `ACC556.assignments` | list | list |
| `BUS435.assignments[0].points` | `ACC556.assignments[0].points` | int | int |
| `BUS435.assignments[0].points` | `ACC100.assignments[0].points` | int | int |
| `BUS437.assignments[0].assignmentTitle` | `ACC100.assignments[0].assignmentTitle` | str | str |
| `BUS437.assignments[0].assignmentTitle` | `ACC556.assignments[0].assignmentTitle` | str | str |
| `BUS435.assignments[0].assignmentTitle` | `ACC100.assignments[0].assignmentTitle` | str | str |
| `BUS435.assignments[0].assignmentTitle` | `ACC556.assignments[0].assignmentTitle` | str | str |
| `BUS437.assignments` | `ACC100.assignments` | list | list |
| `BUS437.assignments` | `ACC556.assignments` | list | list |

---

## gradebook-export-status

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 9 |
| SaaS Fields Count | 5 |
| New Fields in SaaS | 4 |
| Missing from SaaS | 8 |
| Common Fields | 1 |
| Type Changes | 1 |
| Potential Renames | 4 |

### New Fields Added in SaaS
| Field Name | Type |
|------------|------|
| `errorDescription` | NoneType |
| `fileKey` | NoneType |
| `requestDate` | NoneType |
| `requestId` | NoneType |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `errorCode` | int |
| `errorString` | NoneType |
| `response` | dict |
| `response.errorDescription` | NoneType |
| `response.fileKey` | NoneType |
| `response.requestDate` | NoneType |
| `response.requestId` | NoneType |
| `response.status` | NoneType |

### Fields with Type Changes
| Field Name | Legacy Type | SaaS Type |
|------------|-------------|-----------|
| `status` | str | NoneType |

### Potential Field Renames
| Legacy Field | SaaS Field | Legacy Type | SaaS Type |
|--------------|------------|-------------|-----------|
| `response.requestId` | `requestId` | NoneType | NoneType |
| `response.requestDate` | `requestDate` | NoneType | NoneType |
| `response.errorDescription` | `errorDescription` | NoneType | NoneType |
| `response.fileKey` | `fileKey` | NoneType | NoneType |

---

## instructor-config

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 1 |
| SaaS Fields Count | 150 |
| New Fields in SaaS | 150 |
| Missing from SaaS | 1 |
| Common Fields | 0 |
| Type Changes | 0 |
| Potential Renames | 0 |

### New Fields Added in SaaS
| Field Name | Type |
|------------|------|
| `generalProperties` | dict |
| `generalProperties.adaAlertText` | dict |
| `generalProperties.adaAlertText.addExtensionForm` | bool |
| `generalProperties.adaAlertText.overviewTab` | bool |
| `generalProperties.adaEmail` | str |
| `generalProperties.createCaseUrl` | str |
| `generalProperties.emailTrainingLink` | str |
| `generalProperties.exportCsv` | bool |
| `generalProperties.showLetterGrade` | bool |
| `generalProperties.smsTrainingLink` | str |
| `generalProperties.terms` | dict |
| `generalProperties.terms.accommodation` | str |
| `generalProperties.terms.accommodationAbv` | str |
| `generalProperties.terms.student` | str |
| `generalProperties.timezone` | str |
| `generalProperties.timezoneIdentifier` | str |
| `generalProperties.trainingLink` | str |
| `nav` | list |
| `nav[0].conditional` | str |
| `nav[0].count` | NoneType |
| `nav[0].cssClass` | NoneType |
| `nav[0].link` | NoneType |
| `nav[0].name` | str |
| `nav[0].page` | list |
| `nav[0].page[0].name` | str |
| `nav[0].page[0].route` | str |
| `nav[0].title` | NoneType |
| `outreachCategories` | list |
| `outreachCategories[0].category` | str |
| `outreachCategories[0].categoryType` | str |
| `outreachCategories[0].id` | int |
| `outreachTypes` | list |
| `outreachTypes[0].id` | int |
| `outreachTypes[0].name` | str |
| `placeHolders` | dict |
| `placeHolders.email` | list |
| `placeHolders.sms` | list |
| `tableColumns` | dict |
| `tableColumns.ayi` | list |
| `tableColumns.ayi[0].columnName` | str |
| `tableColumns.ayi[0].default` | int |
| `tableColumns.ayi[0].filterBy` | bool |
| `tableColumns.ayi[0].mobile` | bool |
| `tableColumns.ayi[0].propName` | str |
| `tableColumns.ayi[0].show` | bool |
| `tableColumns.ayi[0].sortable` | bool |
| `tableColumns.ayi[0].type` | str |
| `tableColumns.courseActivity` | list |
| `tableColumns.courseActivity[0].mobile` | bool |
| `tableColumns.courseActivity[0].propName` | str |
| `tableColumns.courseActivity[0].selectAll` | bool |
| `tableColumns.courseActivity[0].show` | bool |
| `tableColumns.courseActivity[0].sortable` | bool |
| `tableColumns.courseActivity[0].type` | str |
| `tableColumns.courseRoster` | list |
| `tableColumns.courseRoster[0].batchId` | str |
| `tableColumns.courseRoster[0].mobile` | bool |
| `tableColumns.courseRoster[0].propName` | str |
| `tableColumns.courseRoster[0].selectAll` | bool |
| `tableColumns.courseRoster[0].show` | bool |
| `tableColumns.courseRoster[0].sortable` | bool |
| `tableColumns.courseRoster[0].type` | str |
| `tableColumns.discussions` | list |
| `tableColumns.discussions[0].columnName` | str |
| `tableColumns.discussions[0].filterBy` | bool |
| `tableColumns.discussions[0].mobile` | bool |
| `tableColumns.discussions[0].propName` | str |
| `tableColumns.discussions[0].show` | bool |
| `tableColumns.discussions[0].sortable` | bool |
| `tableColumns.discussions[0].type` | str |
| `tableColumns.dropped` | list |
| `tableColumns.dropped[0].columnName` | str |
| `tableColumns.dropped[0].mobile` | bool |
| `tableColumns.dropped[0].propName` | str |
| `tableColumns.dropped[0].show` | bool |
| `tableColumns.dropped[0].sortable` | bool |
| `tableColumns.dropped[0].type` | str |
| `tableColumns.needsGrading` | list |
| `tableColumns.needsGrading[0].columnName` | str |
| `tableColumns.needsGrading[0].filterBy` | bool |
| `tableColumns.needsGrading[0].mobile` | bool |
| `tableColumns.needsGrading[0].propName` | str |
| `tableColumns.needsGrading[0].show` | bool |
| `tableColumns.needsGrading[0].sortable` | bool |
| `tableColumns.needsGrading[0].type` | str |
| `tableColumns.pilotUsers` | list |
| `tableColumns.pilotUsers[0].columnName` | str |
| `tableColumns.pilotUsers[0].mobile` | bool |
| `tableColumns.pilotUsers[0].propName` | str |
| `tableColumns.pilotUsers[0].show` | bool |
| `tableColumns.pilotUsers[0].sortable` | bool |
| `tableColumns.pilotUsers[0].type` | str |
| `tableColumns.search` | list |
| `tableColumns.search[0].columnName` | str |
| `tableColumns.search[0].default` | int |
| `tableColumns.search[0].filterBy` | bool |
| `tableColumns.search[0].mobile` | bool |
| `tableColumns.search[0].propName` | str |
| `tableColumns.search[0].show` | bool |
| `tableColumns.search[0].sortable` | bool |
| `tableColumns.search[0].type` | str |
| `tableColumns.submitGrades` | list |
| `tableColumns.submitGrades[0].columnName` | str |
| `tableColumns.submitGrades[0].default` | bool |
| `tableColumns.submitGrades[0].mobile` | bool |
| `tableColumns.submitGrades[0].propName` | str |
| `tableColumns.submitGrades[0].show` | bool |
| `tableColumns.submitGrades[0].sortable` | bool |
| `tableColumns.submitGrades[0].type` | str |
| `tableColumns.templates` | list |
| `tableColumns.templates[0].columnName` | str |
| `tableColumns.templates[0].default` | int |
| `tableColumns.templates[0].isToggle` | bool |
| `tableColumns.templates[0].mobile` | bool |
| `tableColumns.templates[0].propName` | str |
| `tableColumns.templates[0].show` | bool |
| `tableColumns.templates[0].sortable` | bool |
| `tableColumns.templates[0].type` | str |
| `userFeatures` | dict |
| `userFeatures.alerts` | bool |
| `userFeatures.allAttemptsValid` | bool |
| `userFeatures.askYourProfessor` | bool |
| `userFeatures.compass` | bool |
| `userFeatures.courseActivityMenu` | bool |
| `userFeatures.courseRoster` | bool |
| `userFeatures.discussions` | bool |
| `userFeatures.dropped` | bool |
| `userFeatures.email` | dict |
| `userFeatures.email.read` | bool |
| `userFeatures.email.write` | bool |
| `userFeatures.exportGradebook` | bool |
| `userFeatures.extensions` | dict |
| `userFeatures.extensions.read` | bool |
| `userFeatures.extensions.write` | bool |
| `userFeatures.facHelp` | bool |
| `userFeatures.gradebook` | bool |
| `userFeatures.gradebookDetails` | bool |
| `userFeatures.gradebookInProgress` | bool |
| `userFeatures.gradebookScore` | bool |
| `userFeatures.grading` | bool |
| `userFeatures.messaging` | bool |
| `userFeatures.needsGrading` | bool |
| `userFeatures.notificationContent` | bool |
| `userFeatures.notifications` | bool |
| `userFeatures.outreachTab` | bool |
| `userFeatures.roster` | bool |
| `userFeatures.submitGrades` | bool |
| `userFeatures.textMessage` | dict |
| `userFeatures.textMessage.read` | bool |
| `userFeatures.textMessage.write` | bool |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `Missing` | str |

---

## kaltura-video-my-media

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 69 |
| SaaS Fields Count | 73 |
| New Fields in SaaS | 5 |
| Missing from SaaS | 1 |
| Common Fields | 68 |
| Type Changes | 14 |
| Potential Renames | 0 |

### New Fields Added in SaaS
| Field Name | Type |
|------------|------|
| `objects[0].application` | NoneType |
| `objects[0].applicationVersion` | NoneType |
| `objects[0].blockAutoTranscript` | NoneType |
| `objects[0].embedUrl` | str |
| `objects[0].sourceVersion` | NoneType |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `relatedObjects` | NoneType |

### Fields with Type Changes
| Field Name | Legacy Type | SaaS Type |
|------------|-------------|-----------|
| `objects[0].groupId` | str | NoneType |
| `objects[0].status` | int | str |
| `objects[0].description` | NoneType | str |
| `objects[0].partnerData` | str | NoneType |
| `objects[0].lastPlayedAt` | int | NoneType |
| `objects[0].type` | int | str |
| `objects[0].creditUserName` | str | NoneType |
| `objects[0].replacementStatus` | int | str |
| `objects[0].conversionQuality` | int | str |
| `objects[0].durationType` | NoneType | int |
| `objects[0].templateEntryId` | NoneType | str |
| `objects[0].creditUrl` | str | NoneType |
| `objects[0].licenseType` | int | str |
| `objects[0].displayInSearch` | int | str |

---

## messages-ask-instructor

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 8 |
| SaaS Fields Count | 6 |
| New Fields in SaaS | 0 |
| Missing from SaaS | 2 |
| Common Fields | 6 |
| Type Changes | 0 |
| Potential Renames | 0 |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `discussionSummary[0].courseId` | str |
| `discussionSummary[0].coursePk` | str |

---

## messages-course-message

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 7 |
| SaaS Fields Count | 6 |
| New Fields in SaaS | 2 |
| Missing from SaaS | 3 |
| Common Fields | 4 |
| Type Changes | 0 |
| Potential Renames | 0 |

### New Fields Added in SaaS
| Field Name | Type |
|------------|------|
| `messageSummary[0].newPosts` | int |
| `messageSummary[0].replies` | int |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `messageSummary[0].courseId` | str |
| `messageSummary[0].coursePk` | str |
| `messageSummary[0].unreadMessages` | int |

---

## messages-notification

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 12 |
| SaaS Fields Count | 1 |
| New Fields in SaaS | 1 |
| Missing from SaaS | 12 |
| Common Fields | 0 |
| Type Changes | 0 |
| Potential Renames | 1 |

### New Fields Added in SaaS
| Field Name | Type |
|------------|------|
| `message` | str |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `notifications` | list |
| `notificationsTotalLength` | int |
| `notifications[0].notificationActive` | bool |
| `notifications[0].notificationEnd` | str |
| `notifications[0].notificationId` | str |
| `notifications[0].notificationLinkText` | str |
| `notifications[0].notificationLinkUrl` | str |
| `notifications[0].notificationMessage` | str |
| `notifications[0].notificationRemoved` | str |
| `notifications[0].notificationStart` | str |
| `notifications[0].notificationTitle` | str |
| `notifications[0].notificationType` | str |

### Potential Field Renames
| Legacy Field | SaaS Field | Legacy Type | SaaS Type |
|--------------|------------|-------------|-----------|
| `notifications[0].notificationMessage` | `message` | str | str |

---

## messages-sms-inbox

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 5 |
| SaaS Fields Count | 13 |
| New Fields in SaaS | 12 |
| Missing from SaaS | 4 |
| Common Fields | 1 |
| Type Changes | 0 |
| Potential Renames | 4 |

### New Fields Added in SaaS
| Field Name | Type |
|------------|------|
| `[0].body` | str |
| `[0].email` | str |
| `[0].firstName` | str |
| `[0].inbox` | int |
| `[0].lastName` | str |
| `[0].messageType` | str |
| `[0].phone` | str |
| `[0].rank` | int |
| `[0].readStatus` | bool |
| `[0].sendStatus` | str |
| `[0].studentHash` | str |
| `[0].unreadCount` | int |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `[0].hash` | str |
| `[0].message` | str |
| `[0].read_status` | int |
| `[0].send_status` | str |

### Potential Field Renames
| Legacy Field | SaaS Field | Legacy Type | SaaS Type |
|--------------|------------|-------------|-----------|
| `[0].send_status` | `[0].sendStatus` | str | str |
| `[0].read_status` | `[0].readStatus` | int | bool |
| `[0].message` | `[0].messageType` | str | str |
| `[0].hash` | `[0].studentHash` | str | str |

---

## messages-template-by-id

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 1 |
| SaaS Fields Count | 1 |
| New Fields in SaaS | 0 |
| Missing from SaaS | 0 |
| Common Fields | 1 |
| Type Changes | 0 |
| Potential Renames | 0 |

---

## messages-templates-faculty-templates

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 12 |
| SaaS Fields Count | 10 |
| New Fields in SaaS | 10 |
| Missing from SaaS | 12 |
| Common Fields | 0 |
| Type Changes | 0 |
| Potential Renames | 13 |

### New Fields Added in SaaS
| Field Name | Type |
|------------|------|
| `[0].category` | str |
| `[0].content` | str |
| `[0].isDefault` | bool |
| `[0].rowCreatedTime` | str |
| `[0].rowModifiedTime` | str |
| `[0].subject` | str |
| `[0].template` | str |
| `[0].templateId` | int |
| `[0].templateType` | str |
| `[0].title` | str |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `[0].CATEGORY` | NoneType |
| `[0].CONTENT` | str |
| `[0].FACULTY_ID` | str |
| `[0].ID` | int |
| `[0].IS_DEFAULT` | int |
| `[0].ROW_CREATED_TIME` | str |
| `[0].ROW_MODIFIED_TIME` | str |
| `[0].SUBJECT` | NoneType |
| `[0].TEMPLATE` | str |
| `[0].TEMPLATE_TYPE` | str |
| `[0].TITLE` | str |
| `[0].VIDEO_ID` | NoneType |

### Potential Field Renames
| Legacy Field | SaaS Field | Legacy Type | SaaS Type |
|--------------|------------|-------------|-----------|
| `[0].ID` | `[0].templateId` | int | int |
| `[0].TEMPLATE_TYPE` | `[0].template` | str | str |
| `[0].TEMPLATE_TYPE` | `[0].templateType` | str | str |
| `[0].CONTENT` | `[0].content` | str | str |
| `[0].CATEGORY` | `[0].category` | NoneType | str |
| `[0].TEMPLATE` | `[0].template` | str | str |
| `[0].TEMPLATE` | `[0].templateType` | str | str |
| `[0].TEMPLATE` | `[0].templateId` | str | int |
| `[0].TITLE` | `[0].title` | str | str |
| `[0].SUBJECT` | `[0].subject` | NoneType | str |
| `[0].ROW_CREATED_TIME` | `[0].rowCreatedTime` | str | str |
| `[0].IS_DEFAULT` | `[0].isDefault` | int | bool |
| `[0].ROW_MODIFIED_TIME` | `[0].rowModifiedTime` | str | str |

---

## needs-grading-cu

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 17 |
| SaaS Fields Count | 15 |
| New Fields in SaaS | 15 |
| Missing from SaaS | 17 |
| Common Fields | 0 |
| Type Changes | 0 |
| Potential Renames | 13 |

### New Fields Added in SaaS
| Field Name | Type |
|------------|------|
| `[0].assignmentPk` | int |
| `[0].attempts` | list |
| `[0].attempts[0].assignmentLink` | str |
| `[0].attempts[0].assignmentTitle` | str |
| `[0].attempts[0].attemptOrder` | int |
| `[0].attempts[0].attemptPk` | int |
| `[0].attempts[0].escalated` | NoneType |
| `[0].attempts[0].escalationReason` | NoneType |
| `[0].attempts[0].gradeDetailsUrl` | str |
| `[0].attempts[0].status` | str |
| `[0].attempts[0].submittedDate` | str |
| `[0].gradeGroup` | str |
| `[0].is10x` | bool |
| `[0].previousGrade` | NoneType |
| `[0].studentHash` | str |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `assignments` | list |
| `assignments[0].assignmentPk` | str |
| `assignments[0].attempts` | list |
| `assignments[0].attempts[0].assignmentLink` | str |
| `assignments[0].attempts[0].assignmentTitle` | str |
| `assignments[0].attempts[0].attemptOrder` | int |
| `assignments[0].attempts[0].attemptPk` | str |
| `assignments[0].attempts[0].escalated` | bool |
| `assignments[0].attempts[0].escalationReason` | NoneType |
| `assignments[0].attempts[0].gradeDetailsUrl` | str |
| `assignments[0].attempts[0].submittedDate` | str |
| `assignments[0].coursePk` | str |
| `assignments[0].employeeId` | str |
| `assignments[0].group` | str |
| `assignments[0].is10x` | bool |
| `assignments[0].learnerPk` | str |
| `assignments[0].previousGrade` | str |

### Potential Field Renames
| Legacy Field | SaaS Field | Legacy Type | SaaS Type |
|--------------|------------|-------------|-----------|
| `assignments[0].attempts[0].escalated` | `[0].attempts[0].escalated` | bool | NoneType |
| `assignments[0].attempts[0].attemptOrder` | `[0].attempts[0].attemptOrder` | int | int |
| `assignments[0].attempts[0].gradeDetailsUrl` | `[0].attempts[0].gradeDetailsUrl` | str | str |
| `assignments[0].assignmentPk` | `[0].assignmentPk` | str | int |
| `assignments[0].attempts` | `[0].attempts` | list | list |
| `assignments[0].attempts[0].assignmentTitle` | `[0].attempts[0].assignmentTitle` | str | str |
| `assignments[0].is10x` | `[0].is10x` | bool | bool |
| `assignments[0].group` | `[0].gradeGroup` | str | str |
| `assignments[0].previousGrade` | `[0].previousGrade` | str | NoneType |
| `assignments[0].attempts[0].escalationReason` | `[0].attempts[0].escalationReason` | NoneType | NoneType |
| `assignments[0].attempts[0].submittedDate` | `[0].attempts[0].submittedDate` | str | str |
| `assignments[0].attempts[0].attemptPk` | `[0].attempts[0].attemptPk` | str | int |
| `assignments[0].attempts[0].assignmentLink` | `[0].attempts[0].assignmentLink` | str | str |

---

## needs-grading-su

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 17 |
| SaaS Fields Count | 15 |
| New Fields in SaaS | 15 |
| Missing from SaaS | 17 |
| Common Fields | 0 |
| Type Changes | 0 |
| Potential Renames | 13 |

### New Fields Added in SaaS
| Field Name | Type |
|------------|------|
| `[0].assignmentPk` | int |
| `[0].attempts` | list |
| `[0].attempts[0].assignmentLink` | str |
| `[0].attempts[0].assignmentTitle` | str |
| `[0].attempts[0].attemptOrder` | int |
| `[0].attempts[0].attemptPk` | int |
| `[0].attempts[0].escalated` | NoneType |
| `[0].attempts[0].escalationReason` | NoneType |
| `[0].attempts[0].gradeDetailsUrl` | str |
| `[0].attempts[0].status` | str |
| `[0].attempts[0].submittedDate` | str |
| `[0].gradeGroup` | str |
| `[0].is10x` | bool |
| `[0].previousGrade` | NoneType |
| `[0].studentHash` | str |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `assignments` | list |
| `assignments[0].assignmentPk` | str |
| `assignments[0].attempts` | list |
| `assignments[0].attempts[0].assignmentLink` | str |
| `assignments[0].attempts[0].assignmentTitle` | str |
| `assignments[0].attempts[0].attemptOrder` | int |
| `assignments[0].attempts[0].attemptPk` | str |
| `assignments[0].attempts[0].gradeDetailsUrl` | str |
| `assignments[0].attempts[0].submittedDate` | str |
| `assignments[0].coursePk` | str |
| `assignments[0].employeeId` | str |
| `assignments[0].escalated` | bool |
| `assignments[0].escalationReason` | NoneType |
| `assignments[0].group` | NoneType |
| `assignments[0].is10x` | bool |
| `assignments[0].learnerPk` | str |
| `assignments[0].previousGrade` | str |

### Potential Field Renames
| Legacy Field | SaaS Field | Legacy Type | SaaS Type |
|--------------|------------|-------------|-----------|
| `assignments[0].attempts[0].attemptOrder` | `[0].attempts[0].attemptOrder` | int | int |
| `assignments[0].attempts[0].gradeDetailsUrl` | `[0].attempts[0].gradeDetailsUrl` | str | str |
| `assignments[0].assignmentPk` | `[0].assignmentPk` | str | int |
| `assignments[0].attempts` | `[0].attempts` | list | list |
| `assignments[0].attempts[0].assignmentTitle` | `[0].attempts[0].assignmentTitle` | str | str |
| `assignments[0].escalationReason` | `[0].attempts[0].escalationReason` | NoneType | NoneType |
| `assignments[0].is10x` | `[0].is10x` | bool | bool |
| `assignments[0].group` | `[0].gradeGroup` | NoneType | str |
| `assignments[0].previousGrade` | `[0].previousGrade` | str | NoneType |
| `assignments[0].attempts[0].submittedDate` | `[0].attempts[0].submittedDate` | str | str |
| `assignments[0].escalated` | `[0].attempts[0].escalated` | bool | NoneType |
| `assignments[0].attempts[0].attemptPk` | `[0].attempts[0].attemptPk` | str | int |
| `assignments[0].attempts[0].assignmentLink` | `[0].attempts[0].assignmentLink` | str | str |

---

## roster-drops

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 11 |
| SaaS Fields Count | 5 |
| New Fields in SaaS | 5 |
| Missing from SaaS | 11 |
| Common Fields | 0 |
| Type Changes | 0 |
| Potential Renames | 3 |

### New Fields Added in SaaS
| Field Name | Type |
|------------|------|
| `[0].courseName` | str |
| `[0].students` | list |
| `[0].students[0].dropDate` | str |
| `[0].students[0].firstName` | str |
| `[0].students[0].lastName` | str |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `courses` | list |
| `courses[0].courseId` | str |
| `courses[0].courseName` | str |
| `courses[0].coursePk` | str |
| `courses[0].learners` | list |
| `courses[0].learners[0].droppedOutDate` | str |
| `courses[0].learners[0].emailId` | str |
| `courses[0].learners[0].employeeID` | str |
| `courses[0].learners[0].firstName` | str |
| `courses[0].learners[0].lastName` | str |
| `courses[0].learners[0].learnerPk` | str |

### Potential Field Renames
| Legacy Field | SaaS Field | Legacy Type | SaaS Type |
|--------------|------------|-------------|-----------|
| `courses[0].learners[0].firstName` | `[0].students[0].firstName` | str | str |
| `courses[0].courseName` | `[0].courseName` | str | str |
| `courses[0].learners[0].lastName` | `[0].students[0].lastName` | str | str |

---

## roster-enrollments-cu

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 41 |
| SaaS Fields Count | 75 |
| New Fields in SaaS | 52 |
| Missing from SaaS | 18 |
| Common Fields | 23 |
| Type Changes | 4 |
| Potential Renames | 7 |

### New Fields Added in SaaS
| Field Name | Type |
|------------|------|
| `[0].activeExtension` | int |
| `[0].activityScore` | float |
| `[0].activityScoreBand` | int |
| `[0].activityScoreTrend` | int |
| `[0].ada` | str |
| `[0].advisor` | str |
| `[0].censusDt` | NoneType |
| `[0].courseCategory` | str |
| `[0].coursePk` | int |
| `[0].courseSisId` | str |
| `[0].courseStartDate` | NoneType |
| `[0].csEngDt` | str |
| `[0].currentMilestone` | NoneType |
| `[0].email` | str |
| `[0].endDt` | str |
| `[0].enrolledDays` | NoneType |
| `[0].enrollmentDt` | str |
| `[0].facultyId` | str |
| `[0].firstTerm` | str |
| `[0].futureDropDt` | str |
| `[0].gradeFinal` | NoneType |
| `[0].gradeMidterm` | str |
| `[0].isActiveCourse` | bool |
| `[0].isCourseStarted` | bool |
| `[0].isJWMI` | bool |
| `[0].lastAssessmentDt` | NoneType |
| `[0].lastEngDiff` | int |
| `[0].lastOutreachDt` | NoneType |
| `[0].learnerId` | str |
| `[0].letterGrade` | str |
| `[0].nsoNotComplete` | str |
| `[0].nsoOutreachDt` | NoneType |
| `[0].numDays` | int |
| `[0].oeeInd` | NoneType |
| `[0].outreachCountToday` | int |
| `[0].overdue50Count` | int |
| `[0].overdueCount` | int |
| `[0].phoneType` | str |
| `[0].priorityPilotGroup` | NoneType |
| `[0].priorityRiskLevel` | NoneType |
| `[0].regBlocker` | bool |
| `[0].retake` | str |
| `[0].startDt` | str |
| `[0].studentHash` | str |
| `[0].submittedAssignments` | NoneType |
| `[0].suppressEngFlag` | NoneType |
| `[0].tags[0].tagId` | int |
| `[0].tags[0].tagName` | str |
| `[0].totalAssignments` | NoneType |
| `[0].totalPoints` | str |
| `[0].visiting` | str |
| `[0].weeksInMilestone` | NoneType |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `[0].HASH` | str |
| `[0].advisorName` | str |
| `[0].coursePkId` | int |
| `[0].courseRoom` | NoneType |
| `[0].droppedOutDate` | NoneType |
| `[0].emailAddress` | str |
| `[0].employeeId` | str |
| `[0].endDate` | str |
| `[0].enrollmentDate` | str |
| `[0].fullName` | str |
| `[0].isCanvas` | bool |
| `[0].lastOutreachDate` | str |
| `[0].longCourseId` | str |
| `[0].mobileNumber` | str |
| `[0].overDueCount` | int |
| `[0].phone[0].number` | str |
| `[0].phone[0].type` | str |
| `[0].startDate` | str |

### Fields with Type Changes
| Field Name | Legacy Type | SaaS Type |
|------------|-------------|-----------|
| `[0].advisorEmail` | NoneType | str |
| `[0].priorityScore` | NoneType | float |
| `[0].courseTextNumber` | str | NoneType |
| `[0].phone` | list | str |

### Potential Field Renames
| Legacy Field | SaaS Field | Legacy Type | SaaS Type |
|--------------|------------|-------------|-----------|
| `[0].overDueCount` | `[0].overdueCount` | int | int |
| `[0].coursePkId` | `[0].coursePk` | int | int |
| `[0].phone[0].type` | `[0].phoneType` | str | str |
| `[0].emailAddress` | `[0].email` | str | str |
| `[0].startDate` | `[0].courseStartDate` | str | NoneType |
| `[0].HASH` | `[0].studentHash` | str | str |
| `[0].advisorName` | `[0].advisor` | str | str |

---

## roster-enrollments-flexpath

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 41 |
| SaaS Fields Count | 75 |
| New Fields in SaaS | 52 |
| Missing from SaaS | 18 |
| Common Fields | 23 |
| Type Changes | 4 |
| Potential Renames | 7 |

### New Fields Added in SaaS
| Field Name | Type |
|------------|------|
| `[0].activeExtension` | int |
| `[0].activityScore` | float |
| `[0].activityScoreBand` | int |
| `[0].activityScoreTrend` | int |
| `[0].ada` | str |
| `[0].advisor` | str |
| `[0].censusDt` | NoneType |
| `[0].courseCategory` | str |
| `[0].coursePk` | int |
| `[0].courseSisId` | str |
| `[0].courseStartDate` | NoneType |
| `[0].csEngDt` | str |
| `[0].currentMilestone` | NoneType |
| `[0].email` | str |
| `[0].endDt` | str |
| `[0].enrolledDays` | NoneType |
| `[0].enrollmentDt` | str |
| `[0].facultyId` | str |
| `[0].firstTerm` | str |
| `[0].futureDropDt` | str |
| `[0].gradeFinal` | NoneType |
| `[0].gradeMidterm` | str |
| `[0].isActiveCourse` | bool |
| `[0].isCourseStarted` | bool |
| `[0].isJWMI` | bool |
| `[0].lastAssessmentDt` | NoneType |
| `[0].lastEngDiff` | int |
| `[0].lastOutreachDt` | NoneType |
| `[0].learnerId` | str |
| `[0].letterGrade` | str |
| `[0].nsoNotComplete` | str |
| `[0].nsoOutreachDt` | NoneType |
| `[0].numDays` | int |
| `[0].oeeInd` | NoneType |
| `[0].outreachCountToday` | int |
| `[0].overdue50Count` | int |
| `[0].overdueCount` | int |
| `[0].phoneType` | str |
| `[0].priorityPilotGroup` | NoneType |
| `[0].priorityRiskLevel` | NoneType |
| `[0].regBlocker` | bool |
| `[0].retake` | str |
| `[0].startDt` | str |
| `[0].studentHash` | str |
| `[0].submittedAssignments` | NoneType |
| `[0].suppressEngFlag` | NoneType |
| `[0].tags[0].tagId` | int |
| `[0].tags[0].tagName` | str |
| `[0].totalAssignments` | NoneType |
| `[0].totalPoints` | str |
| `[0].visiting` | str |
| `[0].weeksInMilestone` | NoneType |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `[0].HASH` | str |
| `[0].advisorName` | str |
| `[0].coursePkId` | int |
| `[0].courseRoom` | NoneType |
| `[0].droppedOutDate` | NoneType |
| `[0].emailAddress` | str |
| `[0].employeeId` | str |
| `[0].endDate` | str |
| `[0].enrollmentDate` | str |
| `[0].fullName` | str |
| `[0].isCanvas` | bool |
| `[0].lastOutreachDate` | str |
| `[0].longCourseId` | str |
| `[0].mobileNumber` | str |
| `[0].overDueCount` | int |
| `[0].phone[0].number` | str |
| `[0].phone[0].type` | str |
| `[0].startDate` | str |

### Fields with Type Changes
| Field Name | Legacy Type | SaaS Type |
|------------|-------------|-----------|
| `[0].advisorEmail` | NoneType | str |
| `[0].priorityScore` | NoneType | float |
| `[0].courseTextNumber` | str | NoneType |
| `[0].phone` | list | str |

### Potential Field Renames
| Legacy Field | SaaS Field | Legacy Type | SaaS Type |
|--------------|------------|-------------|-----------|
| `[0].overDueCount` | `[0].overdueCount` | int | int |
| `[0].coursePkId` | `[0].coursePk` | int | int |
| `[0].phone[0].type` | `[0].phoneType` | str | str |
| `[0].emailAddress` | `[0].email` | str | str |
| `[0].startDate` | `[0].courseStartDate` | str | NoneType |
| `[0].HASH` | `[0].studentHash` | str | str |
| `[0].advisorName` | `[0].advisor` | str | str |

---

## roster-enrollments-su

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 46 |
| SaaS Fields Count | 75 |
| New Fields in SaaS | 50 |
| Missing from SaaS | 21 |
| Common Fields | 25 |
| Type Changes | 6 |
| Potential Renames | 9 |

### New Fields Added in SaaS
| Field Name | Type |
|------------|------|
| `[0].activeExtension` | int |
| `[0].ada` | str |
| `[0].advisor` | str |
| `[0].censusDt` | NoneType |
| `[0].courseCategory` | str |
| `[0].coursePk` | int |
| `[0].courseSisId` | str |
| `[0].courseStartDate` | NoneType |
| `[0].csEngDt` | str |
| `[0].currentMilestone` | NoneType |
| `[0].email` | str |
| `[0].endDt` | str |
| `[0].enrolledDays` | NoneType |
| `[0].enrollmentDt` | str |
| `[0].facultyId` | str |
| `[0].firstTerm` | str |
| `[0].futureDropDt` | str |
| `[0].gradeFinal` | NoneType |
| `[0].gradeMidterm` | str |
| `[0].hasMilestones` | bool |
| `[0].isActiveCourse` | bool |
| `[0].isCourseStarted` | bool |
| `[0].isJWMI` | bool |
| `[0].lastAssessmentDt` | NoneType |
| `[0].lastEngDiff` | int |
| `[0].lastOutreachDt` | NoneType |
| `[0].learnerId` | str |
| `[0].nsoNotComplete` | str |
| `[0].nsoOutreachDt` | NoneType |
| `[0].numDays` | int |
| `[0].oeeInd` | NoneType |
| `[0].outreachCountToday` | int |
| `[0].overdue50Count` | int |
| `[0].overdueCount` | int |
| `[0].phoneType` | str |
| `[0].priorityPilotGroup` | NoneType |
| `[0].priorityRiskLevel` | NoneType |
| `[0].priorityScore` | float |
| `[0].regBlocker` | bool |
| `[0].retake` | str |
| `[0].startDt` | str |
| `[0].studentHash` | str |
| `[0].submittedAssignments` | NoneType |
| `[0].suppressEngFlag` | NoneType |
| `[0].tags[0].tagId` | int |
| `[0].tags[0].tagName` | str |
| `[0].totalAssignments` | NoneType |
| `[0].userName` | str |
| `[0].visiting` | str |
| `[0].weeksInMilestone` | NoneType |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `[0].HASH` | str |
| `[0].advisorName` | str |
| `[0].coursePkId` | str |
| `[0].courseRoom` | str |
| `[0].deanEmail` | str |
| `[0].deanName` | str |
| `[0].deanPhone` | str |
| `[0].emailAddress` | str |
| `[0].employeeId` | str |
| `[0].endDate` | str |
| `[0].enrollmentDate` | str |
| `[0].fullName` | str |
| `[0].isCanvas` | bool |
| `[0].lastOutreachDate` | str |
| `[0].longCourseId` | str |
| `[0].mobileNumber` | str |
| `[0].overDue50Count` | int |
| `[0].overDueCount` | int |
| `[0].phone[0].number` | str |
| `[0].phone[0].type` | str |
| `[0].startDate` | str |

### Fields with Type Changes
| Field Name | Legacy Type | SaaS Type |
|------------|-------------|-----------|
| `[0].courseTextNumber` | str | NoneType |
| `[0].phone` | list | str |
| `[0].dropDt` | NoneType | str |
| `[0].daysToDrop` | NoneType | int |
| `[0].totalPoints` | NoneType | str |
| `[0].letterGrade` | NoneType | str |

### Potential Field Renames
| Legacy Field | SaaS Field | Legacy Type | SaaS Type |
|--------------|------------|-------------|-----------|
| `[0].deanEmail` | `[0].email` | str | str |
| `[0].emailAddress` | `[0].email` | str | str |
| `[0].startDate` | `[0].courseStartDate` | str | NoneType |
| `[0].overDue50Count` | `[0].overdue50Count` | int | int |
| `[0].overDueCount` | `[0].overdueCount` | int | int |
| `[0].phone[0].type` | `[0].phoneType` | str | str |
| `[0].HASH` | `[0].studentHash` | str | str |
| `[0].advisorName` | `[0].advisor` | str | str |
| `[0].coursePkId` | `[0].coursePk` | str | int |

---

## submit-grades-grade-details

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 1 |
| SaaS Fields Count | 7 |
| New Fields in SaaS | 7 |
| Missing from SaaS | 1 |
| Common Fields | 0 |
| Type Changes | 0 |
| Potential Renames | 0 |

### New Fields Added in SaaS
| Field Name | Type |
|------------|------|
| `[0].courseSisId` | str |
| `[0].final` | bool |
| `[0].gradingScale` | list |
| `[0].gradingScale[0].calculated_value` | int |
| `[0].gradingScale[0].name` | str |
| `[0].gradingScale[0].value` | float |
| `[0].midterm` | bool |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `missing` | str |

---

## submit-grades-{{exam}}-course-sis-id-{{course-sis-id}}

### Summary
| Metric | Value |
|--------|-------|
| Legacy Fields Count | 10 |
| SaaS Fields Count | 10 |
| New Fields in SaaS | 7 |
| Missing from SaaS | 7 |
| Common Fields | 3 |
| Type Changes | 0 |
| Potential Renames | 5 |

### New Fields Added in SaaS
| Field Name | Type |
|------------|------|
| `learnerGrades` | list |
| `learnerGrades[0].gradeLetter` | str |
| `learnerGrades[0].needsGrading` | bool |
| `learnerGrades[0].studentHash` | str |
| `learnerGrades[0].submitted` | int |
| `learnerGrades[0].totalPoints` | float |
| `learnerGrades[0].totalSubmissions` | int |

### Fields Missing from SaaS (Present in Legacy)
| Field Name | Type |
|------------|------|
| `gradeDetails` | list |
| `gradeDetails[0].employeeId` | str |
| `gradeDetails[0].gradeLetter` | str |
| `gradeDetails[0].needsGrading` | bool |
| `gradeDetails[0].submitted` | int |
| `gradeDetails[0].totalPoints` | float |
| `gradeDetails[0].totalSubmissions` | int |

### Potential Field Renames
| Legacy Field | SaaS Field | Legacy Type | SaaS Type |
|--------------|------------|-------------|-----------|
| `gradeDetails[0].submitted` | `learnerGrades[0].submitted` | int | int |
| `gradeDetails[0].needsGrading` | `learnerGrades[0].needsGrading` | bool | bool |
| `gradeDetails[0].gradeLetter` | `learnerGrades[0].gradeLetter` | str | str |
| `gradeDetails[0].totalPoints` | `learnerGrades[0].totalPoints` | float | float |
| `gradeDetails[0].totalSubmissions` | `learnerGrades[0].totalSubmissions` | int | int |

---
