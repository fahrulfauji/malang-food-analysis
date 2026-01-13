# 📥 MySQL Data Import Guide

## Quick Start
1. Create database using `database_schema.sql`
2. Import CSV data using commands below
3. Verify with simple queries

## Step 1: Prepare CSV File
- File name: `Malang_City_Food_Dataset_Cleaned.csv`
- Encoding: UTF-8
- Location: Note the full file path
- Size: 372 rows + 1 header row

## Step 2: Run Import Command

### Basic Import (Try This First):
```sql
LOAD DATA INFILE 'C:/your/path/Malang_City_Food_Dataset_Cleaned.csv'
INTO TABLE restaurants
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;
```

### If Error, Try This Version:
```sql
LOAD DATA LOCAL INFILE 'C:/your/path/Malang_City_Food_Dataset_Cleaned.csv'
INTO TABLE restaurants
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;
```

## Step 3: Verify Import
```sql
-- Check total rows
SELECT COUNT(*) AS total_rows FROM restaurants;

-- Should return: 376

-- Check sample data
SELECT * FROM restaurants LIMIT 3;

-- Check categories
SELECT DISTINCT Kategori_Menu FROM restaurants;
```

## Common Issues & Fixes

### Issue: "ERROR 1290" - File permission
```sql
-- Check allowed directories
SHOW VARIABLES LIKE 'secure_file_priv';

-- Solutions:
-- 1. Move CSV to directory shown above
-- 2. Or use LOAD DATA LOCAL INFILE
-- 3. Or update MySQL configuration
```

### Issue: "ERROR 1366" - Wrong data type
- Make sure CSV header matches table columns
- Add `IGNORE 1 LINES` to skip header
- Check CSV encoding is UTF-8

### Issue: Column count mismatch
- CSV should have 14 columns
- Table has 14 columns
- Verify with text editor

## Alternative: Manual Verification
If import has issues, verify CSV format:
1. Open CSV in Notepad++
2. Count columns in first row
3. Check for extra commas
4. Ensure proper quotes around text

## Import Success Checklist
- [ ] 372 rows imported
- [ ] No error messages
- [ ] All columns filled
- [ ] Categories match Excel
- [ ] Prices in correct range

## Notes
- Always backup before import
- Test with small file first if unsure
- Document any errors for learning
- Results should match Excel analysis

---
*Imported successfully on 7 January 2026*