# Database Tasks

This repository contains two sets of tasks related to databases.

## Task 1: Product Sales Database

### Description
This task involves designing a database for tracking products sold in various cities and countries to different customers. It includes information about the materials used in the products and their quantities. The database consists of several tables, such as customers, places, materials, products, components, and product purchases.

### SQL Script
To create the database and tables for Task 1, refer to the provided SQL script.

### Table Modifications
The `ALTER TABLE` command should be used to make the following modifications to the tables:
- Define a suitable unique identifier for each table.
- Consider using a surrogate key as the primary key if necessary.
- Add foreign keys and establish proper relationships between tables.
- Remove the "Image" attribute from all tables.
- Rename abbreviated columns with their full names.
- (Bonus) Apply `CHECK` constraints to ensure JMBG and phone numbers contain only digits.

### Additional Table
Create a new table of your choice that includes foreign keys from two existing tables.

### Data Insertion
Insert several rows into each table while maintaining referential integrity.

### Data Cleanup
Add a sequence to clean up the data. Delete all rows from the tables, then delete the tables themselves, and finally, the entire database.

## Task 2: Patient Health Records Database

### Description
This task involves designing a database for managing patients' health records, including their medical history, treatments, and the work of doctors in a healthcare institution. The database consists of tables such as patients, doctors, medications, illnesses, manufacturers, and illness occurrences.

### SQL Script
To create the database and tables for Task 2, refer to the provided SQL script.

### Table Modifications
Follow the same steps as in Task 1 to modify the tables accordingly.

### Additional Table
Create a new table of your choice that includes foreign keys from two existing tables.
