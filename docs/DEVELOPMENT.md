<!-- GSD -->
# Development: Sales Trend Analysis

## Project Structure

```
sales-trend-analysis/
  Source scripts
    2_sales_trend_analysis.py      Main analysis (data gen + static viz + CSV)
    generate_interactive.py        Plotly interactive HTML version
    2_sales_trend_analysis.ipynb   Jupyter notebook

  Output (generated)
    sales_trend_output.csv          180-row dataset with computed columns
    2_sales_trend_analysis.png      Static 3-panel chart
    2_sales_trend_interactive.html  Interactive Plotly chart

  Web
    index.html                      GitHub Pages landing page

  Documentation
    README.md                       Project overview
    docs/ARCHITECTURE.md            Design and methodology
    docs/GETTING-STARTED.md         Installation and first run
    docs/DEVELOPMENT.md             This file
    docs/TESTING.md                 Validation procedures
    docs/CONFIGURATION.md           Parameters reference
```

## How to Modify

### Change the analysis period

In `2_sales_trend_analysis.py`, update the range parameter:

```python
dates = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(180)]
# Change 180 to 365 for a full year
```

Update the trend array to match:

```python
trend = np.linspace(0, 20000, 180)  # Must match number of days
```

### Add a new metric

Example: add a 14-day rolling average.

In `2_sales_trend_analysis.py`, after line 39:

```python
df['14_day_avg'] = df['sales'].rolling(window=14).mean()
```

Add it to the visualization (around line 64-70):

```python
axes[0].plot(df['date'], df['14_day_avg'], color='#f39c12', linewidth=1.5, label='14-Day Avg')
```

### Add a new visualization panel

Increment the subplot count from 3 to 4:

```python
fig, axes = plt.subplots(4, 1, figsize=(14, 16))
```

Plot on the fourth axis:

```python
axes[3].plot(df['date'], df['sales'].rolling(14).std(), color='#e67e22')
axes[3].set_title('14-Day Rolling Volatility')
```

### Modify the interactive version

Edit `generate_interactive.py`. The structure mirrors the main script but uses Plotly:

```python
fig.add_trace(go.Scatter(..., row=1, col=1))  # Daily sales
fig.add_trace(go.Bar(..., row=2, col=1))       # Monthly
fig.add_trace(go.Bar(..., row=3, col=1))       # Day-of-week
```

## Code Style

- Follow PEP 8 conventions.
- Use descriptive variable names (`monthly`, `dow_analysis`, `weekend_boost`).
- Comments for non-obvious logic (seasonality formula, data generation).
- Print actionable insights at the end of the main script.
- Keep the interactive script (`generate_interactive.py`) concise -- it mirrors the main analysis, not duplicates all comments.

## Commit Conventions

This is a single-developer demo project. Use descriptive commit messages:

```
Add 14-day rolling average to analysis
Fix axis label truncation in monthly chart
Update README with new metrics
Generate interactive Plotly HTML version
```

Prefix with type when it helps: `feat:`, `fix:`, `docs:`, `refactor:`.
