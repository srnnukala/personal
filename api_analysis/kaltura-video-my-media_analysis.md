# kaltura-video-my-media API Analysis
**Legacy vs SaaS Comparison**

## Executive Summary

- **5 new fields** added in SaaS
- **1 fields** removed from Legacy (missing in SaaS)
- **14 fields** have type changes

## Overview
| Metric | Legacy | SaaS | Change |
|--------|--------|------|--------|
| Total Fields | 69 | 73 | +4 |
| New Fields | - | 5 | +5 |
| Removed Fields | 1 | - | -1 |
| Common Fields | 68 | 68 | 0 |
| Type Changes | - | 14 | 14 |

## 🆕 New Fields Added in SaaS
These fields are present in SaaS but not in Legacy:

| Field Name | Type | Notes |
|------------|------|-------|
| `objects[0].application` | NoneType | New functionality |
| `objects[0].applicationVersion` | NoneType | New functionality |
| `objects[0].blockAutoTranscript` | NoneType | New functionality |
| `objects[0].embedUrl` | str | New functionality |
| `objects[0].sourceVersion` | NoneType | New functionality |

## ❌ Fields Removed from Legacy
These fields were present in Legacy but are missing in SaaS:

| Field Name | Type | Impact |
|------------|------|--------|
| `relatedObjects` | NoneType | Functionality removed/changed |

## 🔄 Fields with Type Changes
These fields exist in both but have different data types:

| Field Name | Legacy Type | SaaS Type | Impact |
|------------|-------------|-----------|--------|
| `objects[0].licenseType` | int | str | ⚠️ Breaking change |
| `objects[0].groupId` | str | NoneType | ⚠️ Breaking change |
| `objects[0].durationType` | NoneType | int | ⚠️ Breaking change |
| `objects[0].partnerData` | str | NoneType | ⚠️ Breaking change |
| `objects[0].description` | NoneType | str | ⚠️ Breaking change |
| `objects[0].type` | int | str | ⚠️ Breaking change |
| `objects[0].status` | int | str | ⚠️ Breaking change |
| `objects[0].lastPlayedAt` | int | NoneType | ⚠️ Breaking change |
| `objects[0].creditUserName` | str | NoneType | ⚠️ Breaking change |
| `objects[0].conversionQuality` | int | str | ⚠️ Breaking change |
| `objects[0].displayInSearch` | int | str | ⚠️ Breaking change |
| `objects[0].templateEntryId` | NoneType | str | ⚠️ Breaking change |
| `objects[0].creditUrl` | str | NoneType | ⚠️ Breaking change |
| `objects[0].replacementStatus` | int | str | ⚠️ Breaking change |

## Sample Data Structure

### Legacy Sample
```json
{
  "objects": [
    {
      "mediaType": 1,
      "conversionQuality": 4192722,
      "sourceType": "2",
      "searchProviderType": null,
      "searchProviderId": null,
      "creditUserName": "",
      "creditUrl": "",
      "mediaDate": null,
      "dataUrl": "http://cdnapi.kaltura.com/p/1650501/sp/165050100/playManifest/entryId/0_07bmuh5i/format/url/protocol/http",
      "flavorParamsIds": "0,487041,487051,487061",
      "isTrimDisabled": null,
      "streams": null,
      "plays": 1,
      "views": 1,
      "lastPlayedAt": 1469710800,
      "width": 480,
      "height": 360,
      "duration": 14,
      "msDuration": 13519,
      "durationType": null,
      "id": "0_07bmuh5i",
      "name": "Blackboard_KAF_Prod>site>channels>006297_1_1165_1_01>InContextBlackboard_KAF_Prod>site>channels>006297_1_1165_1_01>InContextBlackboard_KAF_Prod>site>channels>006297_1_1165_1_01>InContextBlackboard_KAF_Prod>site>channels>006297_1_1165_1_01>InContextBlackboard_KAF_Prod>site>channels>006297_1_11...
```

### SaaS Sample
```json
{
  "objects": [
    {
      "mediaType": 1,
      "conversionQuality": "8804061",
      "sourceType": "1",
      "searchProviderType": null,
      "searchProviderId": null,
      "creditUserName": null,
      "creditUrl": null,
      "mediaDate": null,
      "dataUrl": "https://cdnapisec.kaltura.com/p/1650501/sp/165050100/playManifest/entryId/1_egv1hkxp/format/url/protocol/https",
      "flavorParamsIds": "0,487051,487111",
      "isTrimDisabled": null,
      "streams": null,
      "plays": 0,
      "views": 1,
      "lastPlayedAt": null,
      "width": 640,
      "height": 480,
      "duration": 2,
      "msDuration": 2133,
      "durationType": 2,
      "id": "1_egv1hkxp",
      "name": "a",
      "description": "",
      "partnerId": 1650501,
      "userId": "MAHMOUD.ELHARAZI",
      "creatorId": "MAHMOUD.ELHARAZI",
      "tags": "captions",
      "adminTags": null,
      "categories": "REV",
      "categoriesIds": "73307661",
      "status": "2",
      "moderationStatus": 6,
     ...
```

## Recommendations

1. **Review new fields**: 5 new fields have been added. Ensure consuming applications can handle these additions.
2. **Handle removed fields**: 1 fields are no longer available. Update consuming applications accordingly.
3. **Address type changes**: 14 fields have changed types. This may require data parsing updates.
