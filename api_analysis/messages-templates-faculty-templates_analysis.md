# messages-templates-faculty-templates API Analysis
**Legacy vs SaaS Comparison**

## Executive Summary

- **10 new fields** added in SaaS
- **12 fields** removed from Legacy (missing in SaaS)
- **13 potential field renames** detected

## Overview
| Metric | Legacy | SaaS | Change |
|--------|--------|------|--------|
| Total Fields | 12 | 10 | -2 |
| New Fields | - | 10 | +10 |
| Removed Fields | 12 | - | -12 |
| Common Fields | 0 | 0 | 0 |
| Type Changes | - | 0 | 0 |

## 🆕 New Fields Added in SaaS
These fields are present in SaaS but not in Legacy:

| Field Name | Type | Notes |
|------------|------|-------|
| `[0].category` | str | New functionality |
| `[0].content` | str | New functionality |
| `[0].isDefault` | bool | New functionality |
| `[0].rowCreatedTime` | str | New functionality |
| `[0].rowModifiedTime` | str | New functionality |
| `[0].subject` | str | New functionality |
| `[0].template` | str | New functionality |
| `[0].templateId` | int | New functionality |
| `[0].templateType` | str | New functionality |
| `[0].title` | str | New functionality |

## ❌ Fields Removed from Legacy
These fields were present in Legacy but are missing in SaaS:

| Field Name | Type | Impact |
|------------|------|--------|
| `[0].CATEGORY` | NoneType | Functionality removed/changed |
| `[0].CONTENT` | str | Functionality removed/changed |
| `[0].FACULTY_ID` | str | Functionality removed/changed |
| `[0].ID` | int | Functionality removed/changed |
| `[0].IS_DEFAULT` | int | Functionality removed/changed |
| `[0].ROW_CREATED_TIME` | str | Functionality removed/changed |
| `[0].ROW_MODIFIED_TIME` | str | Functionality removed/changed |
| `[0].SUBJECT` | NoneType | Functionality removed/changed |
| `[0].TEMPLATE` | str | Functionality removed/changed |
| `[0].TEMPLATE_TYPE` | str | Functionality removed/changed |
| `[0].TITLE` | str | Functionality removed/changed |
| `[0].VIDEO_ID` | NoneType | Functionality removed/changed |

## 🏷️ Potential Field Renames
These appear to be renamed fields (similar names/types):

| Legacy Field | SaaS Field | Legacy Type | SaaS Type | Confidence |
|--------------|------------|-------------|-----------|------------|
| `[0].TEMPLATE` | `[0].templateId` | str | int | Medium |
| `[0].TEMPLATE` | `[0].template` | str | str | High |
| `[0].TEMPLATE` | `[0].templateType` | str | str | High |
| `[0].ROW_MODIFIED_TIME` | `[0].rowModifiedTime` | str | str | High |
| `[0].SUBJECT` | `[0].subject` | NoneType | str | Medium |
| `[0].TEMPLATE_TYPE` | `[0].template` | str | str | High |
| `[0].TEMPLATE_TYPE` | `[0].templateType` | str | str | High |
| `[0].IS_DEFAULT` | `[0].isDefault` | int | bool | Medium |
| `[0].TITLE` | `[0].title` | str | str | High |
| `[0].ROW_CREATED_TIME` | `[0].rowCreatedTime` | str | str | High |
| `[0].ID` | `[0].templateId` | int | int | High |
| `[0].CONTENT` | `[0].content` | str | str | High |
| `[0].CATEGORY` | `[0].category` | NoneType | str | Medium |

## Sample Data Structure

### Legacy Sample
```json
[
  {
    "ID": 1126,
    "TITLE": "signature 1",
    "TEMPLATE": "signature",
    "CONTENT": "<p>Default Signature</p><p>Nagamani</p>",
    "TEMPLATE_TYPE": "Email Signature",
    "FACULTY_ID": "1000233",
    "IS_DEFAULT": 0,
    "SUBJECT": null,
    "CATEGORY": null,
    "VIDEO_ID": null,
    "ROW_CREATED_TIME": "2024-01-29 10:51:47",
    "ROW_MODIFIED_TIME": "2024-03-15 12:04:28"
  },
  {
    "ID": 1240,
    "TITLE": "Email signature1",
    "TEMPLATE": "signature",
    "CONTENT": "<p>Sincerely,</p><p><span class=\"placeholders\">@myName</span></p>",
    "TEMPLATE_TYPE": "Email Signature",
    "FACULTY_ID": "1000233",
    "IS_DEFAULT": 0,
    "SUBJECT": null,
    "CATEGORY": null,
    "VIDEO_ID": null,
    "ROW_CREATED_TIME": "2024-03-15 12:00:14",
    "ROW_MODIFIED_TIME": "2024-03-15 12:04:28"
  }
]
```

### SaaS Sample
```json
[
  {
    "templateId": 100,
    "title": "cupiditate cura",
    "template": "email",
    "isDefault": false,
    "subject": "Culpo traho alter caritas.",
    "content": "<p>Calcar theca civitas. Correptius attonbitus vomito ipsa credo tyrannus trans absconditus adsidue cariosus. Depereo tergiversatio caries iure animus advenio vis aliquid arx.\nCommemoro tabgo pauper termes celer tergeo sordeo tonsor adeptio considero. Quo impedit solutio sol. Voluptates turba usitas clarus inflammatio verecundia trucido torrens.\nVomer thalassinus mollitia tollo charisma verto color. Natus studio debeo. Adduco ustilo aduro laboriosam distinctio stipes.</p><p>Sincerely,</p><p><span class=\"placeholders\" data-type=\"placeholders\" data-id=\"myName\">Test</span></p>",
    "category": "12",
    "rowCreatedTime": "2025-07-13T07:25:42.489Z",
    "rowModifiedTime": "2025-07-12T09:23:42.708Z",
    "templateType": "Email Template"
  },
  {
    "templateId": 101,
    "title": "aut similique abutor",
    "temp...
```

## Recommendations

1. **Review new fields**: 10 new fields have been added. Ensure consuming applications can handle these additions.
2. **Handle removed fields**: 12 fields are no longer available. Update consuming applications accordingly.
4. **Verify renames**: 13 potential field renames detected. Confirm these are intentional changes.
