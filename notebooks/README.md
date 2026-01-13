# 📓 Notebooks Folder

This folder is reserved for Jupyter Notebooks when advanced interactive analysis is required.

## Current Project Structure
For this project, analysis was conducted using:
- **Python scripts** in `scripts/python_visualization/`
- **SQL files** in `scripts/sql_analysis/`
- **Excel documentation** in `scripts/excel_cleaning/`

## Why Scripts Instead of Notebooks?
For this beginner-level portfolio project, I chose to use traditional Python scripts (.py files) instead of Jupyter Notebooks (.ipynb) for several reasons:

### 1. Version Control Friendly
- Scripts are easier to track with Git
- Clear line-by-line changes in commits
- No JSON conflicts (common with .ipynb files)

### 2. Reproducibility
- Scripts run sequentially from top to bottom
- No hidden state issues
- Easier to automate and schedule

### 3. Learning Focus
- As a beginner, mastering fundamental scripting is important
- Scripts encourage structured, modular code
- Better preparation for production environments

### 4. Portfolio Presentation
- Scripts demonstrate coding discipline
- Easier for reviewers to read and understand
- Shows ability to work in different development environments

## Analysis Files Location
All analysis code is available in these locations:

### Python Analysis:
- `scripts/python_visualization/simple_analysis.py` - Main analysis script
- `scripts/python_visualization/requirements.txt` - Dependencies

### SQL Analysis:
- `scripts/sql_analysis/database_schema.sql` - Database setup
- `scripts/sql_analysis/simple_queries.sql` - SQL queries
- `scripts/sql_analysis/import_instructions.md` - Data import guide

### Excel Processing:
- `scripts/excel_cleaning/data_cleaning_steps.md` - Complete workflow documentation

## When Would I Use Jupyter Notebooks?
Jupyter Notebooks would be appropriate for:

### Exploratory Data Analysis (EDA)
- Initial data exploration
- Quick prototyping of visualizations
- Interactive data manipulation

### Teaching/Demonstration
- Step-by-step tutorials
- Code + explanation in one place
- Interactive learning materials

### Research Projects
- Experimental analysis
- Iterative model development
- Sharing research findings with narrative

## Future Use of This Folder
This folder can be used for:

1. **Interactive data exploration notebooks**
2. **Machine learning experiments**
3. **Advanced statistical analysis**
4. **Interactive data visualization demos**
5. **Tutorials and learning materials**

## Current Project Outputs
The analysis from this project generated:
- **5 Python visualizations** in `outputs/` folder
- **SQL query results** in `scripts/sql_analysis/query_results/`
- **Business insights** in `insights/` folder
- **Complete documentation** in README and script files

## How to Convert to Notebooks (If Needed)
If Jupyter Notebook format is preferred in the future:

```bash
# Convert Python script to notebook
jupyter nbconvert --to notebook scripts/python_visualization/simple_analysis.py --output notebooks/analysis.ipynb

# Or create new notebook and copy code cells
# 1. Launch Jupyter: jupyter notebook
# 2. Create new Python notebook
# 3. Copy code from simple_analysis.py
# 4. Add markdown cells for documentation
```

## Learning Path
As I advance in data analysis, I plan to:
1. Master script-based analysis (current level)
2. Learn Jupyter Notebooks for exploratory work
3. Use both tools appropriately for different tasks
4. Develop hybrid workflows that leverage both approaches

---
*This project uses script-based analysis to demonstrate fundamental data analysis skills. The choice reflects a deliberate learning approach focused on building strong foundations before exploring more interactive tools.*

**Project completed: January 2026**  
**Tools: Python 3.13.7 | Excel LTSC 2024 | MySQL Workbench 8.0 CE**

---