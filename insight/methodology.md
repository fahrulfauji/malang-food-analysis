# 🔬 Methodology & Analysis Approach

## Research Design

### 1. Data Collection
- **Source**: Google Maps restaurant listings
- **Method**: Manual data extraction
- **Scope**: Kota Malang (5 kecamatan (subdistrict))
- **Timeframe**: September 2025
- **Sample Size**: 89 restaurants, 372 menu items

### 2. Data Variables Collected

| Variable        |       Type 		 |              Description 		    |
|-----------------|------------------|--------------------------------------|
| Restaurant Name | Text             | Name of eating establishment 		|
| subdistrict     | Text             | Kecamatan location 					|
| Menu Item       | Text             | Specific food/drink item 			|
| Menu Reviews    | Integer          | Number of mentions for specific menu |
| Total Reviews   | Integer          | Total reviews for restaurant 		|
| Rating          | Decimal          | Average rating (1-5 scale) 		    |
| Price Range     | Text             | Minimum and maximum price 			|
| Category        | Text             | Menu classification 					|

### 3. Analysis Framework

#### Phase 1: Descriptive Analysis
- **Objective**: Understand data characteristics
- **Methods**: Counts, percentages, averages
- **Output**: Basic statistics and distributions

#### Phase 2: Comparative Analysis
- **Objective**: Identify patterns and differences
- **Methods**: Group comparisons, ranking
- **Output**: Top performers, category comparisons

#### Phase 3: Insight Generation
- **Objective**: Derive business implications
- **Methods**: Pattern recognition, correlation analysis
- **Output**: Actionable recommendations

## Analytical Tools & Techniques

### Excel Analysis:
- **Data Cleaning**: Text standardization, price conversion
- **Categorization**: Manual classification system
- **Pivot Tables**: Summary statistics by category
- **Basic Charts**: Pie charts for distribution visualization

### SQL Analysis:
- **Database Design**: Table structure creation
- **Data Import**: CSV to MySQL import process
- **Basic Queries**: SELECT, COUNT, GROUP BY, ORDER BY
- **Aggregation**: SUM, AVG, MAX functions

### Python Analysis:
- **Data Loading**: pandas read_csv function
- **Exploration**: Shape, unique counts, basic stats
- **Visualization**: matplotlib and seaborn charts
- **Insight Generation**: Pattern identification from visuals

## Quality Assurance

### Data Validation:
1. **Completeness Check**: No missing values in key columns
2. **Consistency Check**: Rating within 1-5 range, prices logical
3. **Accuracy Check**: Random sample verification
4. **Logic Check**: Minimum price ≤ maximum price

### Analysis Validation:
1. **Cross-Tool Verification**: Excel vs SQL vs Python results
2. **Manual Calculation**: Spot check of calculations
3. **Sensitivity Analysis**: Check for outliers impact
4. **Peer Review**: Methodology review for logical consistency

## Limitations & Assumptions

### Data Limitations:
1. **Sample Bias**: Only restaurants on Google Maps included
2. **Time Constraint**: Snapshot data, not longitudinal
3. **Review Bias**: Reviews may not represent all customers
4. **Price Interpretation**: Assumes prices in thousands of Rupiah

### Analytical Limitations:
1. **Beginner Level**: Basic analytical techniques used
2. **Tool Constraints**: Limited to available software
3. **Scope Constraints**: Focus on descriptive analysis only
4. **Experience Level**: First end-to-end analysis project

## Ethical Considerations

### Data Privacy:
- No personal customer data collected
- Only publicly available information used
- Restaurant names used with respect
- No sensitive business information disclosed

### Research Ethics:
- Transparent methodology documentation
- Honest representation of skill level
- Clear communication of limitations
- Educational purpose clearly stated

## Replication Instructions

### For Researchers:
1. Follow the documented data collection process
2. Use provided scripts for analysis
3. Adapt methodology as needed for different contexts
4. Document any modifications made

### For Students:
1. Study the learning documentation
2. Practice with provided datasets
3. Build upon this foundation with more advanced techniques
4. Always document your learning journey

---
*Methodology documented as part of learning process - January 2026*
