# 📘 Python Learning Journey - Beginner Data Analysis

## 📌 Current Learning Focus

This document summarizes the Python learning process applied during the Malang Food Analysis project.

The project focuses on beginner-level exploratory data analysis using:
- pandas,
- matplotlib,
- seaborn,
- and simple analytical workflows.

---

# 🧠 Current Skill Level

## Comfortable With
- Loading CSV datasets using pandas
- Basic data inspection and filtering
- `groupby()` aggregation
- Simple data visualization
- Basic exploratory data analysis (EDA)

---

## Currently Learning
- Data storytelling through visualization
- Better code organization
- More effective grouping and aggregation strategies

---

## Next Learning Goals
- Advanced pandas operations
- Data transformation workflows
- More structured analysis pipelines
- Better visualization design practices

---

# 📊 What I Learned From This Project

## 1. Data Loading & Inspection

Learned how to:
- load cleaned datasets,
- inspect dataset structure,
- and identify potential data issues before analysis.

Example:

```python
import pandas as pd

df = pd.read_csv("data/processed/Malang_City_Food_Dataset_Cleaned.csv")

df.info()
df.head()
```

---

## 2. Data Aggregation with Pandas

Used:
- `groupby()`
- `sum()`
- `mean()`
- `count()`

Example:

```python
df.groupby("Kategori_Menu")["Jumlah_Ulasan_Menu"].sum()
```

### Key Learning
Aggregation helps convert raw data into summarized analytical information.

---

## 3. Data Visualization

Visualization libraries used:
- matplotlib
- seaborn

### Chart Types Created
- Bar charts
- Horizontal bar charts
- Pie charts

### Key Learning
Visualization is not only about creating charts, but also about simplifying data interpretation.

---

## 4. Insight Generation

Through this project, I practiced translating numerical outputs into simple analytical observations.

### Example Findings
- Sambal-related menus appear frequently in reviews
- Affordable pricing dominates the dataset
- Most restaurants maintain ratings above 4.0

### Key Learning
Raw numerical outputs become more meaningful when connected to observable patterns.

---

## 5. Working with Real-World Data

This project helped me understand that:
- real datasets often contain inconsistencies,
- preprocessing is important before analysis,
- and column consistency across Excel, SQL, and Python workflows matters.

### Example Issues Found
- inconsistent category formatting,
- duplicated naming styles,
- and manual categorization challenges.

---

# ⚙️ Libraries Used

| Library | Purpose |
|---|---|
| pandas | Data manipulation |
| matplotlib | Visualization |
| seaborn | Visualization styling |
| numpy | Numerical operations |

---

# 📁 Python Workflow

1. Load cleaned dataset
2. Inspect dataset structure
3. Aggregate and summarize data
4. Create visualizations
5. Generate insights
6. Export charts

---

# 📉 Project Limitations

- The analysis is descriptive only.
- The dataset represents a single-time snapshot.
- No advanced statistical modeling was used.
- Insights depend on manually collected data quality.

---

# 🎯 Learning Outcome

Through this project, I learned:
- how Python supports exploratory data analysis,
- how visualizations simplify interpretation,
- and how data preprocessing affects analytical results.

---

# 🚀 Next Step

I plan to continue improving:
- pandas skills,
- visualization quality,
- SQL and Python integration,
- and analytical storytelling.

---

## 📝 Note

This project is part of a beginner-level data analysis portfolio focused on learning an end-to-end workflow:

```md
Excel → SQL → Python → Exploratory Insight
```

---

*This document is part of the Malang Food Analysis portfolio project.*