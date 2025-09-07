# messages-sms-inbox API Analysis
**Legacy vs SaaS Comparison**

## Executive Summary

- **12 new fields** added in SaaS
- **4 fields** removed from Legacy (missing in SaaS)
- **4 potential field renames** detected

## Overview
| Metric | Legacy | SaaS | Change |
|--------|--------|------|--------|
| Total Fields | 5 | 13 | +8 |
| New Fields | - | 12 | +12 |
| Removed Fields | 4 | - | -4 |
| Common Fields | 1 | 1 | 0 |
| Type Changes | - | 0 | 0 |

## 🆕 New Fields Added in SaaS
These fields are present in SaaS but not in Legacy:

| Field Name | Type | Notes |
|------------|------|-------|
| `[0].body` | str | New functionality |
| `[0].email` | str | New functionality |
| `[0].firstName` | str | New functionality |
| `[0].inbox` | int | New functionality |
| `[0].lastName` | str | New functionality |
| `[0].messageType` | str | New functionality |
| `[0].phone` | str | New functionality |
| `[0].rank` | int | New functionality |
| `[0].readStatus` | bool | New functionality |
| `[0].sendStatus` | str | New functionality |
| `[0].studentHash` | str | New functionality |
| `[0].unreadCount` | int | New functionality |

## ❌ Fields Removed from Legacy
These fields were present in Legacy but are missing in SaaS:

| Field Name | Type | Impact |
|------------|------|--------|
| `[0].hash` | str | Functionality removed/changed |
| `[0].message` | str | Functionality removed/changed |
| `[0].read_status` | int | Functionality removed/changed |
| `[0].send_status` | str | Functionality removed/changed |

## 🏷️ Potential Field Renames
These appear to be renamed fields (similar names/types):

| Legacy Field | SaaS Field | Legacy Type | SaaS Type | Confidence |
|--------------|------------|-------------|-----------|------------|
| `[0].hash` | `[0].studentHash` | str | str | High |
| `[0].send_status` | `[0].sendStatus` | str | str | High |
| `[0].message` | `[0].messageType` | str | str | High |
| `[0].read_status` | `[0].readStatus` | int | bool | Medium |

## Sample Data Structure

### Legacy Sample
```json
[
  {
    "read_status": 1,
    "send_status": "ACCEPTED",
    "message": "<p>Test FAC</p>",
    "hash": "S21yMzNja2RMZEI5MFlWRXVSNThyZz09Ojr5wT6mfwBuoixC6XD19M91",
    "timestamp": "2020-09-15T20:50:33+00:00"
  }
]
```

### SaaS Sample
```json
[
  {
    "studentHash": "ZGI1N2MwMDgtMzliMC00MGZlLTg5ZTMtMjFhMjQyYWJiOWQ2::YjgwN2QwYzgtMGM4ZC00YWQyLTlhYTktZjRjNzYyNTNjYTQ0",
    "firstName": "Vinnie",
    "lastName": "Runolfsdottir",
    "email": "Vinnie_Runolfsdottir23@nonprod.strategiced.com",
    "phone": "+16693605432",
    "body": "Hello Vinnie,\nTametsi cursim deduco vulgivagus antiquus.\nSincerely,\nMateo",
    "readStatus": false,
    "sendStatus": "FAILED",
    "messageType": "I",
    "inbox": 1,
    "unreadCount": 2,
    "timestamp": "2025-05-25T21:59:34.266Z",
    "rank": 1
  },
  {
    "studentHash": "NTZlZDVkMDMtNjg1Yy00YmRjLWEyMWUtODVkOGM0YTFiMWJm::ZjFlY2ZlZGItYzg3MC00Y2ZiLThmNTItNDkxYmU4ZjlkYzZl",
    "firstName": "Nils",
    "lastName": "Rempel",
    "email": "Nils_Rempel@nonprod.strategiced.com",
    "phone": "+13137116533",
    "body": "Hello Nils,\nAsper culpo aequus thalassinus.\nSincerely,\nMaymie",
    "readStatus": true,
    "sendStatus": "FAILED",
    "messageType": "I",
    "inbox": 0,
    "unreadCount": 0,...
```

## Recommendations

1. **Review new fields**: 12 new fields have been added. Ensure consuming applications can handle these additions.
2. **Handle removed fields**: 4 fields are no longer available. Update consuming applications accordingly.
4. **Verify renames**: 4 potential field renames detected. Confirm these are intentional changes.
