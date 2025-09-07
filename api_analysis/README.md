# API Comparison Analysis Index

This directory contains detailed analysis for each API endpoint comparing Legacy and SaaS implementations.

## Summary Overview

| API Endpoint | New Fields | Removed Fields | Renames | Type Changes | Analysis File |
|--------------|------------|----------------|---------|--------------|---------------|
| ✅ course-activity | 0 | 0 | 0 | 0 | [course-activity_analysis.md](./course-activity_analysis.md) |
| ⚠️ discussion | 4 | 5 | 2 | 5 | [discussion_analysis.md](./discussion_analysis.md) |
| ⚠️ faculty-info-cu | 2 | 1 | 0 | 0 | [faculty-info-cu_analysis.md](./faculty-info-cu_analysis.md) |
| ⚠️ gradebook-assigments-all | 16 | 24 | 42 | 0 | [gradebook-assigments-all_analysis.md](./gradebook-assigments-all_analysis.md) |
| ⚠️ gradebook-export-status | 4 | 8 | 4 | 1 | [gradebook-export-status_analysis.md](./gradebook-export-status_analysis.md) |
| ⚠️ instructor-config | 150 | 1 | 0 | 0 | [instructor-config_analysis.md](./instructor-config_analysis.md) |
| ⚠️ kaltura-video-my-media | 5 | 1 | 0 | 14 | [kaltura-video-my-media_analysis.md](./kaltura-video-my-media_analysis.md) |
| ⚠️ messages-ask-instructor | 0 | 2 | 0 | 0 | [messages-ask-instructor_analysis.md](./messages-ask-instructor_analysis.md) |
| ⚠️ messages-course-message | 2 | 3 | 0 | 0 | [messages-course-message_analysis.md](./messages-course-message_analysis.md) |
| ⚠️ messages-notification | 1 | 12 | 1 | 0 | [messages-notification_analysis.md](./messages-notification_analysis.md) |
| ⚠️ messages-sms-inbox | 12 | 4 | 4 | 0 | [messages-sms-inbox_analysis.md](./messages-sms-inbox_analysis.md) |
| ✅ messages-template-by-id | 0 | 0 | 0 | 0 | [messages-template-by-id_analysis.md](./messages-template-by-id_analysis.md) |
| ⚠️ messages-templates-faculty-templates | 10 | 12 | 13 | 0 | [messages-templates-faculty-templates_analysis.md](./messages-templates-faculty-templates_analysis.md) |
| ⚠️ needs-grading-cu | 15 | 17 | 13 | 0 | [needs-grading-cu_analysis.md](./needs-grading-cu_analysis.md) |
| ⚠️ needs-grading-su | 15 | 17 | 13 | 0 | [needs-grading-su_analysis.md](./needs-grading-su_analysis.md) |
| ⚠️ roster-drops | 5 | 11 | 3 | 0 | [roster-drops_analysis.md](./roster-drops_analysis.md) |
| ⚠️ roster-enrollments-cu | 52 | 18 | 7 | 4 | [roster-enrollments-cu_analysis.md](./roster-enrollments-cu_analysis.md) |
| ⚠️ roster-enrollments-flexpath | 52 | 18 | 7 | 4 | [roster-enrollments-flexpath_analysis.md](./roster-enrollments-flexpath_analysis.md) |
| ⚠️ roster-enrollments-su | 50 | 21 | 9 | 6 | [roster-enrollments-su_analysis.md](./roster-enrollments-su_analysis.md) |
| ⚠️ submit-grades-grade-details | 7 | 1 | 0 | 0 | [submit-grades-grade-details_analysis.md](./submit-grades-grade-details_analysis.md) |
| ⚠️ submit-grades-{{exam}}-course-sis-id-{{course-sis-id}} | 7 | 7 | 5 | 0 | [submit-grades-exam-course-sis-id-course-sis-id_analysis.md](./submit-grades-exam-course-sis-id-course-sis-id_analysis.md) |
| **TOTALS** | **409** | **183** | **123** | **34** | - |

## Key Findings

- **409** total new fields added across all APIs
- **183** total fields removed from Legacy
- **123** potential field renames detected
- **34** fields with type changes

## APIs with Significant Changes

- **instructor-config**: 151 total changes
- **roster-enrollments-su**: 77 total changes
- **roster-enrollments-cu**: 74 total changes
- **roster-enrollments-flexpath**: 74 total changes
- **gradebook-assigments-all**: 40 total changes
- **needs-grading-cu**: 32 total changes
- **needs-grading-su**: 32 total changes
- **messages-templates-faculty-templates**: 22 total changes
- **kaltura-video-my-media**: 20 total changes
- **messages-sms-inbox**: 16 total changes
- **roster-drops**: 16 total changes
- **discussion**: 14 total changes
- **submit-grades-{{exam}}-course-sis-id-{{course-sis-id}}**: 14 total changes
- **gradebook-export-status**: 13 total changes
- **messages-notification**: 13 total changes
