#  Store Sales & Profit Analysis Dashboard using Python

##  Problem Statement

Analyzing the sales and profit performance of a retail store is essential for businesses aiming to optimize operations, refine pricing strategies, enhance marketing efforts, and improve inventory management.

This project focuses on building an **interactive data-driven dashboard** using Python to analyze retail sales data and generate actionable business insights that support strategic decision-making.

---

##  Project Objectives

- Analyze overall sales and profit performance
- Track sales trends over time
- Identify top-performing and underperforming categories
- Compare performance across regions
- Evaluate customer segment contributions
- Visualize Sales vs Profit relationships
- Generate actionable business insights

---

##  Dataset Information

The dataset contains retail store transaction data including:

- Order Details
- Sales Amount
- Profit
- Product Category & Sub-Category
- Region
- Customer Segment
- Quantity
- Order Date
 Dataset Source: Provided in internship task instructions (Google Drive link)

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Dash (Flask-based interactive dashboard framework)

---

##  Project Workflow

### 1️⃣ Data Collection
- Loaded dataset using Pandas
- Verified structure, columns, and data types

### 2️⃣ Data Cleaning
- Checked and handled missing values
- Removed duplicates
- Converted data types where necessary
- Ensured consistency in categorical values

### 3️⃣ Exploratory Data Analysis (EDA)
- Calculated Total Sales and Total Profit
- Computed Profit Margin
- Category-wise sales analysis
- Region-wise performance evaluation
- Segment-wise contribution analysis
- Time-based sales trend analysis

### 4️⃣ Dashboard Development
Built an interactive dashboard with:

- Category filter dropdown
- Region filter dropdown
- Dynamic KPI updates
- Interactive visualizations

---

##  Dashboard Features

### 🔹 Key Metrics
- Total Sales
- Total Profit
- Profit Margin (%)

### 🔹 Interactive Filters
- Category Selector
- Region Selector

### 🔹 Visualizations
-  Sales Trend Over Time (Line Chart)
-  Sales by Segment (Donut Chart)
-  Sales vs Profit Analysis (Bubble Chart – Bubble size represents Quantity)

---

##  How to Run the Project

### Step 1: Clone the Repository
```bash
git clone https://github.com/EvanKS/ShadowFox.git
```

### Step 2: Navigate to Task Folder
```bash
cd Task2_Intermediate_Store_Sales_And_Profit_Analysis
```

### Step 3: Install Required Libraries
```bash
pip install -r requirements.txt
```

### Step 4: Run the Dashboard
```bash
python store_analysis/dashboard.py
```

### Step 5: Open in Browser
```
http://127.0.0.1:8050/
```

The interactive dashboard will launch locally.

---

##  Project Structure

```
Task2_Intermediate_Store_Sales_And_Profit_Analysis/
│
├── store_analysis/
│   ├── dashboard.py
│   ├── data_processing.py
│   └── (supporting files)
│
├── create_dummy_data_v2.py
├── requirements.txt
└── README.md
```

---

##  Key Insights

- Technology category shows strong revenue generation.
- Regional performance varies significantly.
- Some high-sales products operate with lower profit margins.
- Consumer segment contributes a major portion of revenue.
- Certain sub-categories show inefficiencies in profit performance.
- Sales trends fluctuate over time indicating seasonal patterns.

---

##  Business Recommendations

- ptimize pricing strategies for low-margin high-sales products.
- Increase focus on high-performing regions.
- Improve inventory planning using sales trend data.
- Re-evaluate cost structure for underperforming categories.
- Target marketing campaigns based on profitable segments.

---

##  Conclusion

This project demonstrates the practical implementation of retail data analysis and interactive dashboard development using Python and Dash.

By transforming raw sales data into meaningful visual insights, the dashboard enables better strategic decision-making and improved business performance.

The project highlights the power of data-driven analysis in optimizing operations and maximizing profitability.

---

##  Author

**Evan KS**  
AIML Intern – ShadowFox  
