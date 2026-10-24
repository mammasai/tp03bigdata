# 📊 Big Data Analytics - Task 2: Data Visualization & Dashboarding Report

**Student Name:** Mamma Sai  
**Course:** Big Data Analytics / Master 2 Artificial Intelligence  
**Institution:** Université Hamma Lakhder - El Oued  
**Dataset:** Superstore Retail Sales Dataset  
**Tools Used:** Power BI Desktop, Power Query, DAX (Data Analysis Expressions)  

---

## 1. Executive Summary
This project aims to build an interactive Data Visualization Dashboard using **Power BI Desktop** to analyze business performance metrics for a retail corporation (Superstore Dataset). The report covers the end-to-end business intelligence pipeline, including data extraction, data cleaning/transformation, custom metric engineering via DAX formulas, interactive visualization design, and key strategic findings.

---

## 2. Data Extraction & Transformation (ETL Process)

### 2.1 Dataset Overview
The dataset contains transaction records across multiple regions, product categories, and customer segments. The primary features analyzed include:
* **Categorical Dimensions:** `Category`, `SubCategory`, `Region`, `State`, `City`, `Segment`, `Ship Mode`.
* **Quantitative Measures:** `Sales`, `Profit`, `Quantity`, `Discount`.
* **Temporal Attributes:** `Order Date`, `Ship Date`.

### 2.2 Data Cleaning & Power Query Pipeline
During the initial data intake into Power BI, several data quality issues were addressed:
1. **Data Type Correction:** Key numerical fields (`Sales`, `Profit`, `Discount`) were converted from string/text format (`String`) to double-precision floating numbers (`Decimal Number`) using Power Query Editor.
2. **Missing Values & Consistency:** Verified zero null values across critical transactional IDs (`Order ID`, `Customer ID`).
3. **Data Formatting:** Standardized currency representations and rounded profit percentages for optimal visualization display.

---

## 3. Data Modeling & DAX Measures

To evaluate Key Performance Indicators (KPIs), custom **DAX (Data Analysis Expressions)** measures were implemented:

1. **Total Sales:**
   $$\text{Total Sales} = \text{SUM}(\text{Superstore}[Sales])$$

2. **Total Profit:**
   $$\text{Total Profit} = \text{SUM}(\text{Superstore}[Profit])$$

3. **Total Quantity Sold:**
   $$\text{Total Quantity} = \text{SUM}(\text{Superstore}[Quantity])$$

4. **Total Orders Count:**
   $$\text{Total Orders} = \text{DISTINCTCOUNT}(\text{Superstore}[Order ID])$$

5. **Profit Margin Percentage:**
   $$\text{Profit Margin \%} = \text{DIVIDE}([\text{Total Profit}], [\text{Total Sales}], 0)$$

6. **Average Discount:**
   $$\text{Avg Discount \%} = \text{AVERAGE}(\text{Superstore}[Discount])$$

---

## 4. Dashboard Architecture & Visual Elements

The dashboard is structured into three main visual zones for intuitive user navigation:

### A. Executive KPI Cards (Top Banner)
* **Total Sales Card:** Highlights top-line revenue generated.
* **Total Profit Card:** Displays net profit achieved.
* **Total Orders & Quantity Cards:** Tracks transaction volumes.
* **Profit Margin Card:** Indicates overall business operational efficiency.

### B. Visual Analytical Charts
1. **Sales & Profit by Category (Clustered Bar Chart):**
   * *Purpose:* Identifies the most and least profitable product categories (Technology, Office Supplies, Furniture).
2. **Sales Trend Over Time (Line Chart):**
   * *Purpose:* Tracks revenue dynamics month-by-month to observe seasonality and annual growth patterns.
3. **Profitability by Region (Donut / Pie Chart):**
   * *Purpose:* Compares geographic contribution across Central, East, South, and West sales zones.
4. **Top 10 Sub-Categories by Revenue (Horizontal Bar Chart):**
   * *Purpose:* Pinpoints specific high-value inventory items driving total sales.

### C. Interactive Filtering (Slicers)
* **Region Slicer:** Allows dynamic filtering by geographical territory.
* **Date / Year Slicer:** Enables temporal comparative analysis across financial years.

---

## 5. Key Analytical Findings & Business Insights

1. **Category Performance:** Technology leads in profitability, while Furniture exhibits high overall revenue but lower profit margins due to higher logistical and discount costs.
2. **Seasonal Spikes:** Revenue spikes consistently towards Q4 (October – December), aligning with seasonal holiday purchasing patterns.
3. **Geographic Distribution:** The West and East regions account for the highest share of both total sales and net profit margins.

---

## 6. Conclusion

The developed Power BI dashboard successfully translates raw tabular data into actionable business intelligence. By leveraging Power Query for robust ETL workflows and DAX for dynamic computations, the interactive report enables stakeholders to evaluate performance metrics effortlessly and make data-driven decisions.