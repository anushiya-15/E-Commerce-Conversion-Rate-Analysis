
import csv
from pathlib import Path
from collections import Counter

BASE_DIR = Path(__file__).resolve().parent

files = {
    "FUNNEL EVENTS": BASE_DIR / "conversion-funnel-steps-practice-dataset-v1-csv-funnel_events.csv",
    "SHOP SESSIONS": BASE_DIR / "conversion-funnel-steps-practice-dataset-v1-csv-shop_sessions.csv"
}

for name, file_path in files.items():

    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    if not file_path.exists():
        print("File not found:", file_path.name)
        continue

    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames
        rows = list(reader)

    print("\nTotal Rows:", len(rows))
    print("Total Columns:", len(columns))

    print("\nColumn Names:")
    for column in columns:
        print("-", column)

    print("\nMissing Values:")
    for column in columns:
        missing = sum(
            1 for row in rows
            if row.get(column) is None or row[column].strip() == ""
        )
        print(f"{column}: {missing}")

    print("\nDuplicate Rows:", len(rows) - len({
        tuple(row.get(col, "") for col in columns)
        for row in rows
    }))

    print("\nFirst 5 Rows:")
    for row in rows[:5]:
        print(row)

print("\nDATASET INSPECTION COMPLETED!")

import csv
from pathlib import Path
from collections import Counter, defaultdict

BASE_DIR = Path(__file__).resolve().parent

file_path = BASE_DIR / "conversion-funnel-steps-practice-dataset-v1-csv-funnel_events.csv"

with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
    rows = list(csv.DictReader(file))

step_counts = Counter(row["step"] for row in rows)
cart_values = defaultdict(int)

for row in rows:
    if row["cart_value"].strip():
        cart_values[row["step"]] += 1

print("\n========== FUNNEL STAGE ANALYSIS ==========")

for step, count in step_counts.items():
    print(f"{step}: {count} events")

print("\n========== CART VALUE BY STAGE ==========")

for step, count in step_counts.items():
    print(f"{step}: {cart_values[step]} populated cart values")

print("\n========== SESSION ID CHECK ==========")

session_ids = {row["session_id"] for row in rows}

print("Unique session IDs in funnel:", len(session_ids))
print("First 10 session IDs:", sorted(session_ids, key=int)[:10])



import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

funnel_file = BASE_DIR / "conversion-funnel-steps-practice-dataset-v1-csv-funnel_events.csv"
shop_file = BASE_DIR / "conversion-funnel-steps-practice-dataset-v1-csv-shop_sessions.csv"

with open(funnel_file, encoding="utf-8-sig", newline="") as f:
    funnel = list(csv.DictReader(f))

with open(shop_file, encoding="utf-8-sig", newline="") as f:
    shop = list(csv.DictReader(f))

funnel_ids = {row["session_id"] for row in funnel}
shop_ids = {row["id"] for row in shop}

print("\n========== SESSION CONNECTION CHECK ==========")
print("Funnel unique sessions:", len(funnel_ids))
print("Shop session IDs:", len(shop_ids))
print("Matching IDs:", len(funnel_ids & shop_ids))
print("Unmatched funnel IDs:", len(funnel_ids - shop_ids))
print("Unmatched shop IDs:", len(shop_ids - funnel_ids))



import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "cleaned_data"
OUTPUT_DIR.mkdir(exist_ok=True)

files = {
    "funnel_events": BASE_DIR / "conversion-funnel-steps-practice-dataset-v1-csv-funnel_events.csv",
    "shop_sessions": BASE_DIR / "conversion-funnel-steps-practice-dataset-v1-csv-shop_sessions.csv"
}

for name, file_path in files.items():

    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames
        rows = list(reader)

    cleaned_rows = []
    seen = set()

    for row in rows:
        cleaned_row = {
            key: value.strip() if value else ""
            for key, value in row.items()
        }

        row_key = tuple(cleaned_row[col] for col in columns)

        if row_key not in seen:
            seen.add(row_key)
            cleaned_rows.append(cleaned_row)

    output_file = OUTPUT_DIR / f"{name}_cleaned.csv"

    with open(output_file, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(cleaned_rows)

    print(f"\n{name}")
    print("Original rows:", len(rows))
    print("Cleaned rows:", len(cleaned_rows))
    print("Duplicates removed:", len(rows) - len(cleaned_rows))
    print("Saved to:", output_file)

print("\nDATA CLEANING COMPLETED!")
