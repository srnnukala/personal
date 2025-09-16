# Database Schema Documentation

## Overview

This document describes the database schema for the system with the following key entities:
- User management (SS_USER, GROUP, USER_GROUP)
- System and service definitions (COM_SYSTEM, SERVICE)
- Permission management (SERVICE_GROUP, SYSTEM_GROUP)
- Menu hierarchy (COM_MENU)

## Entity-Relationship Summary

### Core Entities
- **SS_USER**: User accounts and authentication
- **GROUP**: User groups for permissions and organization
- **COM_SYSTEM**: System definitions and configuration
- **SERVICE**: Service definitions within systems
- **COM_MENU**: Hierarchical menu structure

### Junction Tables (Many-to-Many Relationships)
- **USER_GROUP**: Links users to groups (M:N)
- **SERVICE_GROUP**: Links services to groups with permission levels (M:N)
- **SYSTEM_GROUP**: Links systems to groups with access levels (M:N)

## Detailed Table Definitions

### SS_USER

**Description**: User accounts and authentication information

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| user_id | INT | PRIMARY KEY | User unique identifier |
| username | VARCHAR(50) | UNIQUE NOT NULL | User login name |
| email | VARCHAR(100) | NOT NULL | User email address |
| first_name | VARCHAR(50) | NOT NULL | User first name |
| last_name | VARCHAR(50) | NOT NULL | User last name |
| created_date | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Account creation date |
| last_login | TIMESTAMP | NULL | Last login timestamp |
| is_active | BOOLEAN | DEFAULT TRUE | Account status |
| password_hash | VARCHAR(255) | NOT NULL | Encrypted password |


### GROUP

**Description**: User groups for permissions and organization

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| group_id | INT | PRIMARY KEY | Group unique identifier |
| group_name | VARCHAR(100) | UNIQUE NOT NULL | Group name |
| group_description | TEXT | NULL | Group description |
| group_type | VARCHAR(50) | NOT NULL | Type of group (role, department, etc.) |
| created_date | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Group creation date |
| created_by | INT | NOT NULL | User who created the group |
| is_active | BOOLEAN | DEFAULT TRUE | Group status |


### COM_SYSTEM

**Description**: System definitions and configuration

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| system_id | INT | PRIMARY KEY | System unique identifier |
| system_name | VARCHAR(100) | UNIQUE NOT NULL | System name |
| system_code | VARCHAR(20) | UNIQUE NOT NULL | System code |
| system_description | TEXT | NULL | System description |
| system_url | VARCHAR(255) | NULL | System base URL |
| system_version | VARCHAR(20) | NULL | Current system version |
| is_active | BOOLEAN | DEFAULT TRUE | System status |
| created_date | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | System registration date |


### SERVICE

**Description**: Service definitions and capabilities

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| service_id | INT | PRIMARY KEY | Service unique identifier |
| service_name | VARCHAR(100) | NOT NULL | Service name |
| service_code | VARCHAR(50) | UNIQUE NOT NULL | Service code |
| service_description | TEXT | NULL | Service description |
| service_type | VARCHAR(50) | NOT NULL | Type of service |
| system_id | INT | NOT NULL | Associated system |
| is_active | BOOLEAN | DEFAULT TRUE | Service status |
| created_date | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Service creation date |


### COM_MENU

**Description**: Menu hierarchy and navigation structure

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| menu_id | INT | PRIMARY KEY | Menu item unique identifier |
| menu_name | VARCHAR(100) | NOT NULL | Menu item name |
| menu_label | VARCHAR(100) | NOT NULL | Display label |
| menu_url | VARCHAR(255) | NULL | Menu item URL |
| menu_icon | VARCHAR(50) | NULL | Menu icon class |
| parent_menu_id | INT | NULL | Parent menu item (for hierarchy) |
| system_id | INT | NULL | Associated system |
| group_id | INT | NULL | Required group for access |
| sort_order | INT | DEFAULT 0 | Display order |
| is_active | BOOLEAN | DEFAULT TRUE | Menu item status |
| created_date | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Menu creation date |


### USER_GROUP

**Description**: Many-to-many relationship between users and groups

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| user_group_id | INT | PRIMARY KEY | Junction table unique identifier |
| user_id | INT | NOT NULL | Reference to SS_USER |
| group_id | INT | NOT NULL | Reference to GROUP |
| assigned_date | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Assignment date |
| assigned_by | INT | NOT NULL | User who made the assignment |
| is_active | BOOLEAN | DEFAULT TRUE | Assignment status |


### SERVICE_GROUP

**Description**: Many-to-many relationship between services and groups

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| service_group_id | INT | PRIMARY KEY | Junction table unique identifier |
| service_id | INT | NOT NULL | Reference to SERVICE |
| group_id | INT | NOT NULL | Reference to GROUP |
| permission_level | VARCHAR(20) | DEFAULT 'READ' | Permission level (read, write, admin) |
| assigned_date | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Assignment date |
| is_active | BOOLEAN | DEFAULT TRUE | Assignment status |


### SYSTEM_GROUP

**Description**: Many-to-many relationship between systems and groups

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| system_group_id | INT | PRIMARY KEY | Junction table unique identifier |
| system_id | INT | NOT NULL | Reference to COM_SYSTEM |
| group_id | INT | NOT NULL | Reference to GROUP |
| access_level | VARCHAR(20) | DEFAULT 'user' | Access level (user, admin, super_admin) |
| assigned_date | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Assignment date |
| is_active | BOOLEAN | DEFAULT TRUE | Assignment status |


## Relationships

| From Table | To Table | Relationship Type | Foreign Key | Description |
|------------|----------|-------------------|-------------|-------------|
| SS_USER | USER_GROUP | 1:N | user_id → user_id | One user can belong to many groups |
| GROUP | USER_GROUP | 1:N | group_id → group_id | One group can have many users |
| SERVICE | SERVICE_GROUP | 1:N | service_id → service_id | One service can be assigned to many groups |
| GROUP | SERVICE_GROUP | 1:N | group_id → group_id | One group can access many services |
| COM_SYSTEM | SYSTEM_GROUP | 1:N | system_id → system_id | One system can be assigned to many groups |
| GROUP | SYSTEM_GROUP | 1:N | group_id → group_id | One group can access many systems |
| COM_SYSTEM | SERVICE | 1:N | system_id → system_id | One system can have many services |
| COM_SYSTEM | COM_MENU | 1:N | system_id → system_id | One system can have many menu items |
| GROUP | COM_MENU | 1:N | group_id → group_id | One group can control many menu items |
| COM_MENU | COM_MENU | 1:N | menu_id → parent_menu_id | Menu hierarchy (self-referencing) |
| SS_USER | GROUP | 1:N | user_id → created_by | User who created the group |
| SS_USER | USER_GROUP | 1:N | user_id → assigned_by | User who made the assignment |

## Key Design Patterns

### Many-to-Many Relationships
The schema uses junction tables to implement many-to-many relationships:
- Users can belong to multiple groups, and groups can contain multiple users
- Services can be assigned to multiple groups with different permission levels
- Systems can be accessible by multiple groups with different access levels

### Hierarchical Structure
The COM_MENU table implements a hierarchical structure using self-referencing foreign keys:
- `parent_menu_id` references `menu_id` in the same table
- This allows for unlimited menu depth and tree-like navigation structures

### Security and Access Control
The schema supports fine-grained access control:
- Group-based permissions for both systems and services
- Menu items can be restricted to specific groups
- Different permission levels (read/write/admin) and access levels (user/admin/super_admin)

### Audit Trail
Most tables include audit fields:
- `created_date`: When the record was created
- `created_by` / `assigned_by`: Who performed the action
- `is_active`: Soft delete functionality
