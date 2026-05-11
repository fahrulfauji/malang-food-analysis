# 🍽️ Malang Food Analysis - Data Analysis Portfolio Project

![Python](https://img.shields.io/badge/Python-3.13.7-blue)
![Excel](https://img.shields.io/badge/Excel-Office%20LTSC%202024-green)
![MySQL](https://img.shields.io/badge/MySQL-Workbench%208.0%20CE-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📊 Project Overview

This project analyzes food trends and restaurant popularity in Malang, Indonesia, using data collected from publicly available information on Google Maps.

The analysis focuses on identifying consumer preferences, restaurant performance patterns, pricing behavior, and menu category trends within Malang’s culinary market.

This project also demonstrates a complete end-to-end data analysis workflow using Excel, MySQL, and Python — from manual data collection and cleaning to exploratory analysis, visualization, and business insight generation.

**Dataset Scope**
- 372 menu items
- 89 restaurants
- Multiple food categories and price segments
- Review and rating-based analysis

---

## 🎯 Project Objectives

1. Identify dominant food preferences among consumers in Malang
2. Analyze restaurant popularity using review and rating metrics
3. Explore pricing patterns across menu categories
4. Understand menu distribution and customer discussion trends
5. Demonstrate an end-to-end data analysis workflow using Excel, MySQL, and Python
6. Generate business-oriented insights from culinary market data

---

## 📁 Project Structure

```text
malang-food-analysis/
├── data/                          # Raw and processed datasets
│   ├── raw/                       # Original Excel files
│   └── processed/                 # Cleaned CSV datasets
├── scripts/                       # Analysis scripts and documentation
│   ├── excel_cleaning/            # Excel preprocessing documentation
│   ├── sql_analysis/              # MySQL database and SQL queries
│   └── python_visualization/      # Python analysis and visualizations
├── outputs/                       # Generated charts and visual outputs
├── insights/                      # Findings and recommendations
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies
```

---

## 🛠️ Tools & Technologies Used

| Tool | Version | Purpose |
|------|---------|---------|
| **Microsoft Excel** | Office LTSC 2024 | Data cleaning and initial preprocessing |
| **MySQL** | Workbench 8.0 CE | Data querying and aggregation |
| **Python** | 3.13.7 | Data analysis and visualization |
| **pandas** | 2.3.3 | Data manipulation |
| **matplotlib** | 3.10.8 | Data visualization |
| **seaborn** | 0.13.2 | Statistical visualization styling |

---

## 📈 Analysis Process

### Phase 1: Excel Data Processing
- Manual collection of culinary data from publicly available Google Maps information
- Price standardization and currency formatting
- Menu categorization into:
  - Protein
  - Karbo
  - Pendamping
- Initial exploratory analysis using pivot tables and charts

### Phase 2: MySQL Database Analysis
- Database schema creation and table setup
- CSV dataset import into MySQL
- SQL-based exploratory analysis using:
  - aggregation
  - filtering
  - grouping
  - ranking queries
- Query result documentation and interpretation

### Phase 3: Python Visualization & Insight Generation
- Dataset loading and exploration using pandas
- Data visualization using matplotlib and seaborn
- Trend and distribution analysis
- Business insight generation from visualization results
- Exporting charts for reporting and presentation purposes

---

## 📊 Key Insights

### 1. 🥇 Strong Presence of Complementary Menu Items
Sambal-related menu items appear frequently in customer discussions, suggesting that complementary condiments play an important role in customer dining preferences and perceived meal satisfaction.

### 2. 🏆 Restaurant Brand Visibility
Ocean Garden restaurants dominate review volume rankings, indicating strong brand visibility and customer engagement within Malang's culinary market.

### 3. 📊 Balanced Menu Category Distribution
- **Pendamping:** 38.6%
- **Protein:** 31.6%
- **Karbo:** 29.8%

The relatively balanced distribution suggests that restaurants in Malang offer diverse menu compositions rather than relying heavily on a single category.

### 4. 💰 Affordable Culinary Market Characteristics
Most menu items fall below Rp25,000, indicating that affordability remains a dominant characteristic of Malang’s culinary ecosystem, potentially influenced by the city’s strong student population.

### 5. ⭐ Consistent Restaurant Ratings
Most restaurants maintain ratings above 4.0, suggesting relatively consistent customer satisfaction and service quality across the sampled establishments.

---

## 📸 Visualizations

### Excel Analysis

![Excel Pivot Table](outputs/excel_pivot_table.png)

<p align="justify">
<em>
Initial exploratory analysis in Excel highlighting menu category distribution and early pattern identification using pivot tables.
</em>
</p>

---

### Python Visualizations

#### Top 5 Most Mentioned Menu

![Top 5 Menus](outputs/top5_menus.png)

*Visualization of menu items receiving the highest customer discussion frequency, indicating strong customer attention and popularity.*

---

#### Top 5 Most Popular Restaurants

![Top 5 Restaurants](outputs/top5_restaurants.png)

*Comparison of restaurants based on total review volume, representing customer engagement and brand visibility.*

---

#### Menu Distribution Categories

![Category Distribution](outputs/category_distribution.png)

*Distribution of menu categories across the dataset, showing the balance between protein, carbohydrate, and complementary menu items.*

---

#### Price Segmentation

![Price Segmentation](outputs/price_segmentation.png)

*Visualization of price distribution patterns, highlighting the dominance of affordable menu pricing within the market.*

---

#### Rating Distribution

![Rating Distribution](outputs/rating_distribution.png)

*Distribution of restaurant ratings across the dataset, indicating overall customer satisfaction trends.*

---

## 🚀 How to Reproduce This Analysis

### Prerequisites

```bash
# Install Python dependencies
pip install -r requirements.txt

# MySQL database setup
mysql -u root -p < scripts/sql_analysis/database_schema.sql
```

### Run Python Analysis

```bash
cd scripts/python_visualization
python simple_analysis.py
```

### Run SQL Queries

```sql
USE malang_food_analysis;
SOURCE scripts/sql_analysis/simple_queries.sql;
```

---

## 📝 Learning Journey

This project represents my current learning journey in data analysis and reflects my practical experience working with real-world culinary datasets.

Through this project, I practiced:
- Data cleaning and preprocessing using Excel
- SQL querying and exploratory analysis using MySQL
- Data visualization and insight generation using Python
- Translating raw data into business-oriented insights

### Learning Philosophy

I believe in building strong fundamentals, documenting the learning process transparently, and continuously improving analytical thinking through hands-on projects.

---

## 📚 Methodology Documentation

Complete documentation of the learning and analysis process:

- [Excel Processing Steps](scripts/excel_cleaning/data_cleaning_steps.md)
- [SQL Learning Notes](scripts/sql_analysis/sql_learning_notes.md)
- [Python Learning Notes](scripts/python_visualization/python_learning_notes.md)

---

## 🤝 Contributing

This is a personal portfolio project. Feedback, suggestions, and discussions are welcome.

---

## 📄 License

This project is licensed under the MIT License — see the LICENSE file for details.

---

## 👨‍💻 Author

**Fahrul Fauji**

- Fresh Graduate in Information Technology
- Published Researcher in Data Clustering and Information Systems
- Research Publication: [Journal of Information System Research (JOSH)](https://doi.org/10.47065/josh.v6i3.6959)

### Connect With Me
- [GitHub](https://github.com/fahrulfauji)
- [LinkedIn](https://www.linkedin.com/in/fahrul-fauji-6729b8383/)

---

### 📌 Project Information

- Project Completion: January 2026
- Tools Used: Python, Excel, MySQL
- Dataset Type: Culinary Market Data

> *"Start simple, be honest, keep learning."*

---

## 🔗 Quick Links

- [View Full Project on GitHub](https://github.com/fahrulfauji/malang-food-analysis)

---

⭐ If you find this project interesting or useful, feel free to give it a star on GitHub.
