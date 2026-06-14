<!-- GSD -->
# Getting Started: Sales Trend Analysis

## Prerequisites

- Python 3.8 or higher
- pip package manager

Verify your installation:

```bash
python --version
pip --version
```

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/harshvardhankulkarni/sales-trend-analysis.git
cd sales-trend-analysis
pip install pandas numpy matplotlib
```

For the interactive version, also install Plotly:

```bash
pip install plotly
```

## First Run

Run the main analysis:

```bash
python 2_sales_trend_analysis.py
```

Expected console output:

```
Saved: 2_sales_trend_analysis.png

--- SALES TREND ANALYSIS RESULTS ---
Period: 2024-01-01 to 2024-06-28
Total days analyzed: 180
Total revenue: Rs.12,134,670
Average daily sales: Rs.67,415
Peak day: Rs.97,452 on 2024-06-26
Lowest day: Rs.19,016 on 2024-01-22

Best performing day: Wednesday (Rs.76,430)
Worst performing day: Monday (Rs.58,829)

Month over month: down 3.3% (Rs.57,360)

Action: Schedule marketing pushes on low-performing days.
Action: Investigate what drove peak days and replicate.
Done.

Exported: sales_trend_output.csv
```

## Interactive Version

Generate the interactive Plotly HTML chart:

```bash
python generate_interactive.py
```

Output: `2_sales_trend_interactive.html` - open in any browser for hover, zoom, and pan.

## Expected Outputs

After running both scripts, you should have these files:

| File | Description |
|------|-------------|
| `sales_trend_output.csv` | 180 rows, 9 columns (date, sales, day_of_week, month, is_weekend, 7_day_avg, 30_day_avg, month_num) |
| `2_sales_trend_analysis.png` | 14x12 inch, 150 DPI, 3-panel matplotlib chart |
| `2_sales_trend_interactive.html` | Self-contained Plotly HTML (open in browser, no server needed) |

## Verify It Worked

```bash
# Check CSV has 180 rows
python -c "import pandas as pd; df=pd.read_csv('sales_trend_output.csv'); print(f'Rows: {len(df)}'); print(f'Columns: {list(df.columns)}')"

# Check images exist
python -c "import os; print(f'PNG: {os.path.getsize(\"2_sales_trend_analysis.png\")} bytes'); print(f'HTML: {os.path.getsize(\"2_sales_trend_interactive.html\")} bytes')"
```
