# ETL Pipeline – Used Car Prices

A Python ETL pipeline that extracts used car data from multiple file formats (CSV, JSON, XML), transforms it, and loads it into a single clean CSV file, logging each stage of the process.

## What it does

- **Extract:** reads all `.csv`, `.json` (JSON Lines) and `.xml` files in the folder and combines them into one dataset.
- **Transform:** rounds the `price` column to 2 decimal places.
- **Load:** saves the result to `transformed_data.csv`.
- **Log:** records a timestamp for the start and end of each phase in `log_file.txt`.

## Tech stack

- Python 3.11
- pandas
- xml.etree.ElementTree, glob, datetime (standard library)

## How to run

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows (Git Bash)
pip install -r requirements.txt
python etl_practice.py
```

## Output

90 records from 9 source files, with columns: `car_model`, `year_of_manufacture`, `price`, `fuel`.

## What I learned

- Parsing XML with ElementTree and reading JSON Lines with pandas.
- Why building a list and concatenating once is more efficient than calling `pd.concat` in a loop.
- Keeping each ETL function focused on a single responsibility.

## Context

Built as part of the IBM *Python Project for Data Engineering* course.