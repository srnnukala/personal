#!/usr/bin/env python3
"""
Database Entity-Relationship Diagram Generator

This tool generates an ERD for the following database tables:
- COM_SYSTEM: System configuration table
- SERVICE: Service definition table  
- GROUP: User/permission groups table
- USER_GROUP: Many-to-many junction table linking SS_USER and GROUP
- SERVICE_GROUP: Many-to-many junction table linking SERVICE and GROUP
- SYSTEM_GROUP: Many-to-many junction table linking COM_SYSTEM and GROUP
- COM_MENU: Menu hierarchy table with references to COM_SYSTEM and GROUP
- SS_USER: User account table
"""

import graphviz
from typing import Dict, List, Tuple
import json
import os


class DatabaseERDGenerator:
    """Generate Entity-Relationship Diagrams for database schemas"""
    
    def __init__(self):
        self.tables = {}
        self.relationships = []
        self._define_database_schema()
    
    def _define_database_schema(self):
        """Define the database schema with tables, columns, and relationships"""
        
        # Define tables with their attributes
        self.tables = {
            "SS_USER": {
                "attributes": [
                    ("user_id", "INT", "PRIMARY KEY", "User unique identifier"),
                    ("username", "VARCHAR(50)", "UNIQUE NOT NULL", "User login name"),
                    ("email", "VARCHAR(100)", "NOT NULL", "User email address"),
                    ("first_name", "VARCHAR(50)", "NOT NULL", "User first name"),
                    ("last_name", "VARCHAR(50)", "NOT NULL", "User last name"),
                    ("created_date", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP", "Account creation date"),
                    ("last_login", "TIMESTAMP", "NULL", "Last login timestamp"),
                    ("is_active", "BOOLEAN", "DEFAULT TRUE", "Account status"),
                    ("password_hash", "VARCHAR(255)", "NOT NULL", "Encrypted password")
                ],
                "description": "User accounts and authentication information"
            },
            
            "GROUP": {
                "attributes": [
                    ("group_id", "INT", "PRIMARY KEY", "Group unique identifier"),
                    ("group_name", "VARCHAR(100)", "UNIQUE NOT NULL", "Group name"),
                    ("group_description", "TEXT", "NULL", "Group description"),
                    ("group_type", "VARCHAR(50)", "NOT NULL", "Type of group (role, department, etc.)"),
                    ("created_date", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP", "Group creation date"),
                    ("created_by", "INT", "NOT NULL", "User who created the group"),
                    ("is_active", "BOOLEAN", "DEFAULT TRUE", "Group status")
                ],
                "description": "User groups for permissions and organization"
            },
            
            "COM_SYSTEM": {
                "attributes": [
                    ("system_id", "INT", "PRIMARY KEY", "System unique identifier"),
                    ("system_name", "VARCHAR(100)", "UNIQUE NOT NULL", "System name"),
                    ("system_code", "VARCHAR(20)", "UNIQUE NOT NULL", "System code"),
                    ("system_description", "TEXT", "NULL", "System description"),
                    ("system_url", "VARCHAR(255)", "NULL", "System base URL"),
                    ("system_version", "VARCHAR(20)", "NULL", "Current system version"),
                    ("is_active", "BOOLEAN", "DEFAULT TRUE", "System status"),
                    ("created_date", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP", "System registration date")
                ],
                "description": "System definitions and configuration"
            },
            
            "SERVICE": {
                "attributes": [
                    ("service_id", "INT", "PRIMARY KEY", "Service unique identifier"),
                    ("service_name", "VARCHAR(100)", "NOT NULL", "Service name"),
                    ("service_code", "VARCHAR(50)", "UNIQUE NOT NULL", "Service code"),
                    ("service_description", "TEXT", "NULL", "Service description"),
                    ("service_type", "VARCHAR(50)", "NOT NULL", "Type of service"),
                    ("system_id", "INT", "NOT NULL", "Associated system"),
                    ("is_active", "BOOLEAN", "DEFAULT TRUE", "Service status"),
                    ("created_date", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP", "Service creation date")
                ],
                "description": "Service definitions and capabilities"
            },
            
            "COM_MENU": {
                "attributes": [
                    ("menu_id", "INT", "PRIMARY KEY", "Menu item unique identifier"),
                    ("menu_name", "VARCHAR(100)", "NOT NULL", "Menu item name"),
                    ("menu_label", "VARCHAR(100)", "NOT NULL", "Display label"),
                    ("menu_url", "VARCHAR(255)", "NULL", "Menu item URL"),
                    ("menu_icon", "VARCHAR(50)", "NULL", "Menu icon class"),
                    ("parent_menu_id", "INT", "NULL", "Parent menu item (for hierarchy)"),
                    ("system_id", "INT", "NULL", "Associated system"),
                    ("group_id", "INT", "NULL", "Required group for access"),
                    ("sort_order", "INT", "DEFAULT 0", "Display order"),
                    ("is_active", "BOOLEAN", "DEFAULT TRUE", "Menu item status"),
                    ("created_date", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP", "Menu creation date")
                ],
                "description": "Menu hierarchy and navigation structure"
            },
            
            # Junction Tables for Many-to-Many relationships
            "USER_GROUP": {
                "attributes": [
                    ("user_group_id", "INT", "PRIMARY KEY", "Junction table unique identifier"),
                    ("user_id", "INT", "NOT NULL", "Reference to SS_USER"),
                    ("group_id", "INT", "NOT NULL", "Reference to GROUP"),
                    ("assigned_date", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP", "Assignment date"),
                    ("assigned_by", "INT", "NOT NULL", "User who made the assignment"),
                    ("is_active", "BOOLEAN", "DEFAULT TRUE", "Assignment status")
                ],
                "description": "Many-to-many relationship between users and groups"
            },
            
            "SERVICE_GROUP": {
                "attributes": [
                    ("service_group_id", "INT", "PRIMARY KEY", "Junction table unique identifier"),
                    ("service_id", "INT", "NOT NULL", "Reference to SERVICE"),
                    ("group_id", "INT", "NOT NULL", "Reference to GROUP"),
                    ("permission_level", "VARCHAR(20)", "DEFAULT 'READ'", "Permission level (read, write, admin)"),
                    ("assigned_date", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP", "Assignment date"),
                    ("is_active", "BOOLEAN", "DEFAULT TRUE", "Assignment status")
                ],
                "description": "Many-to-many relationship between services and groups"
            },
            
            "SYSTEM_GROUP": {
                "attributes": [
                    ("system_group_id", "INT", "PRIMARY KEY", "Junction table unique identifier"),
                    ("system_id", "INT", "NOT NULL", "Reference to COM_SYSTEM"),
                    ("group_id", "INT", "NOT NULL", "Reference to GROUP"),
                    ("access_level", "VARCHAR(20)", "DEFAULT 'user'", "Access level (user, admin, super_admin)"),
                    ("assigned_date", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP", "Assignment date"),
                    ("is_active", "BOOLEAN", "DEFAULT TRUE", "Assignment status")
                ],
                "description": "Many-to-many relationship between systems and groups"
            }
        }
        
        # Define relationships
        self.relationships = [
            # Many-to-Many relationships through junction tables
            ("SS_USER", "USER_GROUP", "1:N", "user_id", "user_id", "One user can belong to many groups"),
            ("GROUP", "USER_GROUP", "1:N", "group_id", "group_id", "One group can have many users"),
            
            ("SERVICE", "SERVICE_GROUP", "1:N", "service_id", "service_id", "One service can be assigned to many groups"),
            ("GROUP", "SERVICE_GROUP", "1:N", "group_id", "group_id", "One group can access many services"),
            
            ("COM_SYSTEM", "SYSTEM_GROUP", "1:N", "system_id", "system_id", "One system can be assigned to many groups"),
            ("GROUP", "SYSTEM_GROUP", "1:N", "group_id", "group_id", "One group can access many systems"),
            
            # Direct relationships
            ("COM_SYSTEM", "SERVICE", "1:N", "system_id", "system_id", "One system can have many services"),
            ("COM_SYSTEM", "COM_MENU", "1:N", "system_id", "system_id", "One system can have many menu items"),
            ("GROUP", "COM_MENU", "1:N", "group_id", "group_id", "One group can control many menu items"),
            ("COM_MENU", "COM_MENU", "1:N", "menu_id", "parent_menu_id", "Menu hierarchy (self-referencing)"),
            ("SS_USER", "GROUP", "1:N", "user_id", "created_by", "User who created the group"),
            ("SS_USER", "USER_GROUP", "1:N", "user_id", "assigned_by", "User who made the assignment")
        ]
    
    def generate_erd(self, output_format='png', output_file='database_erd'):
        """Generate the ERD using Graphviz"""
        
        # Create a new directed graph
        dot = graphviz.Digraph(comment='Database ERD')
        dot.attr(rankdir='TB', size='20,16', dpi='300')
        dot.attr('node', shape='record', style='filled', fillcolor='lightblue')
        dot.attr('edge', fontsize='10')
        
        # Add tables as nodes
        for table_name, table_info in self.tables.items():
            # Create label for the table with attributes
            label_parts = [f"{{<{table_name}> {table_name}|"]
            
            # Add attributes
            for attr_name, data_type, constraints, description in table_info["attributes"]:
                constraint_text = f" {constraints}" if constraints else ""
                if "PRIMARY KEY" in constraints:
                    label_parts.append(f"+ {attr_name}: {data_type}{constraint_text}\\l")
                elif "FOREIGN KEY" in constraints or any(rel[3] == attr_name or rel[4] == attr_name for rel in self.relationships):
                    label_parts.append(f"# {attr_name}: {data_type}{constraint_text}\\l")
                else:
                    label_parts.append(f"{attr_name}: {data_type}{constraint_text}\\l")
            
            label_parts.append("}")
            label = "".join(label_parts)
            
            # Color code different types of tables
            if table_name in ["USER_GROUP", "SERVICE_GROUP", "SYSTEM_GROUP"]:
                fillcolor = 'lightyellow'  # Junction tables
            elif table_name == "SS_USER":
                fillcolor = 'lightgreen'   # User table
            elif table_name in ["COM_SYSTEM", "SERVICE"]:
                fillcolor = 'lightcoral'   # System/Service tables
            else:
                fillcolor = 'lightblue'    # Other tables
            
            dot.node(table_name, label=label, fillcolor=fillcolor)
        
        # Add relationships as edges
        for from_table, to_table, cardinality, from_col, to_col, description in self.relationships:
            # Create edge label with cardinality and description
            edge_label = f"{cardinality}\\n{from_col} → {to_col}"
            
            # Style different types of relationships
            if cardinality == "1:N":
                dot.edge(from_table, to_table, label=edge_label, arrowhead='crow', color='blue')
            else:
                dot.edge(from_table, to_table, label=edge_label, color='red')
        
        # Generate and save the ERD
        try:
            dot.render(output_file, format=output_format, cleanup=True)
            print(f"ERD generated successfully: {output_file}.{output_format}")
            return True
        except Exception as e:
            print(f"Error generating ERD: {str(e)}")
            return False
    
    def generate_schema_documentation(self, output_file='database_schema.md'):
        """Generate markdown documentation of the database schema"""
        
        doc_lines = [
            "# Database Schema Documentation",
            "",
            "## Overview",
            "",
            "This document describes the database schema for the system with the following key entities:",
            "- User management (SS_USER, GROUP, USER_GROUP)",
            "- System and service definitions (COM_SYSTEM, SERVICE)",
            "- Permission management (SERVICE_GROUP, SYSTEM_GROUP)", 
            "- Menu hierarchy (COM_MENU)",
            "",
            "## Entity-Relationship Summary",
            "",
            "### Core Entities",
            "- **SS_USER**: User accounts and authentication",
            "- **GROUP**: User groups for permissions and organization",
            "- **COM_SYSTEM**: System definitions and configuration",
            "- **SERVICE**: Service definitions within systems",
            "- **COM_MENU**: Hierarchical menu structure",
            "",
            "### Junction Tables (Many-to-Many Relationships)",
            "- **USER_GROUP**: Links users to groups (M:N)",
            "- **SERVICE_GROUP**: Links services to groups with permission levels (M:N)",
            "- **SYSTEM_GROUP**: Links systems to groups with access levels (M:N)",
            "",
            "## Detailed Table Definitions",
            ""
        ]
        
        # Add table details
        for table_name, table_info in self.tables.items():
            doc_lines.extend([
                f"### {table_name}",
                "",
                f"**Description**: {table_info['description']}",
                "",
                "| Column Name | Data Type | Constraints | Description |",
                "|-------------|-----------|-------------|-------------|"
            ])
            
            for attr_name, data_type, constraints, description in table_info["attributes"]:
                constraint_text = constraints if constraints else ""
                doc_lines.append(f"| {attr_name} | {data_type} | {constraint_text} | {description} |")
            
            doc_lines.extend(["", ""])
        
        # Add relationships section
        doc_lines.extend([
            "## Relationships",
            "",
            "| From Table | To Table | Relationship Type | Foreign Key | Description |",
            "|------------|----------|-------------------|-------------|-------------|"
        ])
        
        for from_table, to_table, cardinality, from_col, to_col, description in self.relationships:
            doc_lines.append(f"| {from_table} | {to_table} | {cardinality} | {from_col} → {to_col} | {description} |")
        
        doc_lines.extend([
            "",
            "## Key Design Patterns",
            "",
            "### Many-to-Many Relationships",
            "The schema uses junction tables to implement many-to-many relationships:",
            "- Users can belong to multiple groups, and groups can contain multiple users",
            "- Services can be assigned to multiple groups with different permission levels",
            "- Systems can be accessible by multiple groups with different access levels",
            "",
            "### Hierarchical Structure",
            "The COM_MENU table implements a hierarchical structure using self-referencing foreign keys:",
            "- `parent_menu_id` references `menu_id` in the same table",
            "- This allows for unlimited menu depth and tree-like navigation structures",
            "",
            "### Security and Access Control",
            "The schema supports fine-grained access control:",
            "- Group-based permissions for both systems and services",
            "- Menu items can be restricted to specific groups",
            "- Different permission levels (read/write/admin) and access levels (user/admin/super_admin)",
            "",
            "### Audit Trail",
            "Most tables include audit fields:",
            "- `created_date`: When the record was created",
            "- `created_by` / `assigned_by`: Who performed the action",
            "- `is_active`: Soft delete functionality",
            ""
        ])
        
        # Write documentation to file
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(doc_lines))
            print(f"Schema documentation generated: {output_file}")
            return True
        except Exception as e:
            print(f"Error generating documentation: {str(e)}")
            return False
    
    def export_schema_json(self, output_file='database_schema.json'):
        """Export the schema definition as JSON"""
        
        schema_data = {
            "schema_info": {
                "name": "System Database Schema",
                "description": "Database schema for user management, systems, services, and permissions",
                "version": "1.0",
                "generated_date": "2024-01-01"
            },
            "tables": self.tables,
            "relationships": [
                {
                    "from_table": rel[0],
                    "to_table": rel[1],
                    "cardinality": rel[2],
                    "from_column": rel[3],
                    "to_column": rel[4],
                    "description": rel[5]
                }
                for rel in self.relationships
            ]
        }
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(schema_data, f, indent=2)
            print(f"Schema JSON exported: {output_file}")
            return True
        except Exception as e:
            print(f"Error exporting JSON: {str(e)}")
            return False


def main():
    """Main function to generate ERD and documentation"""
    
    print("Database ERD Generator")
    print("=" * 50)
    
    # Create ERD generator instance
    generator = DatabaseERDGenerator()
    
    # Generate ERD in multiple formats
    formats = ['png', 'svg', 'pdf']
    success_count = 0
    
    for format_type in formats:
        print(f"\nGenerating ERD in {format_type.upper()} format...")
        if generator.generate_erd(output_format=format_type, output_file='database_erd'):
            success_count += 1
        else:
            print(f"Failed to generate {format_type.upper()} format")
    
    # Generate documentation
    print("\nGenerating schema documentation...")
    generator.generate_schema_documentation()
    
    # Export JSON schema
    print("Exporting schema as JSON...")
    generator.export_schema_json()
    
    print(f"\nGeneration complete! Successfully created {success_count}/{len(formats)} ERD formats.")
    
    # List generated files
    print("\nGenerated files:")
    for ext in ['png', 'svg', 'pdf']:
        filename = f"database_erd.{ext}"
        if os.path.exists(filename):
            print(f"  - {filename}")
    
    for doc_file in ['database_schema.md', 'database_schema.json']:
        if os.path.exists(doc_file):
            print(f"  - {doc_file}")


if __name__ == "__main__":
    main()