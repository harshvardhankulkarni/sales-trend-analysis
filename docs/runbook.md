# Runbook: Sales Trend Analysis

## When to Use This Runbook

- First-time setup and execution.
- Re-running with modified parameters.
- Troubleshooting errors.

## Prerequisites

- Python 3.8+ installed.
- pip installed.

## Procedure

### Step 1: Install Dependencies

```bash
pip install pandas numpy matplotlib
```

### Step 2: Run the Analysis

```bash
cd path/to/sales-trend-analysis
python 2_sales_trend_analysis.py
```

### Step 3: Verify Output

Check for these files:

- `2_sales_trend_analysis.png` - 3-panel chart.
- `sales_trend_output.csv` - 180 rows with columns: date, sales, 7_day_avg, 30_day_avg.

### Step 4: Read the Report

Key numbers from the console output:

- Total revenue over 180 days.
- Average daily revenue.
- Best and worst days of the week.
- Month-over-month change direction.

### Step 5: Act on Insights

- If Monday and Tuesday are low, schedule marketing pushes on those days.
- If revenue is declining, investigate the cause before it accelerates.

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| No chart displayed | Missing matplotlib backend | Add `matplotlib.use('Agg')` before pyplot import |
| CSV empty | Script crashed before export | Check for error messages in console |
| Wrong date range | Modified date generation parameters | Reset to original values |
| Negative sales values | Noise too high | Reduce `noise` standard deviation |
| Plot text overlapping | Too many data points | Increase figure size or reduce DPI |

## Modifying Parameters

To test different scenarios, change these values:

```python
base_sales = 50000      # Base daily revenue
weekend_boost = [1.0, 1.0, 1.0, 1.1, 1.2, 1.5, 1.3]  # Mon-Sun multipliers
noise = np.random.normal(0, 5000, 180)  # Second param controls volatility
```

## Escalation

Open a GitHub issue with:

- Full console output.
- Python version.
- Any parameter changes made.
- Expected vs actual behavior.
