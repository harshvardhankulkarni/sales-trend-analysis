# Architecture: Sales Trend Analysis

## Context

Businesses collect daily sales data but rarely use it to make decisions. Trend analysis reveals whether revenue is growing, which days perform best, and where marketing spend should go.

## Goals

- Identify revenue trends over a 180-day period.
- Detect day-of-week performance patterns.
- Calculate rolling averages for noise reduction.
- Produce actionable recommendations.

## Design

### Data Flow

```
Synthetic Data Generator
  - Base trend (linear growth)
  - Weekly seasonality (sine wave)
  - Day-of-week effect (multipliers)
  - Random noise (normal distribution)
        |
        v
Daily Sales DataFrame (180 rows)
        |
        +---> 7-day rolling average
        +---> 30-day rolling average
        +---> Month-over-month comparison
        +---> Day-of-week aggregation
        |
        v
Visualization (3-panel chart) + CSV Export
```

### Key Formulas

```python
# Synthetic sales generation
sales = (base_sales + trend) * weekly_seasonality * day_of_week_factor + noise

# Rolling averages
df['7_day_avg'] = df['sales'].rolling(window=7).mean()
df['30_day_avg'] = df['sales'].rolling(window=30).mean()

# Month-over-month change
monthly['mom_change_pct'] = monthly['total_sales'].pctchange() * 100
```

### Visualization Layout

```
Panel 1: Daily sales line chart with 7-day and 30-day overlays
Panel 2: Monthly bar chart
Panel 3: Day-of-week bar chart
```

## Key Decisions

| Decision | Rationale |
|----------|-----------|
| 180-day window | Long enough for trend detection. Short enough for quick runs. |
| 7-day and 30-day averages | Industry standard. 7-day removes weekly noise. 30-day shows direction. |
| Synthetic data | No external files needed. Fully reproducible. |
| Day-of-week multipliers | Matches real-world patterns (weekends higher). |

## Trade-offs

- **Synthetic vs real data**: Real data would require CSV import, date parsing, and missing value handling. The trade-off is convenience vs realism.
- **Linear trend assumption**: Real trends are rarely linear. Polynomial or exponential fits could be more accurate but need more data.
- **Static analysis**: No forecasting. Extending to predict future sales would require ARIMA or Prophet.

## Integration Points

- **Input**: Self-generates data. Replace with `pd.read_csv('real_sales.csv')` for real data.
- **Output**: `sales_trend_output.csv` can feed into BI tools (Power BI, Tableau) or reporting systems.

## Dependencies

- Python 3.8+
- pandas, numpy, matplotlib

No external APIs or databases.
