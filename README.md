# Sales Trend Analysis - Demo Project

Analyze 180 days of daily sales data. Identify trends, seasonal patterns, and day-of-week performance. Use the insights to optimize marketing spend and staffing.

This is a demo project using synthetic data to demonstrate time series analysis techniques.

## Problem

Businesses collect sales data every day but rarely analyze it systematically. Without trend analysis, you cannot tell if revenue is growing or declining. You cannot identify your best and worst days. You make decisions on gut feelings instead of numbers.

## Approach

Generated 180 days of synthetic daily sales data with built-in trends and seasonality:

- **Base trend**: Revenue grows linearly over 180 days.
- **Weekly seasonality**: Cyclical pattern repeating every 7 days.
- **Day-of-week effect**: Weekend days get higher traffic.
- **Random noise**: Realistic day-to-day variation.

Calculated 7-day and 30-day rolling averages to smooth noise. Compared month-over-month performance. Ranked days of week by average revenue.

## Results

- Total revenue over 180 days: Rs.12,134,670.
- Average daily revenue: Rs.67,415.
- Best performing day: Wednesday (Rs.76,430 average).
- Worst performing day: Monday (Rs.58,829 average).
- Revenue declined 3.3% from month 5 to month 6.

## Actions

1. Shift marketing budget from peak days to low days. Monday and Tuesday need the most push.
2. Study what made Wednesdays perform well. Replicate that playbook.
3. Investigate the month-over-month decline before it becomes a trend.

## How to Run

```bash
pip install pandas matplotlib numpy
python 2_sales_trend_analysis.py
```

Output: `2_sales_trend_analysis.png` (chart) and `sales_trend_output.csv` (daily data with averages).

## Tech Stack

Python, Pandas, NumPy, Matplotlib

## License

MIT
