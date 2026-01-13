# 📘 SQL Learning Journey - Beginner Level

## My Current SQL Skill Level
**Comfortable With**: Basic SELECT, COUNT, GROUP BY, ORDER BY, LIMIT  
**Learning Now**: AVG(), ROUND(), MAX() with GROUP BY  
**Next Goals**: JOINs, subqueries, window functions  

## What I Learned From This Project

### 1. Basic SQL Operations Mastered:
- ✅ **Counting data**: `SELECT COUNT(*) FROM table`
- ✅ **Grouping data**: `GROUP BY` with categories
- ✅ **Aggregation**: `AVG()`, `MAX()` for numerical analysis
- ✅ **Sorting results**: `ORDER BY DESC/ASC`
- ✅ **Limiting output**: `LIMIT` for top-N analysis

### 2. Practical Business Questions Answered:
1. **How much data do we have?** → COUNT() query
2. **How are items distributed?** → GROUP BY query
3. **What are the average prices?** → AVG() with GROUP BY
4. **Who are the top performers?** → ORDER BY + LIMIT
5. **How is quality distributed?** → ROUND() with GROUP BY

### 3. Technical Skills Demonstrated:
- Database schema creation
- CSV data import to MySQL
- Writing and executing SQL queries
- Interpreting query results
- Documenting the analysis process

## Query-by-Query Learning Points

### Query 1: Simple Counting
```sql
SELECT COUNT(*) AS total_menu FROM restaurants;
```
**Learning**: Most fundamental SQL operation - verifying data completeness.

### Query 2: Categorical Distribution
```sql
SELECT Kategori_Menu, COUNT(*) FROM restaurants GROUP BY Kategori_Menu;
```
**Learning**: How to summarize data by categories using GROUP BY.

### Query 3: Numerical Aggregation
```sql
SELECT Kategori_Menu, AVG(Harga_Rata_Rata) FROM restaurants GROUP BY Kategori_Menu;
```
**Learning**: Calculating averages within groups.

### Query 4: Ranking & Sorting
```sql
SELECT Nama_Tempat, MAX(Jumlah_Total_Ulasan) 
FROM restaurants 
GROUP BY Nama_Tempat 
ORDER BY ... DESC 
LIMIT 5;
```
**Learning**: Finding top performers with sorting and limiting.

### Query 5: Data Transformation
```sql
SELECT ROUND(Rating, 1), COUNT(*) 
FROM restaurants 
GROUP BY ROUND(Rating, 1);
```
**Learning**: Modifying data (rounding) before grouping.

## Challenges & Solutions

### Challenge 1: Understanding GROUP BY
Initially confused about when to use GROUP BY vs simple SELECT.

**Solution**: Practiced with simple datasets until I understood that GROUP BY is for categorical summaries.

### Challenge 2: Importing CSV Data
The `LOAD DATA INFILE` had issues with file paths and permissions.

**Solution**: Learned about MySQL's secure_file_priv setting and proper file path formatting.

### Challenge 3: Query Result Interpretation
Numbers without context weren't meaningful.

**Solution**: Added analysis sections to explain what the results mean for business decisions.