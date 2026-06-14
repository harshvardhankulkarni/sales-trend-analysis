<!-- GSD -->
# Testing: Sales Trend Analysis

This is a demo/portfolio project. There are no automated test suites.

## Manual Validation Checklist

After each run, verify:

### 1. Script executes without errors

```bash
python 2_sales_trend_analysis.py
python generate_interactive.py
```

Both should exit with code 0 and print success messages.

### 2. CSV has 180 rows

The data generator produces exactly 180 data points (Jan 1 - Jun 28, 2024).

```bash
python -c "import pandas as pd; df=pd.read_csv('sales_trend_output.csv'); assert len(df) == 180, f'Expected 180 rows, got {len(df)}'; print('PASS: 180 rows')"
```

### 3. Rolling averages are computed

The CSV should contain `7_day_avg` and `30_day_avg` columns with the first 6 and first 29 values being NaN respectively (since rolling windows need full history).

```bash
python -c "
import pandas as pd
df = pd.read_csv('sales_trend_output.csv')
assert '7_day_avg' in df.columns, 'Missing 7_day_avg'
assert '30_day_avg' in df.columns, 'Missing 30_day_avg'
assert df['7_day_avg'].isna().sum() == 6, f'Expected 6 NaN in 7_day_avg, got {df[\"7_day_avg\"].isna().sum()}'
assert df['30_day_avg'].isna().sum() == 29, f'Expected 29 NaN in 30_day_avg, got {df[\"30_day_avg\"].isna().sum()}'
print('PASS: Rolling averages present and correct')
"
```

### 4. Output files exist

```bash
python -c "
import os
files = [
    '2_sales_trend_analysis.png',
    'sales_trend_output.csv',
    '2_sales_trend_interactive.html'
]
for f in files:
    assert os.path.exists(f), f'Missing: {f}'
    assert os.path.getsize(f) > 0, f'Empty file: {f}'
    print(f'PASS: {f} exists ({os.path.getsize(f)} bytes)')
"
```

### 5. Interactive HTML renders

Open `2_sales_trend_interactive.html` in a browser. Confirm:
- Three chart panels are visible (daily trend, monthly bars, day-of-week bars)
- Hover tooltips display values
- Zoom and pan work on the top chart
- The chart title reads "Sales Trend Analysis - Interactive"

### 6. Data is reproducible

Running the script twice with the same random seed produces identical output.

```bash
python 2_sales_trend_analysis.py
python -c "import hashlib; h1 = hashlib.md5(open('sales_trend_output.csv','rb').read()).hexdigest()"
# Run again
python 2_sales_trend_analysis.py
python -c "import hashlib; h2 = hashlib.md5(open('sales_trend_output.csv','rb').read()).hexdigest(); print('PASS: Reproducible' if h1 == h2 else 'FAIL: Different output')"
```

## Regression Test After Changes

Run the full validation sequence above after any code change. If CSV structure changes (new columns, different row count), update the assertions accordingly.
