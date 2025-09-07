# messages-notification API Analysis
**Legacy vs SaaS Comparison**

## Executive Summary

- **1 new fields** added in SaaS
- **12 fields** removed from Legacy (missing in SaaS)
- **1 potential field renames** detected

## Overview
| Metric | Legacy | SaaS | Change |
|--------|--------|------|--------|
| Total Fields | 12 | 1 | -11 |
| New Fields | - | 1 | +1 |
| Removed Fields | 12 | - | -12 |
| Common Fields | 0 | 0 | 0 |
| Type Changes | - | 0 | 0 |

## 🆕 New Fields Added in SaaS
These fields are present in SaaS but not in Legacy:

| Field Name | Type | Notes |
|------------|------|-------|
| `message` | str | New functionality |

## ❌ Fields Removed from Legacy
These fields were present in Legacy but are missing in SaaS:

| Field Name | Type | Impact |
|------------|------|--------|
| `notifications` | list | Functionality removed/changed |
| `notificationsTotalLength` | int | Functionality removed/changed |
| `notifications[0].notificationActive` | bool | Functionality removed/changed |
| `notifications[0].notificationEnd` | str | Functionality removed/changed |
| `notifications[0].notificationId` | str | Functionality removed/changed |
| `notifications[0].notificationLinkText` | str | Functionality removed/changed |
| `notifications[0].notificationLinkUrl` | str | Functionality removed/changed |
| `notifications[0].notificationMessage` | str | Functionality removed/changed |
| `notifications[0].notificationRemoved` | str | Functionality removed/changed |
| `notifications[0].notificationStart` | str | Functionality removed/changed |
| `notifications[0].notificationTitle` | str | Functionality removed/changed |
| `notifications[0].notificationType` | str | Functionality removed/changed |

## 🏷️ Potential Field Renames
These appear to be renamed fields (similar names/types):

| Legacy Field | SaaS Field | Legacy Type | SaaS Type | Confidence |
|--------------|------------|-------------|-----------|------------|
| `notifications[0].notificationMessage` | `message` | str | str | High |

## Sample Data Structure

### Legacy Sample
```json
{
  "notificationsTotalLength": 1,
  "notifications": [
    {
      "notificationId": "3041",
      "notificationType": "none",
      "notificationTitle": "The quick brown fox jumped over the lazy dog.",
      "notificationMessage": "Sound is transmitted through gases, plasma, and liquids as longitudinal waves, also called compression waves. It requires a medium to propagate. Through solids, however, it can be transmitted as both longitudinal waves and transverse waves. Longitudinal  @link are waves of alternating pressure deviations from the equilibrium pressure, causing local regions of compression and rarefaction, while transverse waves (in solids) are waves of alternating shear stress at right angle to the direction of propagation.",
      "notificationLinkText": "sound waves",
      "notificationLinkUrl": "https://en.wikipedia.org/wiki/Sound#Waves",
      "notificationStart": "2022-09-23 08:30:00",
      "notificationEnd": "2022-09-29 09:45:00",
      "notificationRemoved": "",
  ...
```

### SaaS Sample
```json
{
  "message": "missing api response"
}
```

## Recommendations

1. **Review new fields**: 1 new fields have been added. Ensure consuming applications can handle these additions.
2. **Handle removed fields**: 12 fields are no longer available. Update consuming applications accordingly.
4. **Verify renames**: 1 potential field renames detected. Confirm these are intentional changes.
