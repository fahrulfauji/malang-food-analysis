````
# 📘 SQL Learning Journey — Beginner SQL Exploration

## 📌 Current SQL Skill Level

### Comfortable With
- SELECT statements
- WHERE filtering
- COUNT(), AVG(), MAX()
- GROUP BY
- ORDER BY
- LIMIT
- Basic data aggregation

### Currently Learning
- HAVING clause
- CASE WHEN
- Subqueries
- Multi-condition filtering
- More structured analytical queries

### Future Learning Goals
- JOIN operations
- Common Table Expressions (CTE)
- Window Functions
- Query optimization
- More advanced business-oriented analysis

---

# 🎯 What I Learned From This Project

This project helped me understand how SQL can be used to transform raw restaurant data into structured analytical insights.

The analysis focused on:
- Data aggregation
- Category analysis
- Review distribution
- Pricing analysis
- Restaurant popularity

---

# ✅ SQL Skills Demonstrated

## 1. Data Aggregation

Used aggregation functions to summarize restaurant and menu data.

Examples:
- COUNT()
- AVG()
- MAX()
- ROUND()

---

## 2. Categorical Analysis

Used `GROUP BY` to analyze:
- Menu categories
- Rating distribution
- Price segmentation

This helped identify common patterns within the dataset.

---

## 3. Ranking & Sorting

Used:
- ORDER BY
- LIMIT

to identify:
- Highly reviewed restaurants
- Most discussed menu items

---

## 4. Analytical Thinking

Translated business-related questions into SQL queries.

Examples:
- Which menu categories dominate?
- Which restaurants receive the most reviews?
- How are menu prices distributed?
- Do higher prices relate to higher ratings?

---

# 🔍 Query-by-Query Learning Notes

## Query 1 — Dataset Overview

```sql
SELECT
    COUNT(*) AS total_menu_items,
    COUNT(DISTINCT Nama_Tempat) AS total_restaurants
FROM restaurants;
````

### Learning Outcome

Learned how to:

* Measure dataset size
* Count unique entities
* Validate imported data

---

## Query 2 — Menu Category Distribution

```sql
SELECT
    Kategori_Menu,
    COUNT(*) AS total_menu_items
FROM restaurants
GROUP BY Kategori_Menu;
```

### Learning Outcome

Learned how to:

* Group categorical data
* Generate category summaries
* Understand distribution patterns

---

## Query 3 — Average Price Analysis

```sql
SELECT
    Kategori_Menu,
    AVG(Harga_Rata_Rata) AS average_price
FROM restaurants
GROUP BY Kategori_Menu;
```

### Learning Outcome

Learned how to:

* Calculate averages
* Compare categories numerically
* Perform basic pricing analysis

---

## Query 4 — Top Restaurants by Reviews

```sql
SELECT
    Nama_Tempat,
    MAX(Jumlah_Total_Ulasan) AS total_reviews
FROM restaurants
GROUP BY Nama_Tempat
ORDER BY total_reviews DESC
LIMIT 5;
```

### Learning Outcome

Learned how to:

* Rank data
* Sort analytical results
* Identify highly reviewed restaurants

---

## Query 5 — Rating Distribution

```sql
SELECT
    ROUND(Rating, 1) AS rating_score,
    COUNT(*) AS total_records
FROM restaurants
GROUP BY ROUND(Rating, 1);
```

### Learning Outcome

Learned how to:

* Transform numeric data
* Use ROUND() for cleaner grouping
* Analyze score distributions

---

# ⚠️ Challenges Faced During the Project

## Challenge 1 — Understanding GROUP BY

Initially, I was confused about:

* When GROUP BY is necessary
* Why aggregation functions require grouping

### Solution

Practiced with smaller examples until I understood how grouped summaries work.

---

## Challenge 2 — CSV Import Issues

I experienced problems with:

* File paths
* MySQL permissions
* `LOAD DATA INFILE`

### Solution

Learned about:

* `secure_file_priv`
* Proper CSV formatting
* MySQL import configuration

---

## Challenge 3 — Interpreting Query Results

At first, query outputs felt like just numbers without meaning.

### Solution

Focused on connecting SQL results to:

* Customer behavior
* Restaurant trends
* Pricing patterns
* Business interpretation

---

# 🧠 Key Takeaways

Through this project, I learned that SQL is not only about retrieving data, but also about:

* Structuring information
* Finding patterns
* Supporting analytical thinking
* Translating raw data into insights

---

# 🚀 Next Improvement Targets

The next version of this project may include:

* More advanced filtering
* Basic relationship analysis
* Multi-table relational design
* SQL JOIN operations
* Window functions
* Better analytical storytelling

---

# 📚 Learning Reflection

This project represents my early-stage SQL learning journey.

Rather than focusing on complex techniques immediately, I focused on:

* Understanding fundamentals
* Writing readable queries
* Building analytical habits
* Documenting the learning process clearly

---

*This document reflects a beginner-level SQL learning journey built through a real exploratory data analysis project.*

```