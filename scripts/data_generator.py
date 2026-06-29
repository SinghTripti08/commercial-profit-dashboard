import os
import pandas as pd
import numpy as np

# Ensure data directory exists
os.makedirs('data', exist_ok=True)

# Set random seed for reproducibility (aligned with alignment/balance)
np.random.seed(44)

# Configuration
num_rows = 1000
regions = ['North America', 'EMEA', 'APAC', 'LATAM']
categories = ['Enterprise Software', 'Cloud Infrastructure', 'Hardware Systems', 'Consulting Services']
sales_teams = [f'Team {alpha}' for alpha in ['Alpha', 'Beta', 'Gamma', 'Delta']]

# Generate Mock Sales Data
df_sales = pd.DataFrame({
    'TransactionID': range(10001, 10001 + num_rows),
    'Date': pd.date_range(start='2025-01-01', periods=num_rows, freq='h'),
    'Region': np.random.choice(regions, size=num_rows),
    'Category': np.random.choice(categories, size=num_rows),
    'SalesTeam': np.random.choice(sales_teams, size=num_rows),
    'Revenue': np.round(np.random.uniform(5000, 75000, size=num_rows), 2)
})

# Add COGS (Cost of Goods Sold) ensuring realistic, fluctuating profit margins
df_sales['COGS'] = np.round(df_sales['Revenue'] * np.random.uniform(0.4, 0.75, size=num_rows), 2)

# Generate Supply Chain/Operational Cost data
df_costs = pd.DataFrame({
    'Region': regions,
    'SupplyChainCosts': [1200000, 950000, 1500000, 600000]
})

# Save to CSV
df_sales.to_csv('data/raw_sales_data.csv', index=False)
df_costs.to_csv('data/supply_chain_costs.csv', index=False)

print("✅ Corporate financial mock datasets successfully generated in /data/ folder.")
