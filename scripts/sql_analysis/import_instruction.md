# 📥 MySQL CSV Import Instructions

This document explains the basic process used to import the cleaned CSV dataset into MySQL.

---

## 1. Create Database

Run:

```sql
CREATE DATABASE malang_food_analysis;
USE malang_food_analysis;
```
## 2. Run Database Schema

Execute:

SOURCE database_schema.sql;

This will:

create the restaurants table,
and prepare the database structure.

## 3. Place CSV File

Move the cleaned CSV dataset into your MySQL upload directory.

Example:

C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/

## 4. Import CSV Data

Run the LOAD DATA INFILE statement included inside:

database_schema.sql

## 5. Validate Imported Data

Example validation query:

```sql
SELECT COUNT(*) FROM restaurants;
```

Expected result:

372 rows imported successfully

*This workflow reflects a beginner-level SQL data import process using MySQL Workbench.*