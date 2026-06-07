# jamn_sales_tracker
Collects sales data from multiple sources and plugs into a spreadsheet for book-keeping. For my band, JAMN.

Usage:

```
python jamn_sales_tracker.py [-h] [-d DAYS] [-g GOOGLE_SHEETS]
```

```
options:
  -h, --help            show this help message and exit
  -d, --days DAYS       Last X days you want transactions from. Will get 365 if empty.
  -gs, --gs_log GS_LOG  Log to Google Sheets. False by default.
```
