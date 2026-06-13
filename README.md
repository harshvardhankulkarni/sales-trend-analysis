# Sales Trend Analysis - Demo Project

Analyze 180 days of daily sales data. Identify trends, seasonal patterns, and day-of-week performance.

This is a demo project using synthetic data to demonstrate time series analysis techniques.

## Tech Stack

- Python 3.8+
- Pandas 2.0+ - Data manipulation and rolling calculations
- NumPy 1.24+ - Numerical operations
- Matplotlib 3.7+ - Visualization

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

```bash
git clone https://github.com/harshvardhankulkarni/sales-trend-analysis.git
cd sales-trend-analysis
pip install pandas numpy matplotlib
```

### Running

```bash
python 2_sales_trend_analysis.py
```

Expected output:

```
Saved: 2_sales_trend_analysis.png
--- SALES TREND ANALYSIS RESULTS ---
Period: 2024-01-01 to 2024-06-28
Total revenue: Rs.12,134,670
Average daily sales: Rs.67,415
...
Exported: sales_trend_output.csv
Done.
```

### Output Files

| File | Description |
|------|-------------|
| 2_sales_trend_analysis.png | 3-panel visualization chart |
| sales_trend_output.csv | Daily sales data with 7-day and 30-day averages |

## How It Works

The script generates 180 days of synthetic daily sales with four components:

1. **Base trend** - Revenue grows linearly over time (Rs.0 to Rs.20,000 uplift).
2. **Weekly seasonality** - Cyclical pattern repeating every 7 days.
3. **Day-of-week effect** - Weekend days get 1.3x to 1.5x boost.
4. **Random noise** - Realistic day-to-day variation.

Two rolling averages smooth the noise:

- **7-day average** - Captures weekly cycles.
- **30-day average** - Shows the underlying trend.

### Metrics Calculated

- Total revenue over the period.
- Average daily revenue.
- Peak and lowest sales days.
- Best and worst performing days of the week.
- Month-over-month change percentage.

## Project Structure

```
sales-trend-analysis/
  2_sales_trend_analysis.py   Main analysis script
  README.md                   This file
  docs/
    architecture.md            Design and methodology
    runbook.md                 Operations guide
```

## Configuration

Edit these parameters at the top of the script:

- `np.random.seed(42)` - Change for different data.
- `base_sales = 50000` - Baseline daily revenue.
- `trend` range - Controls growth rate.
- `weekend_boost` array - Adjust day-of-week multipliers.

## License

MIT
