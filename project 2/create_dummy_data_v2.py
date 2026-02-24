
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Ensure directory exists
os.makedirs("store_analysis/data", exist_ok=True)

# Create dummy data
np.random.seed(42)
num_rows = 1000

data = {
    'Order Date': [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 365*2)) for _ in range(num_rows)],
    'Sales': np.random.uniform(10, 1000, num_rows).round(2),
    'Profit': np.random.uniform(-100, 300, num_rows).round(2),
    'Category': np.random.choice(['Furniture', 'Office Supplies', 'Technology'], num_rows),
    'Sub-Category': np.random.choice(['Chairs', 'Tables', 'Binders', 'Paper', 'Phones', 'Accessories'], num_rows),
    'Segment': np.random.choice(['Consumer', 'Corporate', 'Home Office'], num_rows),
    'Region': np.random.choice(['East', 'West', 'Central', 'South'], num_rows),
    'Product Name': [f'Product {i}' for i in range(num_rows)],
    'Quantity': np.random.randint(1, 10, num_rows),
    'Discount': np.random.choice([0, 0.1, 0.2, 0.3], num_rows)
}

df = pd.DataFrame(data)

# Save to CSV in the correct location
filename = "store_analysis/data/store_data.csv"
df.to_csv(filename, index=False)
print(f"✅ Created dummy dataset '{filename}' with {num_rows} rows.")
