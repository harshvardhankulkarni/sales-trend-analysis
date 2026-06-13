"""
Sales Trend Analysis
Analyzes daily sales data with trend decomposition and forecasting.
Generates its own data. No external files needed.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Generate 180 days of synthetic sales data
np.random.seed(42)
dates = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(180)]

base_sales = 50000
trend = np.linspace(0, 20000, 180)
weekly_seasonality = 1 + 0.3 * np.sin(np.pi * np.arange(180) / 3.5)
weekend_boost = np.array([1.0, 1.0, 1.0, 1.1, 1.2, 1.5, 1.3])  # Mon-Sun
day_of_week = [d.weekday() for d in dates]
day_factors = [weekend_boost[dow] for dow in day_of_week]
noise = np.random.normal(0, 5000, 180)

sales = (base_sales + trend) * weekly_seasonality * np.array(day_factors) + noise
sales = np.maximum(sales, 10000).round(2)

data = {
    'date': dates,
    'sales': sales,
    'day_of_week': [d.strftime('%A') for d in dates],
    'month': [d.strftime('%B') for d in dates],
    'is_weekend': [1 if d.weekday() >= 5 else 0 for d in dates],
}

df = pd.DataFrame(data)

# Calculate rolling averages
df['7_day_avg'] = df['sales'].rolling(window=7).mean()
df['30_day_avg'] = df['sales'].rolling(window=30).mean()

# Month over month comparison
df['month_num'] = pd.to_datetime(df['date']).dt.month
monthly = df.groupby('month_num').agg(
    total_sales=('sales', 'sum'),
    avg_sales=('sales', 'mean'),
    order_count=('sales', 'count')
).round(2)

monthly['mom_change_pct'] = monthly['total_sales'].pct_change() * 100

# Day of week analysis
dow_analysis = df.groupby('day_of_week').agg(
    avg_sales=('sales', 'mean'),
    total_sales=('sales', 'sum')
).round(2)

day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dow_analysis = dow_analysis.reindex(day_order)

# Visualization
fig, axes = plt.subplots(3, 1, figsize=(14, 12))

# Plot 1: Daily sales with trend
axes[0].plot(df['date'], df['sales'], alpha=0.4, color='#3498db', linewidth=0.8, label='Daily Sales')
axes[0].plot(df['date'], df['7_day_avg'], color='#e74c3c', linewidth=2, label='7-Day Avg')
axes[0].plot(df['date'], df['30_day_avg'], color='#2ecc71', linewidth=2, label='30-Day Avg')
axes[0].set_title('Daily Sales Trend with Rolling Averages')
axes[0].set_ylabel('Sales (INR)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Plot 2: Monthly comparison
months_short = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
axes[1].bar(months_short, monthly['total_sales'], color='#3498db', edgecolor='white')
axes[1].set_title('Monthly Sales')
axes[1].set_ylabel('Total Sales (INR)')
for i, v in enumerate(monthly['total_sales']):
    axes[1].text(i, v + 5000, f'Rs.{v/1000:.0f}K', ha='center')

# Plot 3: Day of week performance
axes[2].bar(dow_analysis.index, dow_analysis['avg_sales'], color='#9b59b6', edgecolor='white')
axes[2].set_title('Average Sales by Day of Week')
axes[2].set_ylabel('Average Sales (INR)')
axes[2].tick_params(axis='x', rotation=45)
for i, v in enumerate(dow_analysis['avg_sales']):
    axes[2].text(i, v + 500, f'Rs.{v:.0f}', ha='center')

plt.tight_layout()
plt.savefig('2_sales_trend_analysis.png', dpi=150, bbox_inches='tight')
print('Saved: 2_sales_trend_analysis.png')

# Print insights
print('\n--- SALES TREND ANALYSIS RESULTS ---')
print(f'Period: {df["date"].min().date()} to {df["date"].max().date()}')
print(f'Total days analyzed: {len(df)}')
print(f'Total revenue: Rs.{df["sales"].sum():,.0f}')
print(f'Average daily sales: Rs.{df["sales"].mean():,.0f}')
print(f'Peak day: Rs.{df["sales"].max():,.0f} on {df.loc[df["sales"].idxmax(), "date"].date()}')
print(f'Lowest day: Rs.{df["sales"].min():,.0f} on {df.loc[df["sales"].idxmin(), "date"].date()}')

best_day = dow_analysis['avg_sales'].idxmax()
worst_day = dow_analysis['avg_sales'].idxmin()
print(f'\nBest performing day: {best_day} (Rs.{dow_analysis.loc[best_day, "avg_sales"]:,.0f})')
print(f'Worst performing day: {worst_day} (Rs.{dow_analysis.loc[worst_day, "avg_sales"]:,.0f})')

if len(monthly) >= 2:
    latest_month = monthly.iloc[-1]
    prev_month = monthly.iloc[-2]
    change = latest_month['total_sales'] - prev_month['total_sales']
    pct = (change / prev_month['total_sales']) * 100
    direction = 'up' if change > 0 else 'down'
    print(f'\nMonth over month: {direction} {abs(pct):.1f}% (Rs.{abs(change):,.0f})')

print('\nAction: Schedule marketing pushes on low-performing days.')
print('Action: Investigate what drove peak days and replicate.')
print('Done.')

df.to_csv('sales_trend_output.csv', index=False)
print('\nExported: sales_trend_output.csv')
