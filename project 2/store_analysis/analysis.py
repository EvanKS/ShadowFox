
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import os

# Set Plotly template
pio.templates.default = "plotly_white"

# ==========================================
# 1. Data Loading & Cleaning
# ==========================================
def load_and_clean_data(filepath):
    """
    Loads dataset, converts dates, handles missing values, and treats outliers.
    """
    if not os.path.exists(filepath):
        print(f"❌ Error: File '{filepath}' not found. Please place the dataset in the 'store_analysis/data/' directory.")
        return None

    try:
        # Try reading as CSV first, then Excel
        if filepath.endswith('.csv'):
            df = pd.read_csv(filepath, encoding='latin1') 
        else:
            df = pd.read_excel(filepath)
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return None

    # Dataset Overview
    print("\n📋 --- DATASET OVERVIEW ---")
    print(f"Shape: {df.shape}")
    print("Columns:", df.columns.tolist())
    print("-" * 30)

    # Date Conversion
    if 'Order Date' in df.columns:
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        df['Year'] = df['Order Date'].dt.year
        df['Month'] = df['Order Date'].dt.month_name()
        df['Quarter'] = df['Order Date'].dt.to_period('Q').astype(str)
        df['Month_Num'] = df['Order Date'].dt.month # Helper for sorting
    
    # Missing Values
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print("\n⚠️ Missing Values Detected:\n", missing[missing > 0])
        df.dropna(inplace=True) 
        print("✅ Missing values handled (rows dropped).")

    # Outlier Detection (Profit) - IQR
    Q1 = df['Profit'].quantile(0.25)
    Q3 = df['Profit'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Flag Outliers
    df['Is_Outlier'] = ~df['Profit'].between(lower_bound, upper_bound)
    print(f"ℹ️ Outliers detected: {df['Is_Outlier'].sum()} rows.")
    
    return df

# ==========================================
# 2. Sales Analysis
# ==========================================
def analyze_sales(df):
    print("\n📊 --- SALES ANALYSIS ---")
    
    # Monthly Trends
    monthly = df.groupby(['Year', 'Month_Num', 'Month'])['Sales'].sum().reset_index().sort_values(['Year', 'Month_Num'])
    peak_month = monthly.loc[monthly['Sales'].idxmax()]
    
    print(f"📅 Peak Sales Month: {peak_month['Month']} {peak_month['Year']} (${peak_month['Sales']:,.2f})")
    
    # Category Analysis
    cat_sales = df.groupby('Category')['Sales'].sum().reset_index().sort_values('Sales', ascending=False)
    
    # Top 10 Products
    top_products = df.groupby('Product Name')['Sales'].sum().nlargest(10).reset_index()
    
    print("🏆 Top 3 Best-Selling Products:")
    for i, row in top_products.head(3).iterrows():
        print(f"   {i+1}. {row['Product Name']} (${row['Sales']:,.2f})")
        
    return monthly, cat_sales, top_products

# ==========================================
# 3. Profit Analysis
# ==========================================
def analyze_profit(df):
    print("\n💰 --- PROFIT ANALYSIS ---")
    
    # Profit Trends
    year_profit = df.groupby('Year')['Profit'].sum().reset_index()
    
    # Most/Least Profitable Sub-Categories
    sub_profit = df.groupby('Sub-Category')['Profit'].sum().reset_index().sort_values('Profit', ascending=False)
    
    print(f"✅ Most Profitable Sub-Category: {sub_profit.iloc[0]['Sub-Category']} (${sub_profit.iloc[0]['Profit']:,.2f})")
    print(f"❌ Least Profitable Sub-Category: {sub_profit.iloc[-1]['Sub-Category']} (${sub_profit.iloc[-1]['Profit']:,.2f})")
    
    return year_profit, sub_profit

# ==========================================
# 4. Customer Segment Analysis
# ==========================================
def analyze_segments(df):
    print("\n👥 --- CUSTOMER SEGMENT ANALYSIS ---")
    
    grouped = df.groupby('Segment')[['Sales', 'Profit']].sum().reset_index()
    grouped['Profit_Margin'] = (grouped['Profit'] / grouped['Sales']) * 100
    
    for i, row in grouped.iterrows():
        print(f"   • {row['Segment']}: Sales=${row['Sales']:,.0f} | Profit=${row['Profit']:,.0f} | Margin={row['Profit_Margin']:.1f}%")
        
    return grouped

# ==========================================
# 5. Operational Insights
# ==========================================
def operational_insights(df):
    print("\n💡 --- OPERATIONAL INSIGHTS ---")
    
    # High Sales, Low Profit Areas
    # Aggregating by Sub-Category
    ops = df.groupby('Sub-Category')[['Sales', 'Profit']].sum().reset_index()
    ops['Profit_Ratio'] = ops['Profit'] / ops['Sales']
    
    loss_makers = ops[ops['Profit'] < 0].sort_values('Profit')
    
    if not loss_makers.empty:
        print("⚠️ ACTION REQUIRED: The following sub-categories are generating losses:")
        for i, row in loss_makers.iterrows():
            print(f"   - {row['Sub-Category']}: Loss = ${abs(row['Profit']):,.2f}")
            
    # Recommendations
    print("\n🚀 RECOMMENDATIONS:")
    print("1. Review pricing strategy for loss-making sub-categories (tables/machines often have high shipping costs).")
    print("2. Focus marketing on high-margin segments (Consumer/Home Office often vary).")
    print("3. Analyze if deep discounts are eroding profits in specific regions.")

# ==========================================
# 6. Visualization
# ==========================================
def visualize_results(monthly_sales, cat_sales, sub_profit, segment_data):
    # 1. Sales Trend
    fig1 = px.line(monthly_sales, x='Month', y='Sales', color='Year', markers=True, 
                   title='📈 Monthly Sales Trend Comparison')
    fig1.show()
    
    # 2. Category Sales
    fig2 = px.bar(cat_sales, x='Category', y='Sales', 
                  title='📦 Total Sales by Category', text_auto='.2s', color='Sales')
    fig2.show()
    
    # 3. Sub-Category Profit
    sub_profit['Color'] = sub_profit['Profit'].apply(lambda x: 'Profit' if x>0 else 'Loss')
    fig3 = px.bar(sub_profit, x='Profit', y='Sub-Category', orientation='h', color='Color',
                  title='📊 Net Profit by Sub-Category',
                  color_discrete_map={'Profit': '#2ecc71', 'Loss': '#e74c3c'})
    fig3.show()
    
    # 4. Segment Contribution
    fig4 = px.pie(segment_data, values='Sales', names='Segment', 
                  title='🍰 Sales Contribution by Customer Segment', hole=0.3)
    fig4.show()

# ==========================================
# Main Execution
# ==========================================
if __name__ == "__main__":
    DATA_PATH = "store_analysis/data/store_data.csv"
    
    print("🔄 Initializing Analysis...")
    
    # Load
    df = load_and_clean_data(DATA_PATH)
    
    if df is not None:
        # Analyze
        monthly, cats, top10 = analyze_sales(df)
        yr_prof, sub_prof = analyze_profit(df)
        segs = analyze_segments(df)
        operational_insights(df)
        
        # Visualize
        print("\n🎨 Opening Visualizations...")
        visualize_results(monthly, cats, sub_prof, segs)
        print("\n✅ Project execution complete.")
