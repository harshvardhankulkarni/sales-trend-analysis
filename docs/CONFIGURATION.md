<!-- GSD -->
# Configuration: Sales Trend Analysis

There are no external configuration files. All parameters are set inline in the source scripts.

## Inline Parameters (Main Script)

File: `2_sales_trend_analysis.py`

### Data Generation

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `np.random.seed(42)` | int | 42 | Random seed for reproducible output. Change for different data. |
| `range(180)` | int | 180 | Number of days to generate. |
| `datetime(2024, 1, 1)` | date | 2024-01-01 | Start date of the analysis period. |
| `base_sales` | int | 50000 | Baseline daily revenue in INR. |
| `trend` | array | linspace(0, 20000, 180) | Linear trend uplift. First value = day 1 boost, last value = day 180 boost. |
| `weekly_seasonality` | array | 1 + 0.3 * sin(pi * arange / 3.5) | Sine wave multiplier. 0.3 = 30% amplitude. Period ~7 days (pi/3.5). |
| `weekend_boost` | array | [1.0, 1.0, 1.0, 1.1, 1.2, 1.5, 1.3] | Day-of-week multipliers. Index 0 = Monday, 6 = Sunday. |
| `noise` | array | normal(0, 5000, 180) | Gaussian noise. Second param (5000) = standard deviation in INR. |
| `sales` floor | int | 10000 | Minimum sales value via `np.maximum(sales, 10000)`. |

### Rolling Averages

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `window=7` | int | 7 | 7-day rolling average window. |
| `window=30` | int | 30 | 30-day rolling average window. |

### Visualization

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `figsize=(14, 12)` | tuple | (14, 12) | Figure dimensions in inches. |
| `dpi=150` | int | 150 | Output resolution for PNG. |

## Inline Parameters (Interactive Script)

File: `generate_interactive.py`

Same data generation parameters as the main script.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `height=800` | int | 800 | Plotly chart height in pixels. |
| `hovermode='x unified'` | string | 'x unified' | Hover behavior: unified x-axis tooltip. |

## Modifying Parameters

To change the analysis, edit the values directly in the script. Examples:

```python
# Longer period (365 days)
dates = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(365)]
trend = np.linspace(0, 40000, 365)

# Stronger weekend effect
weekend_boost = [1.0, 1.0, 1.0, 1.2, 1.4, 1.8, 1.6]

# Less noise (smoother data)
noise = np.random.normal(0, 2000, 180)

# Different rolling windows
df['14_day_avg'] = df['sales'].rolling(window=14).mean()
df['60_day_avg'] = df['sales'].rolling(window=60).mean()
```

## Output Options

| Output | File | Control |
|--------|------|---------|
| Static chart | `2_sales_trend_analysis.png` | `plt.savefig()` filename and DPI |
| CSV data | `sales_trend_output.csv` | `df.to_csv()` filename and index param |
| Interactive HTML | `2_sales_trend_interactive.html` | `fig.write_html()` filename in `generate_interactive.py` |
