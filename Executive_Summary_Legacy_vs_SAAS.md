# Executive Summary: Legacy vs SAAS API Field Analysis

**Analysis Date**: September 3, 2025  
**Analyst**: API Comparison Analysis Tool  
**Objective**: Identify fields present in Legacy APIs but missing in SAAS APIs

## 🎯 Key Findings

### Critical Statistics
- **64 fields** exist in Legacy but are **NOT available in SAAS**
- **48 fields** are new in SAAS (not in Legacy)
- **96 fields** are common between both systems
- **18 API endpoints** analyzed across the system

## 🔴 CRITICAL IMPACT: Legacy-Only Fields

### Summary by Impact Level

#### **HIGH IMPACT** - Identity & Reference Fields (14 fields)
These fields are essential for data linking and system integration:

| Field | Endpoint | Impact | Recommended Action |
|-------|----------|---------|-------------------|
| `coursePk` | discussion, needs grading, ask-instructor, messages, roster drops | **CRITICAL** - Primary key for course linkage | Must establish mapping table or use alternative identifiers |
| `courseId` | discussion, ask-instructor, messages, roster drops | **CRITICAL** - Human-readable course identifier | Consider using SAAS course identifiers or maintain mapping |
| `employeeId` / `employeeID` | needs grading, roster drops | **HIGH** - Faculty identification | Map to SAAS `studentHash` or equivalent identifier |
| `learnerPk` | needs grading, roster drops | **HIGH** - Student primary key | Map to SAAS student identification system |
| `longCourseId` | faculty-info | **MEDIUM** - Extended course identifier | May be derivable from SAAS course data |

#### **MEDIUM IMPACT** - System Metadata Fields (15 fields)
These provide system-level information and status:

| Field Category | Count | Examples | Recommended Action |
|----------------|-------|----------|-------------------|
| Response wrappers | 8 | `code`, `status`, `message` objects | Implement in SAAS response structure or handle in client |
| User preferences | 4 | `gradebookFilterActive`, `courseActivityPilot`, `smsActive` | Migrate to SAAS user preference system |
| Timestamps | 3 | `rowCreatedTime`, `rowModifiedTime` | Use SAAS equivalent timestamp fields |

#### **LOW IMPACT** - Template & Content Fields (35 fields)
Legacy template structure differs significantly from SAAS:

- **Legacy Structure**: Flat field structure (`templateId`, `title`, `content`, etc.)
- **SAAS Structure**: Nested under `message` object (`message.ID`, `message.TITLE`, etc.)
- **Assessment**: These are **like-for-like replacements** with structural differences only

## 🎯 Recommendations & Action Plan

### Immediate Actions Required

1. **Data Migration Strategy**
   - Create mapping tables for `coursePk` ↔ SAAS course identifiers
   - Establish `employeeId` ↔ SAAS faculty identifiers mapping
   - Design `learnerPk` ↔ SAAS student identifiers conversion

2. **API Response Standardization**
   - Decide whether to maintain Legacy-style response wrappers (`code`, `status`, `message`)
   - Consider implementing these in SAAS for backward compatibility

3. **User Preference Migration**
   - Map Legacy user preferences to SAAS user settings system
   - Ensure features like `gradebookFilterActive` have SAAS equivalents

### Medium-term Considerations

1. **Template System Harmonization**
   - Legacy and SAAS have equivalent template data but different structures
   - Consider API wrapper to present Legacy-compatible format if needed

2. **Audit and Logging**
   - Legacy tracking fields like `rowCreatedTime` may need SAAS equivalents
   - Ensure audit trails are maintained during migration

### Low-risk Items (No Action Required)

1. **Structural Differences Only**
   - Template fields are reorganized but functionally equivalent
   - Date/time fields have format differences but same data
   - Many fields are simple renames or restructuring

## 🚨 Critical Questions for Stakeholders

1. **Is backward compatibility required** for existing Legacy integrations?
2. **Can we establish data mapping strategies** for the 14 critical identity fields?
3. **Should SAAS APIs include Legacy-style response wrappers** for easier migration?
4. **Are there business processes** that depend on Legacy-only metadata fields?

## 📊 Risk Assessment

| Risk Level | Field Count | Mitigation Complexity |
|------------|-------------|----------------------|
| **HIGH** | 14 | Complex - Requires data mapping |
| **MEDIUM** | 15 | Moderate - Structural changes needed |
| **LOW** | 35 | Simple - Like-for-like replacements |

## 🎉 Good News

- **60% of Legacy fields** have direct or equivalent SAAS counterparts
- **Template systems** are functionally equivalent despite structural differences
- **Core business data** is preserved in SAAS with modern improvements
- **Most differences** are structural rather than functional gaps

---

**Next Steps**: Review this analysis with technical and business stakeholders to prioritize migration strategies for the 64 Legacy-only fields identified.