# Database Entity-Relationship Diagram (ERD)

This repository contains a comprehensive Entity-Relationship Diagram (ERD) for a database schema designed to manage users, systems, services, and permissions.

## Generated Files

### ERD Visualizations
- **database_erd.png** - High-resolution PNG format ERD (6000x2218 pixels)
- **database_erd.svg** - Scalable Vector Graphics format ERD
- **database_erd.pdf** - PDF format ERD for printing and documentation

### Schema Documentation
- **database_schema.md** - Detailed markdown documentation of all tables, columns, and relationships
- **database_schema.json** - JSON export of the complete schema definition
- **database_erd_generator.py** - Python tool used to generate the ERD and documentation

## Database Tables Overview

The ERD includes the following 8 tables as specified in the requirements:

### Core Entity Tables
1. **SS_USER** - User accounts and authentication information
2. **GROUP** - User groups for permissions and organization  
3. **COM_SYSTEM** - System definitions and configuration
4. **SERVICE** - Service definitions within systems
5. **COM_MENU** - Hierarchical menu structure

### Junction Tables (Many-to-Many Relationships)
6. **USER_GROUP** - Links users to groups (M:N relationship)
7. **SERVICE_GROUP** - Links services to groups with permission levels (M:N relationship) 
8. **SYSTEM_GROUP** - Links systems to groups with access levels (M:N relationship)

## Key Relationships Implemented

### Many-to-Many (M:N) Relationships
- **Users ↔ Groups**: Via USER_GROUP junction table
  - One user can belong to multiple groups
  - One group can contain multiple users
  - Includes assignment tracking (date, assigned by user)

- **Services ↔ Groups**: Via SERVICE_GROUP junction table
  - One service can be assigned to multiple groups
  - One group can access multiple services
  - Includes permission levels (read, write, admin)

- **Systems ↔ Groups**: Via SYSTEM_GROUP junction table
  - One system can be assigned to multiple groups
  - One group can access multiple systems
  - Includes access levels (user, admin, super_admin)

### One-to-Many (1:N) Relationships
- **COM_SYSTEM → SERVICE**: One system can have many services
- **COM_SYSTEM → COM_MENU**: One system can have many menu items
- **GROUP → COM_MENU**: One group can control access to many menu items
- **COM_MENU → COM_MENU**: Self-referencing for menu hierarchy (parent-child relationships)

## Schema Features

### Security and Access Control
- Group-based permission system
- Fine-grained access control for services and systems
- Menu visibility based on group membership
- Multiple permission/access levels supported

### Audit Trail
- Creation timestamps on all tables
- User tracking for assignments and group creation
- Soft delete functionality with `is_active` flags

### Hierarchical Structure
- COM_MENU supports unlimited menu depth via self-referencing foreign keys
- Parent-child relationships enable tree-like navigation structures

### Data Integrity
- Primary keys on all tables
- Foreign key relationships properly defined
- Unique constraints where appropriate
- NOT NULL constraints on required fields

## Visual Design

The ERD uses color coding for easy identification:
- **Light Green**: User-related tables (SS_USER)
- **Light Yellow**: Junction tables (USER_GROUP, SERVICE_GROUP, SYSTEM_GROUP)
- **Light Coral**: System/Service tables (COM_SYSTEM, SERVICE)
- **Light Blue**: Other tables (GROUP, COM_MENU)

Relationship lines show:
- **Blue arrows**: One-to-Many relationships
- **Labels**: Show cardinality and column mappings
- **Crow's foot notation**: Indicates the "many" side of relationships

## How to Use

1. **View the ERD**: Open `database_erd.png` for the visual diagram
2. **Read Documentation**: Check `database_schema.md` for detailed table definitions
3. **Integrate with Tools**: Use `database_schema.json` for schema import into database tools
4. **Regenerate**: Run `python3 database_erd_generator.py` to recreate all files

## Requirements Met

✅ **All 8 specified tables included**: COM_SYSTEM, SERVICE, GROUP, USER_GROUP, SERVICE_GROUP, SYSTEM_GROUP, COM_MENU, SS_USER

✅ **Many-to-Many relationships properly implemented**:
- USER_GROUP links SS_USER and GROUP
- SERVICE_GROUP links SERVICE and GROUP  
- SYSTEM_GROUP links COM_SYSTEM and GROUP

✅ **Hierarchical relationships**: COM_MENU references COM_SYSTEM and GROUP, plus supports menu hierarchy

✅ **Complete attribute definitions**: All tables include relevant attributes with data types, constraints, and descriptions

✅ **Primary and Foreign Keys**: Properly defined relationships with clear key mappings

✅ **Accurate cardinality representation**: 1:N and M:N relationships clearly marked in the diagram

This ERD provides a comprehensive foundation for a user management system with flexible permission controls and hierarchical menu structures.