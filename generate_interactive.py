
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
dates = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(180)]
base = 50000
trend = np.linspace(0, 20000, 180)
weekly = 1 + 0.3 * np.sin(np.pi * np.arange(180) / 3.5)
wknd = np.array([1.0, 1.0, 1.0, 1.1, 1.2, 1.5, 1.3])
day_factors = [wknd[d.weekday()] for d in dates]
noise = np.random.normal(0, 5000, 180)
sales = np.maximum((base + trend) * weekly * np.array(day_factors) + noise, 10000).round(2)

df = pd.DataFrame({'date': dates, 'sales': sales})
df['7d'] = df['sales'].rolling(7).mean()
df['30d'] = df['sales'].rolling(30).mean()
df['dow'] = [d.strftime('%A') for d in dates]

fig = make_subplots(rows=3, cols=1, subplot_titles=('Daily Sales Trend', 'Monthly Sales', 'Avg by Day of Week'))

fig.add_trace(go.Scatter(x=df['date'], y=df['sales'], mode='lines', name='Daily',
                         line=dict(color='#3498db', width=0.8), opacity=0.4), row=1, col=1)
fig.add_trace(go.Scatter(x=df['date'], y=df['7d'], mode='lines', name='7-Day Avg',
                         line=dict(color='#e74c3c', width=2)), row=1, col=1)
fig.add_trace(go.Scatter(x=df['date'], y=df['30d'], mode='lines', name='30-Day Avg',
                         line=dict(color='#2ecc71', width=2)), row=1, col=1)

df['month'] = pd.to_datetime(df['date']).dt.month
monthly = df.groupby('month')['sales'].sum()
months_short = ['Jan','Feb','Mar','Apr','May','Jun']
fig.add_trace(go.Bar(x=months_short[:len(monthly)], y=monthly.values,
                     text=[f'Rs.{v/1000:.0f}K' for v in monthly.values],
                     textposition='outside', marker_color='#3498db', showlegend=False), row=2, col=1)

dow_avg = df.groupby('dow')['sales'].mean().reindex(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
fig.add_trace(go.Bar(x=dow_avg.index, y=dow_avg.values,
                     text=[f'Rs.{v:.0f}' for v in dow_avg.values],
                     textposition='outside', marker_color='#9b59b6', showlegend=False), row=3, col=1)

fig.update_layout(height=800, title_text='Sales Trend Analysis - Interactive', hovermode='x unified')
fig.write_html('2_sales_trend_interactive.html')
print('Saved: 2_sales_trend_interactive.html')
