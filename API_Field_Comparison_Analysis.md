# Comprehensive API Field Comparison Analysis: Legacy vs SAAS
**Generated on**: 2025-09-03 19:33:03

## Executive Summary

- **Total API Endpoints Analyzed**: 18
- **Total Fields Only in Legacy**: 64
- **Total Fields Only in SAAS**: 48
- **Total Common Fields**: 96

## 🔴 CRITICAL: Fields Present in Legacy but NOT in SAAS

**Total Legacy-Only Fields Found**: 64

| # | Endpoint | Field Name | Legacy Type | Notes/Impact |
|---|----------|------------|-------------|--------------|
| 1 | discussion | `coursePk` | unknown | Missing in SaaS |
| 2 | discussion | `courseId` | unknown | Missing in SaaS |
| 3 | needs grading | `assignment.employeeId` | string | No notes |
| 4 | needs grading | `assignment.learnerPk` | string | No notes |
| 5 | needs grading | `assignment.coursePk` | string | No notes |
| 6 | needs grading | `assignment.group` | string | Equivalent to SAAS gradeGroup |
| 7 | faculty-info | `code` | number | Legacy only, top-level |
| 8 | faculty-info | `status` | string | Legacy only, top-level |
| 9 | faculty-info | `message` | object | No notes |
| 10 | faculty-info | `message.oprid` | string | Equivalent to SAAS "loginId" |
| 11 | faculty-info | `message.firstName` | string | No notes |
| 12 | faculty-info | `message.lastName` | string | No notes |
| 13 | faculty-info | `message.email` | string | No notes |
| 14 | faculty-info | `message.globalInbox` | array | No notes |
| 15 | faculty-info | `message.gradebookFilterActive` | boolean | No notes |
| 16 | faculty-info | `message.courseActivityPilot` | boolean | No notes |
| 17 | faculty-info | `message.role` | array<object> | Each has longCourseId + role |
| 18 | faculty-info | `message.role[].longCourseId` | string | No notes |
| 19 | faculty-info | `message.role[].role` | string | No notes |
| 20 | faculty-info | `message.smsActive` | boolean | No notes |
| 21 | my-media | `message` | object | Only Legacy, wrapper for objects |
| 22 | my-media | `relatedObjects` | object/null | Only Legacy, inside message |
| 23 | my-media | `startDate` | None | Legacy only |
| 24 | my-media | `endDate` | None | Legacy only |
| 25 | faculty-templates | `templateId` | number | Legacy only |
| 26 | faculty-templates | `title` | string | Legacy only |
| 27 | faculty-templates | `template` | string | Legacy only (SAAS: message.TEMPLATE) |
| 28 | faculty-templates | `isDefault` | boolean | Legacy only (SAAS: message.IS_DEFAULT) |
| 29 | faculty-templates | `subject` | string/null | Legacy only (SAAS: message.SUBJECT) |
| 30 | faculty-templates | `content` | string | Legacy only (SAAS: message.CONTENT) |
| 31 | faculty-templates | `category` | string/null | Legacy only (SAAS: message.CATEGORY) |
| 32 | faculty-templates | `rowCreatedTime` | string (datetime) | Legacy only (SAAS: message.ROW_CREATED_TIME) |
| 33 | faculty-templates | `rowModifiedTime` | string/null | Legacy only (SAAS: message.ROW_MODIFIED_TIME) |
| 34 | faculty-templates | `templateType` | string | Legacy only (SAAS: message.TEMPLATE_TYPE) |
| 35 | ask-instructor | `discussionSummary[].courseId` | string | Unique to Legacy |
| 36 | ask-instructor | `discussionSummary[].coursePk` | string | Unique to Legacy |
| 37 | ask-instructor | `code` | number | Only in Legacy, top-level |
| 38 | ask-instructor | `status` | string | Only in Legacy, top-level |
| 39 | ask-instructor | `message` | object | Only in Legacy, wrapper for other fields |
| 40 | inbox | `code` | number | Legacy top-level |
| 41 | inbox | `status` | string | Legacy top-level |
| 42 | inbox | `message` | array<object> | Legacy: array of messages |
| 43 | inbox | `hash` | string | Legacy |
| 44 | inbox | `employee_id` | string | Legacy |
| 45 | inbox | `first_name` | string | Legacy |
| 46 | inbox | `last_name` | string | Legacy |
| 47 | inbox | `course_id` | string | Legacy |
| 48 | inbox | `message` | string | Legacy: message text |
| 49 | inbox | `read_status` | number | Legacy: 1/0 |
| 50 | inbox | `send_status` | string | Legacy |
| 51 | messages-course-messages | `messageSummary[].unreadMessages` | number | Legacy only; count of unread messages |
| 52 | messages-course-messages | `messageSummary[].courseId` | string | Legacy only |
| 53 | messages-course-messages | `messageSummary[].coursePk` | string | Legacy only |
| 54 | messages-course-messages | `code` | number | Legacy only, top-level |
| 55 | messages-course-messages | `status` | string | Legacy only, top-level |
| 56 | messages-course-messages | `message` | object | Legacy only; wrapper for the above fields |
| 57 |  roster drops | `code` | unknown | Missing in SaaS |
| 58 |  roster drops | `status` | unknown | Missing in SaaS |
| 59 |  roster drops | `message` | unknown | Missing in SaaS |
| 60 |  roster drops | `courseId` | unknown | Missing in SaaS |
| 61 |  roster drops | `coursePk` | unknown | Missing in SaaS |
| 62 |  roster drops | `learnerPk` | unknown | Missing in SaaS |
| 63 |  roster drops | `employeeID` | unknown | Missing in SaaS |
| 64 |  roster drops | `emailId` | unknown | Missing in SaaS |

### 📊 Analysis and Recommendations

#### 🆔 Missing Identity/Reference Fields

These fields are critical for data linking and may require mapping strategies:
- **coursePk** (discussion): Missing in SaaS
- **courseId** (discussion): Missing in SaaS
- **assignment.employeeId** (needs grading): None
- **assignment.learnerPk** (needs grading): None
- **assignment.coursePk** (needs grading): None
- **message.role[].longCourseId** (faculty-info): None
- **discussionSummary[].courseId** (ask-instructor): Unique to Legacy
- **discussionSummary[].coursePk** (ask-instructor): Unique to Legacy
- **messageSummary[].courseId** (messages-course-messages): Legacy only
- **messageSummary[].coursePk** (messages-course-messages): Legacy only
- **courseId** ( roster drops): Missing in SaaS
- **coursePk** ( roster drops): Missing in SaaS
- **learnerPk** ( roster drops): Missing in SaaS
- **employeeID** ( roster drops): Missing in SaaS

#### 📋 Missing Metadata Fields

These fields provide additional context and may need alternative solutions:
- **code** (faculty-info): Legacy only, top-level
- **status** (faculty-info): Legacy only, top-level
- **message** (faculty-info): None
- **message.oprid** (faculty-info): Equivalent to SAAS "loginId"
- **message.firstName** (faculty-info): None
- **message.lastName** (faculty-info): None
- **message.email** (faculty-info): None
- **message.globalInbox** (faculty-info): None
- **message.gradebookFilterActive** (faculty-info): None
- **message.courseActivityPilot** (faculty-info): None
- **message.role** (faculty-info): Each has longCourseId + role
- **message.role[].longCourseId** (faculty-info): None
- **message.role[].role** (faculty-info): None
- **message.smsActive** (faculty-info): None
- **message** (my-media): Only Legacy, wrapper for objects
- **code** (ask-instructor): Only in Legacy, top-level
- **status** (ask-instructor): Only in Legacy, top-level
- **message** (ask-instructor): Only in Legacy, wrapper for other fields
- **code** (inbox): Legacy top-level
- **status** (inbox): Legacy top-level
- **message** (inbox): Legacy: array of messages
- **message** (inbox): Legacy: message text
- **read_status** (inbox): Legacy: 1/0
- **send_status** (inbox): Legacy
- **messageSummary[].unreadMessages** (messages-course-messages): Legacy only; count of unread messages
- **messageSummary[].courseId** (messages-course-messages): Legacy only
- **messageSummary[].coursePk** (messages-course-messages): Legacy only
- **code** (messages-course-messages): Legacy only, top-level
- **status** (messages-course-messages): Legacy only, top-level
- **message** (messages-course-messages): Legacy only; wrapper for the above fields
- **code** ( roster drops): Missing in SaaS
- **status** ( roster drops): Missing in SaaS
- **message** ( roster drops): Missing in SaaS
- **emailId** ( roster drops): Missing in SaaS

## 🟢 Fields Present in SAAS but NOT in Legacy

**Total SAAS-Only Fields Found**: 48

| # | Endpoint | Field Name | SAAS Type | Notes |
|---|----------|------------|-----------|-------|
| 1 | needs grading | `assignment.studentHash` | string | No notes |
| 2 | needs grading | `assignment.gradeGroup` | string | No notes |
| 3 | needs grading | `assignment.attempts[].status` | string | Attempt‐level status present only in SAAS |
| 4 | faculty-info | `loginId` | string | Legacy uses "oprid" |
| 5 | faculty-info | `courses` | array<object> | No notes |
| 6 | faculty-info | `courses[].courseId` | string | No notes |
| 7 | faculty-info | `courses[].role` | string | No notes |
| 8 | faculty-info | `allCourses` | array<object> | Contains course, strm, sessionCode |
| 9 | faculty-info | `allCourses[].courses` | string | No notes |
| 10 | faculty-info | `allCourses[].strm` | string | No notes |
| 11 | faculty-info | `allCourses[].sessionCode` | string | No notes |
| 12 | faculty-info | `needsGrading` | number | No notes |
| 13 | faculty-info | `discussionCount` | number | No notes |
| 14 | my-media | `startDt` | None | SAAS only |
| 15 | my-media | `endDt` | None | SAAS only |
| 16 | my-media | `embedUrl` | string | SAAS only |
| 17 | faculty-templates | `message.ID` | number | SAAS only |
| 18 | faculty-templates | `message.TITLE` | string | SAAS only |
| 19 | faculty-templates | `message.CONTENT` | string | SAAS only |
| 20 | faculty-templates | `message.TEMPLATE_TYPE` | string | SAAS only (Legacy: templateType) |
| 21 | faculty-templates | `message.FACULTY_ID` | string/number | SAAS only |
| 22 | faculty-templates | `message.SUBJECT` | string | SAAS only (Legacy: subject) |
| 23 | faculty-templates | `message.CATEGORY` | number | SAAS only (Legacy: category, string or null) |
| 24 | faculty-templates | `message.IS_DEFAULT` | boolean/null | SAAS only (Legacy: isDefault, boolean) |
| 25 | faculty-templates | `message.TEMPLATE` | string | SAAS only (Legacy: template) |
| 26 | faculty-templates | `message.ROW_CREATED_TIME` | string (datetime) | SAAS only (Legacy: rowCreatedTime) |
| 27 | faculty-templates | `message.ROW_MODIFIED_TIME` | string (datetime) | SAAS only (Legacy: rowModifiedTime) |
| 28 | faculty-templates | `message.VIDEO_ID` | number | SAAS only |
| 29 | faculty-templates | `message.videoData` | object | SAAS only |
| 30 | faculty-templates | `message.videoData.videoLink` | string | SAAS only |
| 31 | faculty-templates | `message.videoData.dataUrl` | string/null | SAAS only |
| 32 | faculty-templates | `message.videoData.videoId` | string | SAAS only |
| 33 | faculty-templates | `message.videoData.imgUrl` | string | SAAS only |
| 34 | faculty-templates | `message.videoData.name` | string | SAAS only |
| 35 | inbox | `studentHash` | string | SAAS |
| 36 | inbox | `firstName` | string | SAAS |
| 37 | inbox | `lastName` | string | SAAS |
| 38 | inbox | `email` | string | SAAS |
| 39 | inbox | `phone` | string | SAAS |
| 40 | inbox | `body` | string | SAAS |
| 41 | inbox | `readStatus` | boolean | SAAS |
| 42 | inbox | `sendStatus` | string | SAAS |
| 43 | inbox | `messageType` | string | SAAS |
| 44 | inbox | `inbox` | number | SAAS |
| 45 | inbox | `unreadCount` | number | SAAS |
| 46 | inbox | `rank` | number | SAAS |
| 47 | messages-course-messages | `messageSummary[].newPosts` | number | SAAS only; count of new posts |
| 48 | messages-course-messages | `messageSummary[].replies` | number | SAAS only; count of replies |

## 📋 API Endpoint Analysis Summary

| Endpoint | Format | Fields Analyzed | Legacy-Only | SAAS-Only | Common | Status |
|----------|--------|----------------|-------------|-----------|--------|--------|
|  roster drops | legacy_saas_mapping | 15 | 8 | 0 | 2 | 🔴 Has Legacy-Only |
|  roster enrollments | legacy_saas_mapping | 25 | 0 | 0 | 1 | 🟢 Compatible |
|  submit-grades grade-details | minimal | 0 | 0 | 0 | 0 | ⚪ No Data |
| ask-instructor | standard_comparison | 15 | 5 | 0 | 6 | 🔴 Has Legacy-Only |
| courseactivity overview | minimal | 0 | 0 | 0 | 0 | ⚪ No Data |
| discussion | legacy_saas_mapping | 24 | 2 | 0 | 7 | 🔴 Has Legacy-Only |
| faculty-info | standard_comparison | 39 | 14 | 10 | 4 | 🔴 Has Legacy-Only |
| faculty-templates | standard_comparison | 36 | 10 | 18 | 3 | 🔴 Has Legacy-Only |
| flexpath assesments | minimal | 0 | 0 | 0 | 0 | ⚪ No Data |
| flexpath roster | minimal | 0 | 0 | 0 | 0 | ⚪ No Data |
| get assignment all | minimal | 0 | 0 | 0 | 0 | ⚪ No Data |
| inbox | standard_comparison | 29 | 11 | 12 | 1 | 🔴 Has Legacy-Only |
| instructor config | minimal | 0 | 0 | 0 | 0 | ⚪ No Data |
| messages-course-messages | standard_comparison | 16 | 6 | 2 | 4 | 🔴 Has Legacy-Only |
| my-media | standard_comparison | 85 | 4 | 3 | 68 | 🔴 Has Legacy-Only |
| needs grading | standard_comparison | 7 | 4 | 3 | 0 | 🔴 Has Legacy-Only |
| notification | minimal | 0 | 0 | 0 | 0 | ⚪ No Data |
| templates | minimal | 0 | 0 | 0 | 0 | ⚪ No Data |

## 📖 Detailed Analysis by Endpoint

###  roster drops

**Analysis Summary:**
- Total Fields: 15
- Legacy-Only: 8
- SAAS-Only: 0
- Common: 2
- Format: legacy_saas_mapping

#### 🔴 Fields Present in Legacy but NOT in SAAS:

- **`code`** (unknown)
  - **Impact**: Missing in SaaS
- **`status`** (unknown)
  - **Impact**: Missing in SaaS
- **`message`** (unknown)
  - **Impact**: Missing in SaaS
- **`courseId`** (unknown)
  - **Impact**: Missing in SaaS
- **`coursePk`** (unknown)
  - **Impact**: Missing in SaaS
- **`learnerPk`** (unknown)
  - **Impact**: Missing in SaaS
- **`employeeID`** (unknown)
  - **Impact**: Missing in SaaS
- **`emailId`** (unknown)
  - **Impact**: Missing in SaaS

#### ✅ Common Fields: 2

| Field | Legacy Type | SAAS Type | Notes |
|-------|-------------|-----------|-------|
| `firstName` | unknown | unknown | firstName (same) |
| `lastName` | unknown | unknown | lastName (same) |

---

###  roster enrollments

**Analysis Summary:**
- Total Fields: 25
- Legacy-Only: 0
- SAAS-Only: 0
- Common: 1
- Format: legacy_saas_mapping

#### ✅ Common Fields: 1

| Field | Legacy Type | SAAS Type | Notes |
|-------|-------------|-----------|-------|
| `advisorPhone` | unknown | unknown | advisorPhone (same structure) |

---

###  submit-grades grade-details

#### ℹ️ Additional Notes:

- Minimal data sheet

---

### ask-instructor

**Analysis Summary:**
- Total Fields: 15
- Legacy-Only: 5
- SAAS-Only: 0
- Common: 6
- Format: standard_comparison

#### 🔴 Fields Present in Legacy but NOT in SAAS:

- **`discussionSummary[].courseId`** (string)
  - **Impact**: Unique to Legacy
- **`discussionSummary[].coursePk`** (string)
  - **Impact**: Unique to Legacy
- **`code`** (number)
  - **Impact**: Only in Legacy, top-level
- **`status`** (string)
  - **Impact**: Only in Legacy, top-level
- **`message`** (object)
  - **Impact**: Only in Legacy, wrapper for other fields

#### ✅ Common Fields: 6

| Field | Legacy Type | SAAS Type | Notes |
|-------|-------------|-----------|-------|
| `totalPosts` | number | number | Top-level in SAAS, inside message in Legacy |
| `discussionSummary` | array<object> | array<object> | Top-level in SAAS, inside message in Legacy |
| `discussionSummary[].newPosts` | number | number | No notes |
| `discussionSummary[].replies` | number | number | No notes |
| `discussionSummary[].link` | string | string | No notes |
| `discussionSummary[].courseName` | string | string | No notes |

---

### courseactivity overview

#### ℹ️ Additional Notes:

- Minimal data sheet

---

### discussion

**Analysis Summary:**
- Total Fields: 24
- Legacy-Only: 2
- SAAS-Only: 0
- Common: 7
- Format: legacy_saas_mapping

#### 🔴 Fields Present in Legacy but NOT in SAAS:

- **`coursePk`** (unknown)
  - **Impact**: Missing in SaaS
- **`courseId`** (unknown)
  - **Impact**: Missing in SaaS

#### ✅ Common Fields: 7

| Field | Legacy Type | SAAS Type | Notes |
|-------|-------------|-----------|-------|
| `assignmentPk` | unknown | unknown | assignmentPk (changed to number type) |
| `group` | unknown | unknown | group (same) |
| `attemptPk` | unknown | unknown | attemptPk (changed to number type) |
| `discussionId` | unknown | unknown | discussionId (changed to number type) |
| `discussionTitle` | unknown | unknown | discussionTitle (same) |
| `escalated` | unknown | unknown | escalated (same) |
| `escalationReason` | unknown | unknown | escalationReason (same) |

---

### faculty-info

**Analysis Summary:**
- Total Fields: 39
- Legacy-Only: 14
- SAAS-Only: 10
- Common: 4
- Format: standard_comparison

#### 🔴 Fields Present in Legacy but NOT in SAAS:

- **`code`** (number)
  - **Impact**: Legacy only, top-level
- **`status`** (string)
  - **Impact**: Legacy only, top-level
- **`message`** (object)
  - **Impact**: None
- **`message.oprid`** (string)
  - **Impact**: Equivalent to SAAS "loginId"
- **`message.firstName`** (string)
  - **Impact**: None
- **`message.lastName`** (string)
  - **Impact**: None
- **`message.email`** (string)
  - **Impact**: None
- **`message.globalInbox`** (array)
  - **Impact**: None
- **`message.gradebookFilterActive`** (boolean)
  - **Impact**: None
- **`message.courseActivityPilot`** (boolean)
  - **Impact**: None
- **`message.role`** (array<object>)
  - **Impact**: Each has longCourseId + role
- **`message.role[].longCourseId`** (string)
  - **Impact**: None
- **`message.role[].role`** (string)
  - **Impact**: None
- **`message.smsActive`** (boolean)
  - **Impact**: None

#### 🟢 Fields Present in SAAS but NOT in Legacy:

- **`loginId`** (string)
  - **Notes**: Legacy uses "oprid"
- **`courses`** (array<object>)
  - **Notes**: None
- **`courses[].courseId`** (string)
  - **Notes**: None
- **`courses[].role`** (string)
  - **Notes**: None
- **`allCourses`** (array<object>)
  - **Notes**: Contains course, strm, sessionCode
- **`allCourses[].courses`** (string)
  - **Notes**: None
- **`allCourses[].strm`** (string)
  - **Notes**: None
- **`allCourses[].sessionCode`** (string)
  - **Notes**: None
- **`needsGrading`** (number)
  - **Notes**: None
- **`discussionCount`** (number)
  - **Notes**: None

#### ✅ Common Fields: 4

| Field | Legacy Type | SAAS Type | Notes |
|-------|-------------|-----------|-------|
| `firstName` | string | string | No notes |
| `lastName` | string | string | No notes |
| `email` | string | string | No notes |
| `globalInbox` | array | array[string] | SAAS: array of emails, Legacy: array (empty) |

---

### faculty-templates

**Analysis Summary:**
- Total Fields: 36
- Legacy-Only: 10
- SAAS-Only: 18
- Common: 3
- Format: standard_comparison

#### 🔴 Fields Present in Legacy but NOT in SAAS:

- **`templateId`** (number)
  - **Impact**: Legacy only
- **`title`** (string)
  - **Impact**: Legacy only
- **`template`** (string)
  - **Impact**: Legacy only (SAAS: message.TEMPLATE)
- **`isDefault`** (boolean)
  - **Impact**: Legacy only (SAAS: message.IS_DEFAULT)
- **`subject`** (string/null)
  - **Impact**: Legacy only (SAAS: message.SUBJECT)
- **`content`** (string)
  - **Impact**: Legacy only (SAAS: message.CONTENT)
- **`category`** (string/null)
  - **Impact**: Legacy only (SAAS: message.CATEGORY)
- **`rowCreatedTime`** (string (datetime))
  - **Impact**: Legacy only (SAAS: message.ROW_CREATED_TIME)
- **`rowModifiedTime`** (string/null)
  - **Impact**: Legacy only (SAAS: message.ROW_MODIFIED_TIME)
- **`templateType`** (string)
  - **Impact**: Legacy only (SAAS: message.TEMPLATE_TYPE)

#### 🟢 Fields Present in SAAS but NOT in Legacy:

- **`message.ID`** (number)
  - **Notes**: SAAS only
- **`message.TITLE`** (string)
  - **Notes**: SAAS only
- **`message.CONTENT`** (string)
  - **Notes**: SAAS only
- **`message.TEMPLATE_TYPE`** (string)
  - **Notes**: SAAS only (Legacy: templateType)
- **`message.FACULTY_ID`** (string/number)
  - **Notes**: SAAS only
- **`message.SUBJECT`** (string)
  - **Notes**: SAAS only (Legacy: subject)
- **`message.CATEGORY`** (number)
  - **Notes**: SAAS only (Legacy: category, string or null)
- **`message.IS_DEFAULT`** (boolean/null)
  - **Notes**: SAAS only (Legacy: isDefault, boolean)
- **`message.TEMPLATE`** (string)
  - **Notes**: SAAS only (Legacy: template)
- **`message.ROW_CREATED_TIME`** (string (datetime))
  - **Notes**: SAAS only (Legacy: rowCreatedTime)
- **`message.ROW_MODIFIED_TIME`** (string (datetime))
  - **Notes**: SAAS only (Legacy: rowModifiedTime)
- **`message.VIDEO_ID`** (number)
  - **Notes**: SAAS only
- **`message.videoData`** (object)
  - **Notes**: SAAS only
- **`message.videoData.videoLink`** (string)
  - **Notes**: SAAS only
- **`message.videoData.dataUrl`** (string/null)
  - **Notes**: SAAS only
- **`message.videoData.videoId`** (string)
  - **Notes**: SAAS only
- **`message.videoData.imgUrl`** (string)
  - **Notes**: SAAS only
- **`message.videoData.name`** (string)
  - **Notes**: SAAS only

#### ✅ Common Fields: 3

| Field | Legacy Type | SAAS Type | Notes |
|-------|-------------|-----------|-------|
| `code` | number | number | Top-level, same |
| `status` | string | string | Top-level, same |
| `message` | array<object> | object | SAAS: single object, Legacy: array of templates |

---

### flexpath assesments

#### ℹ️ Additional Notes:

- Minimal data sheet

---

### flexpath roster

#### ℹ️ Additional Notes:

- Minimal data sheet

---

### get assignment all

#### ℹ️ Additional Notes:

- Minimal data sheet

---

### inbox

**Analysis Summary:**
- Total Fields: 29
- Legacy-Only: 11
- SAAS-Only: 12
- Common: 1
- Format: standard_comparison

#### 🔴 Fields Present in Legacy but NOT in SAAS:

- **`code`** (number)
  - **Impact**: Legacy top-level
- **`status`** (string)
  - **Impact**: Legacy top-level
- **`message`** (array<object>)
  - **Impact**: Legacy: array of messages
- **`hash`** (string)
  - **Impact**: Legacy
- **`employee_id`** (string)
  - **Impact**: Legacy
- **`first_name`** (string)
  - **Impact**: Legacy
- **`last_name`** (string)
  - **Impact**: Legacy
- **`course_id`** (string)
  - **Impact**: Legacy
- **`message`** (string)
  - **Impact**: Legacy: message text
- **`read_status`** (number)
  - **Impact**: Legacy: 1/0
- **`send_status`** (string)
  - **Impact**: Legacy

#### 🟢 Fields Present in SAAS but NOT in Legacy:

- **`studentHash`** (string)
  - **Notes**: SAAS
- **`firstName`** (string)
  - **Notes**: SAAS
- **`lastName`** (string)
  - **Notes**: SAAS
- **`email`** (string)
  - **Notes**: SAAS
- **`phone`** (string)
  - **Notes**: SAAS
- **`body`** (string)
  - **Notes**: SAAS
- **`readStatus`** (boolean)
  - **Notes**: SAAS
- **`sendStatus`** (string)
  - **Notes**: SAAS
- **`messageType`** (string)
  - **Notes**: SAAS
- **`inbox`** (number)
  - **Notes**: SAAS
- **`unreadCount`** (number)
  - **Notes**: SAAS
- **`rank`** (number)
  - **Notes**: SAAS

#### ✅ Common Fields: 1

| Field | Legacy Type | SAAS Type | Notes |
|-------|-------------|-----------|-------|
| `timestamp` | string | string | ISO format in both |

---

### instructor config

#### ℹ️ Additional Notes:

- Minimal data sheet

---

### messages-course-messages

**Analysis Summary:**
- Total Fields: 16
- Legacy-Only: 6
- SAAS-Only: 2
- Common: 4
- Format: standard_comparison

#### 🔴 Fields Present in Legacy but NOT in SAAS:

- **`messageSummary[].unreadMessages`** (number)
  - **Impact**: Legacy only; count of unread messages
- **`messageSummary[].courseId`** (string)
  - **Impact**: Legacy only
- **`messageSummary[].coursePk`** (string)
  - **Impact**: Legacy only
- **`code`** (number)
  - **Impact**: Legacy only, top-level
- **`status`** (string)
  - **Impact**: Legacy only, top-level
- **`message`** (object)
  - **Impact**: Legacy only; wrapper for the above fields

#### 🟢 Fields Present in SAAS but NOT in Legacy:

- **`messageSummary[].newPosts`** (number)
  - **Notes**: SAAS only; count of new posts
- **`messageSummary[].replies`** (number)
  - **Notes**: SAAS only; count of replies

#### ✅ Common Fields: 4

| Field | Legacy Type | SAAS Type | Notes |
|-------|-------------|-----------|-------|
| `totalUnreadMessages` | number | number | Top-level; same meaning and type |
| `messageSummary` | array<object> | array<object> | Top-level; structure differs |
| `messageSummary[].link` | string | string | Common; URL format slightly differs |
| `messageSummary[].courseName` | string | string | Common |

---

### my-media

**Analysis Summary:**
- Total Fields: 85
- Legacy-Only: 4
- SAAS-Only: 3
- Common: 68
- Format: standard_comparison

#### 🔴 Fields Present in Legacy but NOT in SAAS:

- **`message`** (object)
  - **Impact**: Only Legacy, wrapper for objects
- **`relatedObjects`** (object/null)
  - **Impact**: Only Legacy, inside message
- **`startDate`** (None)
  - **Impact**: Legacy only
- **`endDate`** (None)
  - **Impact**: Legacy only

#### 🟢 Fields Present in SAAS but NOT in Legacy:

- **`startDt`** (None)
  - **Notes**: SAAS only
- **`endDt`** (None)
  - **Notes**: SAAS only
- **`embedUrl`** (string)
  - **Notes**: SAAS only

#### ✅ Common Fields: 68

*Common fields list is large. See detailed data for complete information.*

---

### needs grading

**Analysis Summary:**
- Total Fields: 7
- Legacy-Only: 4
- SAAS-Only: 3
- Common: 0
- Format: standard_comparison

#### 🔴 Fields Present in Legacy but NOT in SAAS:

- **`assignment.employeeId`** (string)
  - **Impact**: None
- **`assignment.learnerPk`** (string)
  - **Impact**: None
- **`assignment.coursePk`** (string)
  - **Impact**: None
- **`assignment.group`** (string)
  - **Impact**: Equivalent to SAAS gradeGroup

#### 🟢 Fields Present in SAAS but NOT in Legacy:

- **`assignment.studentHash`** (string)
  - **Notes**: None
- **`assignment.gradeGroup`** (string)
  - **Notes**: None
- **`assignment.attempts[].status`** (string)
  - **Notes**: Attempt‐level status present only in SAAS

---

### notification

#### ℹ️ Additional Notes:

- Minimal data sheet

---

### templates

#### ℹ️ Additional Notes:

- Minimal data sheet

---
