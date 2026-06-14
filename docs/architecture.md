<!-- GSD -->

# Sales Trend Analysis — Architecture

## Context and Goals

This project analyzes 180 days of synthetic daily sales data to uncover trends, seasonal patterns, and day-of-week performance. It is a portfolio demo that demonstrates time series analysis techniques using Python.

## Data Flow

```
Synthetic Data Generation
  → Daily sales with trend + seasonality + noise
  → 7-day and 30-day rolling averages
  → Month-over-month comparison
  → Day-of-week performance breakdown
  → Static matplotlib visualization (3-panel)
  → Interactive Plotly HTML visualization
  → CSV export
```

## Components

| File | Role |
|------|------|
| `2_sales_trend_analysis.py` | Main analysis script: data generation, rolling averages, MoM, DoW, static chart, CSV export |
| `generate_interactive.py` | Generates interactive Plotly HTML version of the analysis |
| `2_sales_trend_analysis.ipynb` | Jupyter notebook version for exploratory development |
| `2_sales_trend_interactive.html` | Generated interactive Plotly chart |
| `2_sales_trend_analysis.png` | Generated static 3-panel visualization |
| `sales_trend_output.csv` | Generated output with daily sales + rolling averages |

## Design Decisions

| Decision | Rationale |
|----------|-----------|
| 180-day window | Provides enough data for meaningful trend and seasonality analysis without overwhelming complexity |
| Synthetic data | Demonstrates the analysis pipeline without requiring real sales data access |
| 7-day and 30-day rolling averages | Short window captures weekly trends; long window smooths noise for overall direction |
| Day-of-week breakdown | Reveals weekly seasonality patterns common in retail sales |
| Static + interactive charts | Static for quick reference, interactive for exploration |

## Trade-offs

- Synthetic data means patterns are known and clean — real data would include anomalies, missing values, and irregular seasonality
- Rolling averages lag behind real trends — they detect changes after they happen
- 180 days may miss longer-term seasonal cycles (quarterly or annual)
- Simple additive model for data generation oversimplifies real-world sales dynamics

## File Organization

```
sales-trend-analysis/
├── 2_sales_trend_analysis.py     # Main analysis
├── generate_interactive.py        # Interactive HTML chart generator
├── 2_sales_trend_analysis.ipynb   # Jupyter notebook
├── 2_sales_trend_analysis.png     # Static chart output
├── 2_sales_trend_interactive.html # Interactive chart output
├── sales_trend_output.csv         # Data export
├── index.html                    # GitHub Pages site
└── docs/
    ├── ARCHITECTURE.md           # This file
    ├── GETTING-STARTED.md
    ├── DEVELOPMENT.md
    ├── TESTING.md
    └── CONFIGURATION.md
```
