# API Field Comparison Analysis: Legacy vs SAAS
Generated on: 2025-09-03 19:30:34

## Executive Summary

- **Total API Endpoints Analyzed**: 18
- **Total Fields Only in Legacy**: 8
- **Total Fields Only in SAAS**: 0
- **Total Common Fields**: 0

## Table of Contents

1. [ roster drops](#-roster-drops)
2. [ roster enrollments](#-roster-enrollments)
3. [ submit-grades grade-details](#-submit-grades-grade-details)
4. [ask-instructor](#ask-instructor)
5. [courseactivity overview](#courseactivity-overview)
6. [discussion](#discussion)
7. [faculty-info](#faculty-info)
8. [faculty-templates](#faculty-templates)
9. [flexpath assesments](#flexpath-assesments)
10. [flexpath roster](#flexpath-roster)
11. [get assignment all](#get-assignment-all)
12. [inbox](#inbox)
13. [instructor config](#instructor-config)
14. [messages-course-messages](#messages-course-messages)
15. [my-media](#my-media)
16. [needs grading](#needs-grading)
17. [notification](#notification)
18. [templates](#templates)

## Summary: Fields Present in Legacy but NOT in SAAS

| Endpoint | Legacy-Only Field | Notes |
|----------|-------------------|-------|
|  roster drops | code | Missing in SaaS |
|  roster drops | status | Missing in SaaS |
|  roster drops | message | Missing in SaaS |
|  roster drops | courseId | Missing in SaaS |
|  roster drops | coursePk | Missing in SaaS |
|  roster drops | learnerPk | Missing in SaaS |
|  roster drops | employeeID | Missing in SaaS |
|  roster drops | emailId | Missing in SaaS |

## Detailed Analysis by Endpoint

###  roster drops

**Total Fields Analyzed**: 15
**Legacy-Only Fields**: 8
**SAAS-Only Fields**: 0
**Common Fields**: 0

#### Fields Present in Legacy but NOT in SAAS:

- **code** (Unknown type)
  - Notes: Missing in SaaS
- **status** (Unknown type)
  - Notes: Missing in SaaS
- **message** (Unknown type)
  - Notes: Missing in SaaS
- **courseId** (Unknown type)
  - Notes: Missing in SaaS
- **coursePk** (Unknown type)
  - Notes: Missing in SaaS
- **learnerPk** (Unknown type)
  - Notes: Missing in SaaS
- **employeeID** (Unknown type)
  - Notes: Missing in SaaS
- **emailId** (Unknown type)
  - Notes: Missing in SaaS

---

###  roster enrollments

**Total Fields Analyzed**: 25
**Legacy-Only Fields**: 0
**SAAS-Only Fields**: 0
**Common Fields**: 0

---

###  submit-grades grade-details

#### Additional Notes:

- Single column sheet with minimal data: /submit-grades/grade-details

---

### ask-instructor

#### Additional Notes:

- Non-standard format detected. Columns: ['/ask-instructor', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5']

---

### courseactivity overview

#### Additional Notes:

- Single column sheet with minimal data: /course-activity/overview

---

### discussion

#### Additional Notes:

- Non-standard format detected. Columns: ['/gradebook/discussions/replies/hidden/false', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3']

---

### faculty-info

#### Additional Notes:

- Non-standard format detected. Columns: ['/faculty-info', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5']

---

### faculty-templates

#### Additional Notes:

- Non-standard format detected. Columns: ['/templates/faculty-templates', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5']

---

### flexpath assesments

#### Additional Notes:

- Single column sheet with minimal data: /flexpath/assignments

---

### flexpath roster

#### Additional Notes:

- Single column sheet with minimal data: flexpath/enrollments

---

### get assignment all

#### Additional Notes:

- Single column sheet with minimal data: /gradebook/assignments/all

---

### inbox

#### Additional Notes:

- Non-standard format detected. Columns: ['/sms/inbox', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5']

---

### instructor config

#### Additional Notes:

- Single column sheet with minimal data: instructor /config

---

### messages-course-messages

#### Additional Notes:

- Non-standard format detected. Columns: ['messages/course-message', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5']

---

### my-media

#### Additional Notes:

- Non-standard format detected. Columns: ['/video/my-media', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5']

---

### needs grading

#### Additional Notes:

- Non-standard format detected. Columns: ['/needs-grading', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5']

---

### notification

#### Additional Notes:

- Single column sheet with minimal data: /notification

---

### templates

#### Additional Notes:

- Single column sheet with minimal data: templates/{{type}}/{{id}}

---
