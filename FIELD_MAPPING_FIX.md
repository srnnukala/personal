# Field Mapping Fix for API Comparison Tool

## Issue Fixed

**Problem**: In the course-activity-overview API comparison, the tool was incorrectly comparing fields from different logical paths:
- `[0].activityScoreTrend` (SAAS) was being treated as a separate field from `message[0].activityScoreTrend` (Legacy)
- This caused incorrect field mapping where inner fields were not properly matched between SAAS and Legacy responses

## Root Cause

The original field path extraction logic created different path names for the same logical fields when the response structures had different wrapper objects:

- **SAAS structure**: Direct array `[0].fieldName`
- **Legacy structure**: Wrapped in message object `message[0].fieldName`

## Solution Implemented

Added smart field normalization logic to the `APIComparisonAnalyzer` class:

1. **New Method**: `normalize_field_path()` - Removes common wrapper prefixes to create normalized paths for comparison
2. **Updated Logic**: `analyze_api_differences()` now uses normalized paths for matching while preserving original paths for display
3. **Wrapper Filtering**: Automatically ignores wrapper fields (`code`, `status`, `message`) as requested

## Changes Made

### Added `normalize_field_path()` method:
```python
def normalize_field_path(self, field_path: str) -> str:
    """Normalize field paths by removing common wrapper prefixes like 'message[0]' -> '[0]'"""
    if field_path.startswith('message[0].'):
        return field_path.replace('message[0].', '[0].')
    elif field_path == 'message[0]':
        return '[0]'
    elif field_path.startswith('message.'):
        return field_path.replace('message.', '')
    elif field_path == 'message':
        return 'root_array'
    return field_path
```

### Updated `analyze_api_differences()` method:
- Creates normalized path mappings for both SAAS and Legacy
- Matches fields based on normalized paths instead of literal paths
- Filters out wrapper fields (`code`, `status`, `message`)
- Uses original paths for display while using normalized paths for comparison logic

## Results

### Before the Fix:
```
Field: [0].activityScore
  SAAS: Yes (string)
  Legacy: No ()
  Notes: Field only exists in SAAS

Field: message[0].activityScore  
  SAAS: No ()
  Legacy: Yes (string)
  Notes: Field only exists in Legacy
```

### After the Fix:
```
Field: message[0].activityScore
  SAAS: Yes (string)
  Legacy: Yes (string)
  Notes: String values differ between systems

Field: message[0].activityScoreTrend
  SAAS: Yes (integer)
  Legacy: Yes (integer)
  Notes: Numeric values differ between systems
```

## Validation

✅ **Test Results**: All tests pass
- Inner fields are properly matched between SAAS and Legacy
- Wrapper fields are correctly ignored
- Other APIs continue to work without issues
- Original field mapping issue is resolved

## Impact

- **Fixed**: course-activity-overview field mapping
- **Improved**: All APIs with similar wrapper structure differences
- **Maintained**: Backward compatibility with existing comparisons
- **Added**: Better field matching logic for future API comparisons

This fix ensures that equivalent inner fields are properly compared regardless of their wrapper structure differences, providing more accurate API comparison results.