from pathlib import Path
import pandas as pd

here = Path(__file__).parent
csv_in = here / "dat.csv"
csv_out = here / "sales_cleaned.csv"

if not csv_in.exists() or csv_in.stat().st_size == 0:
    raise FileNotFoundError(f"CSV missing or empty: {csv_in}")

try:
    df = pd.read_csv(csv_in) 
except pd.errors.EmptyDataError:
    raise ValueError("CSV is empty. Add a header row like: order_id,customer,amount,notes")
except pd.errors.ParserError as e:
    raise ValueError(f"CSV parse error: {e}\nTip: ensure commas separate columns and the first line is headers.")


df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
df["customer"] = df["customer"].astype(str).str.strip()
df = df.dropna(subset=["customer", "amount"])

df.to_csv(csv_out, index=False)
print(f"Rows written: {len(df)}")
print(f"Cleaned file -> {csv_out}")
