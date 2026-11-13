"""Person 1 - Data cleaning (branch: feature/data-cleaning)"""
import pandas as pd


def load_data(path):
    """Load the raw Superstore CSV and return a DataFrame."""
    # The Kaggle Superstore file is usually latin-1 encoded
    return pd.read_csv(path, encoding="latin-1")


def standardize_columns(df):
    """Make column names lowercase with underscores: 'Sub-Category' -> 'sub_category'."""
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )
    return df


def clean_data(df):
    """Clean the DataFrame and return it."""
    df = standardize_columns(df)

    # 1. Remove duplicate rows
    before = len(df)
    df = df.drop_duplicates()
    print(f"Removed {before - len(df)} duplicate rows")

    # 2. Fix data types
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["ship_date"] = pd.to_datetime(df["ship_date"], errors="coerce")
    if "postal_code" in df.columns:
        df["postal_code"] = df["postal_code"].astype(str)

    # 3. Handle missing values
    df = df.dropna(subset=["order_date", "sales"])      # rows we cannot use
    df["discount"] = df["discount"].fillna(0)
    df["profit"] = df["profit"].fillna(0)
    df["quantity"] = df["quantity"].fillna(df["quantity"].median())

    # 4. Strip extra spaces in text columns
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

    # 5. Add new useful columns
    df["year"] = df["order_date"].dt.year
    df["month"] = df["order_date"].dt.month
    df["month_name"] = df["order_date"].dt.strftime("%b")
    df["year_month"] = df["order_date"].dt.to_period("M").astype(str)
    df["shipping_days"] = (df["ship_date"] - df["order_date"]).dt.days
    df["profit_margin"] = (df["profit"] / df["sales"] * 100).round(2)

    return df.reset_index(drop=True)


def save_clean_data(df, path):
    """Save the cleaned DataFrame to a CSV."""
    df.to_csv(path, index=False)
    print(f"Cleaned data saved to {path}")


if __name__ == "__main__":
    raw = load_data("data/raw/superstore.csv")
    cleaned = clean_data(raw)
    save_clean_data(cleaned, "data/cleaned/superstore_clean.csv")