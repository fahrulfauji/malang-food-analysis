# 📊 Excel Data Processing Workflow

## 📌 Project Overview

This document explains the Excel-based data cleaning and preprocessing workflow used in the Malang Food Analysis project.

The workflow covers:
- manual data collection,
- price standardization,
- menu categorization,
- exploratory analysis,
- and CSV preparation for SQL and Python analysis.

---

# 📁 Data Collection

### Source Information
- **Platform:** Google Maps
- **Collection Method:** Manual data collection
- **Collection Duration:** Approximately 5 days
- **Collection Date:** January 2026

### Dataset Summary
- 372 menu items
- 89 restaurants
- 5 subdistricts in Malang City:
  - Lowokwaru
  - Blimbing
  - Klojen
  - Sukun
  - Kedungkandang

### Initial Output File
```md
Malang_City_Food_Record_Dataset_By_Google_Maps.xlsx
```

---

# ⚙️ Excel Preparation

## 1. Dataset Initialization

The raw dataset was organized into structured tabular format using Excel Tables to simplify filtering, formula propagation, and data consistency checks.

### Main Columns
- Restaurant Name
- Subdistrict
- Menu
- Menu Reviews
- Total Reviews
- Rating
- Minimum Price
- Maximum Price

---

# 🧹 Data Cleaning Process

## 2. Price Standardization

### Initial Issue
The raw dataset stored simplified numeric values:
- `25` → Rp25,000
- `50` → Rp50,000

### Cleaning Process
Additional columns were created:
- `Harga_Min_Clean`
- `Harga_Max_Clean`

### Conversion Formula

```excel
=[@[Harga_Minimal]]*1000
```

The converted values were then formatted using Rupiah currency formatting.

---

## 3. Average Price Calculation

A new column named:

```md
Harga_Rata_Rata
```

was created using:

```excel
=([@[Harga_Min_Clean]]+[@[Harga_Max_Clean]])/2
```

This column was used for pricing analysis and segmentation.

---

## 4. Price Segmentation

Menu prices were grouped into three categories:

| Segment | Description |
|---|---|
| Murah | Below Rp25,000 |
| Sedang | Rp25,000–Rp50,000 |
| Mahal | Above Rp50,000 |

### Formula Used

```excel
=IF([@[Harga_Rata_Rata]]<=25000,"Murah (<25K)",
    IF([@[Harga_Rata_Rata]]<=50000,"Sedang (25-50K)",
    "Mahal (>50K)"))
```

---

# 🍽️ Menu Categorization

## 5. Menu Classification

Menu items were manually categorized into:

| Category | Description |
|---|---|
| PROTEIN | Chicken, fish, meat, seafood |
| KARBO | Rice, noodles, porridge |
| PENDAMPING | Sambal, tofu, tempeh, snacks |

### Example Classification
- Ayam → PROTEIN
- Nasi → KARBO
- Sambal → PENDAMPING

The categorization process was performed manually after sorting similar menu names alphabetically.

---

# 📈 Exploratory Analysis in Excel

## 6. Pivot Table Analysis

Pivot tables were used to summarize:
- total menu reviews,
- average prices,
- and menu category distribution.

### Main Metrics
- Sum of Menu Reviews
- Average Menu Price
- Total Menu Count

---

# 📊 Visualization

## 7. Excel Charts

Basic visualizations were created using Excel to support early exploratory analysis.

### Charts Created
- Pie Chart — Menu Category Distribution
- Pivot Summary Visualization

The charts were exported as PNG files for documentation purposes.

---

# ✅ Data Validation

## 8. Validation Checks

Several validation checks were performed:

### Logical Validation
- No minimum price exceeded maximum price
- Rating values remained within valid range (1–5)

### Completeness Check
- No missing values in important columns
- All menu items successfully categorized

### Spot Checking
Approximately 10% of rows were manually reviewed to verify:
- categorization consistency,
- formula accuracy,
- and formatting quality.

---

# 📤 CSV Export Preparation

## 9. Export Workflow

Formula-based columns were converted into static values before export to prevent formula dependency issues.

### Export Format
```md
CSV UTF-8
```

### Final Output File
```md
Malang_City_Food_Dataset_Cleaned.csv
```

Location:
```md
data/processed/
```

---

# 📊 Summary Findings from Excel Analysis

| Category | Reviews | Percentage | Avg Price | Total Menu |
|---|---|---|---|---|
| Pendamping | 4,327 | 38.6% | Rp32,779 | 131 |
| Protein | 3,548 | 31.6% | Rp36,652 | 132 |
| Karbo | 3,346 | 29.8% | Rp35,335 | 109 |

---

# 🔍 Initial Insights

- Complementary menu items frequently appear in customer discussions.
- Protein menus tend to have higher average prices.
- Menu distribution across categories is relatively balanced.
- Affordable and mid-priced menus dominate the dataset.

---

# 🖼️ Excel Analysis Screenshots

### Pivot Table Summary
![Excel Pivot Table](excel_screenshots/04_pivot_table_results.png)

*Pivot table summary showing menu distribution, total reviews, and average prices.*

---

### Pie Chart Visualization
![Excel Pie Chart](excel_screenshots/05_pie_chart_excel.png)

*Pie chart visualization of menu category distribution created in Microsoft Excel.*

---

## 📝 Note

This documentation reflects a beginner-level exploratory data cleaning and preprocessing workflow using Microsoft Excel.

It is intended to demonstrate the learning process and practical implementation of basic data analysis techniques.

---

*This document is part of the Malang Food Analysis portfolio project.*