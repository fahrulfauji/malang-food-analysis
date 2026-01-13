# 📊 Excel Data Processing - Complete Workflow

## 📁 Project Initialization

### 1. DATA COLLECTION (Manual)
- **Platform**: Google Maps
- **Method**: Manual scraping & recording
- **Duration**: 5 days
- **Output**: `Malang_City_Food_Record_Dataset_By_Google_Maps.xlsx`
- **Statistics**:
  - Total rows: 373 with headers
  - Total Data: 372
  - Unique restaurants: 89
  - Subdistricts covered: 5 (Lowokwaru, Blimbing, Klojen, Sukun, Kedungkandang)
  - Date collected: 9 September 2026

### 2. INITIAL EXCEL SETUP
**Step 1: Open Raw Data**
- Open `Dataset_Kota_Malang_By_Google_Maps.xlsx`
- Confirm data structure:
  ```
  Columns: No | Nama_Tempat | Kecamatan | Menu | Jumlah_Ulasan_Menu |Jumlah_Total_Ulasan | Rating | Harga_Minimal | Harga_Maksimal
  ```

**Step 2: Convert to Excel Table**
1. Select all data: `Ctrl + A`
2. Convert to Table: `Ctrl + T`
3. Table settings:
   - ☑️ "My table has headers"
   - Table name: `tbl_malang_food`
   - ☑️ "Filter Button"
   - Table Style: Choose preferred style
4. Click **OK**

**Step 3: Table Benefits Activated**
- Automatic column filtering
- Structured references
- Easy formula dragging
- Visual banding for readability

---

## 🧹 DATA CLEANING PROCESS

### 3. PRICE FORMAT STANDARDIZATION
**Problem Identified**: 
- Price columns show values like 1, 25, 50
- Actually represents thousands: 1 = Rp 1.000, 25 = Rp 25.000

**Solution Applied**:

**3.1 Add New Columns for Clean Prices**
1. Right-click column H (`Harga_Minimal`)
2. Select **Insert** → **Table Columns to the Right**
3. Name new column: `Harga_Min_Clean`
4. Repeat for column I → `Harga_Max_Clean`

**3.2 Apply Conversion Formula**
In cell J2 (first data row of `Harga_Min_Clean`):
```excel
=[@[Harga_Minimal]]*1000
```
- Press Enter
- Formula auto-fills to all rows in table

In cell K2 (first data row of `Harga_Max_Clean`):
```excel
=[@[Harga_Maksimal]]*1000
```
- Press Enter
- Auto-fill complete

**3.3 Format as Currency**
1. Select columns J and K
2. Right-click → **Format Cells**
3. Category: **Number**
4. Decimal places: 0
5. Use 1000 separator: ☑️
6. Symbol: **Rp** (Rupiah)

---

### 4. AVERAGE PRICE CALCULATION
**4.1 Add Average Price Column**
1. Right-click column K
2. **Insert** → **Table Columns to the Right**
3. Name: `Harga_Rata_Rata`

**4.2 Apply Average Formula**
In cell L2:
```excel
=([@[Harga_Min_Clean]]+[@[Harga_Max_Clean]])/2
```
- Auto-fills to all rows
- Format as Currency (same as step 3.3)

---

### 5. PRICE SEGMENTATION
**5.1 Create Price Category Column**
1. Right-click column L
2. **Insert** → **Table Columns to the Right**
3. Name: `Rentang_Harga`

**5.2 Apply Segmentation Logic**
In cell M2:
```excel
=IF([@[Harga_Rata_Rata]]<=25000,"Murah (<25K)",
    IF([@[Harga_Rata_Rata]]<=50000,"Sedang (25-50K)",
    "Mahal (>50K)"))
```

**Logic Breakdown**:
- IF price ≤ 25,000 → "Murah (<25K)"
- ELSE IF price ≤ 50,000 → "Sedang (25-50K)"
- ELSE → "Mahal (>50K)"

---

### 6. MENU CATEGORIZATION (MANUAL METHOD)

**6.1 Add Category Column**
1. Insert column after `Menu` (column L)
2. Name: `Kategori_Menu`

**6.2 Manual Categorization Strategy**
**Decision Framework**:
```
PROTEIN   = All animal-based items (ayam, bebek, ikan, seafood, daging, jeroan)
KARBO     = Carb-based main dishes (nasi, mie, bubur, soto, rawon, gulai)
PENDAMPING = Side dishes & accompaniments (sambal, sayur, tempe, tahu, snack)
```

**6.3 Efficient Manual Process**
1. **Sort by Menu**:
   - Click filter on `Menu` column
   - Sort A to Z
   - Similar items group together

2. **Batch Categorization**:
   - Find first "Sambal" entry
   - Type `PENDAMPING` in `Kategori_Menu`
   - Double-click fill handle (small square at cell corner)
   - All "Sambal" entries get same category

3. **Repeat for All Groups**:
   - Ayam entries → `PROTEIN`
   - Nasi entries → `KARBO`
   - Tempe entries → `PENDAMPING`
   - etc.

**6.4 Special Cases Handled**:
- "Chinese Food" → `KARBO` (assumption: rice/noodle based)
- "Babi Panggang" → `PROTEIN`
- "Dimsum" → `PENDAMPING`
- "Ceker" → `PROTEIN`
- "Belut" → `PROTEIN`

---

## 📈 DATA ANALYSIS IN EXCEL

### 7. PIVOT TABLE CREATION
**7.1 Insert Pivot Table**
1. Select any cell in table
2. **Insert** → **PivotTable**
3. Location: New Worksheet
4. Click **OK**

**7.2 Configure Pivot Fields**
```
ROWS: Kategori_Menu
VALUES:
  - Jumlah_Ulasan_Menu (Sum)
  - Harga_Rata_Rata (Average)
  - Menu (Count)
```

**7.3 Format Pivot Table**
1. **Design** tab → Choose a style
2. Right-click values → **Number Format**
3. Currency for prices, Number for counts

**7.4 Add Percentage Column**
1. Right-click Sum of Jumlah_Ulasan_Menu
2. **Show Values As** → **% of Grand Total**
3. Format as Percentage (1 decimal)

### 8. VISUALIZATION
**8.1 Create Pie Chart**
1. Select Pivot Table
2. **PivotTable Analyze** → **PivotChart**
3. Choose **Pie Chart**
4. Customize:
   - Title: "Distribusi Kategori Menu"
   - Data Labels: Show Percentage and Value
   - Colors: Distinct for each category

**8.2 Save Charts as Images**
1. Right-click chart → **Save as Picture**
2. Format: PNG
3. Name: `excel_pie_chart.png`

---

## ✅ DATA VALIDATION CHECKS

### 9. QUALITY ASSURANCE
**9.1 Spot Checks**
- Randomly check 10% of rows (38 rows)
- Verify categorization logic
- Confirm price calculations

**9.2 Logical Checks**
```excel
=COUNTIF([Harga_Min_Clean], ">" & [Harga_Max_Clean])
-- Should return 0 (min should not exceed max)

=COUNTIF([Rating], "<1") + COUNTIF([Rating], ">5")
-- Should return 0 (rating must be 1-5)
```

**9.3 Data Completeness**
- No blank cells in critical columns
- All 372 rows have complete data
- Categories assigned to all rows

---

## 📤 EXPORT PROCESS

### 10. PREPARE FOR EXPORT
**10.1 Convert Table to Range**
1. Select table
2. **Table Design** → **Convert to Range**
3. Click **Yes**

**10.2 Remove Formulas (Keep Values)**
1. Select columns with formulas (J, K, M, N)
2. **Copy** → **Paste Special** → **Values**
3. This prevents formula errors in CSV

### 11. SAVE AS CSV
**11.1 Export Settings**
1. **File** → **Save As**
2. Location: Project `data/processed/` folder
3. File name: `malang_food_clean.csv`
4. Save as type: **CSV UTF-8 (Comma delimited)**
5. Click **Save**

**11.2 Warning Handling**
- Excel warns about features not supported in CSV
- Click **Yes** to save only active sheet
- Click **OK** to keep format

### 12. VERIFY CSV FILE
**12.1 Open in Notepad++**
1. Open `Malang_City_Food_Dataset_Cleaned.csv` in Notepad++
2. Check:
   - First line has headers
   - Commas as delimiters
   - No extra quotes
   - UTF-8 encoding (bottom right)

**12.2 Quick Data Check**
- Lines count: 373 (1 header + 372 data)
- Column count: 14 columns
- Special characters preserved

---

## 📊 EXCEL ANALYSIS RESULTS

### 13. KEY FINDINGS FROM EXCEL
**13.1 Category Distribution**
```
Pendamping: 4,327 ulasan (38.6%) - Rp 32,779 avg - 131 menu
Protein:    3,548 ulasan (31.6%) - Rp 36,652 avg - 132 menu  
Karbo:      3,346 ulasan (29.8%) - Rp 35,335 avg - 109 menu
Total:     11,221 ulasan (100%)  - Rp 34,902 avg - 372 menu
```

**13.2 Quick Insights**
1. **Pendamping dominates**: Sambal & side dishes most discussed
2. **Protein most expensive**: Average Rp 36,652
3. **Balanced menu count**: Each category has 109 - 132 items
4. **Price segmentation**: Majority in Murah & Sedang categories

---

## 📝 DOCUMENTATION FILES CREATED

### 14. SAVE EXCEL WORKBOOK
1. **File** → **Save As**
2. Name: `Malang_City_Food_Dataset_Cleaned.xlsx`
3. Location: Project root folder
4. Includes: Raw data, cleaned data, pivot tables, charts

### 15. CREATE DOCUMENTATION
File: `scripts/excel_cleaning/data_cleaning_steps.md`
- Contains this complete workflow
- Formulas used
- Decisions made
- Results obtained

---

## 🖼️ Excel Analysis Screenshots

### Pivot Table Summary
![Excel Pivot Table](excel_screenshots/04_pivot_table_results.png)
*Pivot table menunjukkan distribusi kategori menu*

### Pie Chart Visualization  
![Excel Pie Chart](excel_screenshots/05_pie_chart_excel.png)
*Visualisasi distribusi kategori dalam bentuk pie chart*

---