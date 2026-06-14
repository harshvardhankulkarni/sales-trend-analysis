<!-- GSD -->
# Sales Trend Analysis

Time series analysis of 180 days of synthetic daily sales data. Generates reproducible data, computes rolling averages, identifies day-of-week patterns, and produces actionable revenue insights.

**Demo / Portfolio project.** Uses synthetic data to demonstrate time series analysis techniques.

## Features

- Generates 180 days of synthetic daily sales with trend, seasonality, and realistic noise
- 7-day and 30-day rolling average calculations
- Month-over-month revenue comparison with percentage change
- Day-of-week performance breakdown
- Static 3-panel visualization (PNG)
- Interactive Plotly HTML chart with hover, zoom, and pan
- CSV export for downstream use

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.8+ |
| Data processing | Pandas 2.0+, NumPy 1.24+ |
| Static viz | Matplotlib 3.7+ |
| Interactive viz | Plotly 5.x |
| Notebook | Jupyter |

## Quick Start

```bash
git clone https://github.com/harshvardhankulkarni/sales-trend-analysis.git
cd sales-trend-analysis
pip install pandas numpy matplotlib plotly
python 2_sales_trend_analysis.py
```

For the interactive version:

```bash
python generate_interactive.py
```

## Project Structure

```
sales-trend-analysis/
  2_sales_trend_analysis.py    Main analysis script
  generate_interactive.py      Plotly interactive HTML version
  2_sales_trend_analysis.ipynb Jupyter notebook
  index.html                   GitHub Pages landing page
  sales_trend_output.csv       Generated output data
  2_sales_trend_analysis.png   Static 3-panel chart
  2_sales_trend_interactive.html Interactive Plotly chart
  README.md                    This file
  docs/
    ARCHITECTURE.md            Design and methodology
    GETTING-STARTED.md         Installation and first run
    DEVELOPMENT.md             Modification guide
    TESTING.md                 Validation procedures
    CONFIGURATION.md           Parameters reference
```

## GitHub Pages

Live demo: https://harshvardhankulkarni.github.io/sales-trend-analysis/
