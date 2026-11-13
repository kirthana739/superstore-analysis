"""Runs the whole pipeline: clean -> analyse -> visualise."""
import os
from src import cleaning, analysis, visualization

RAW_PATH = "data/raw/superstore.csv"
CLEAN_PATH = "data/cleaned/superstore_clean.csv"
TABLE_DIR = "outputs/tables"


def main():
    # Step 1: cleaning (Person 1)
    raw = cleaning.load_data(RAW_PATH)
    df = cleaning.clean_data(raw)
    cleaning.save_clean_data(df, CLEAN_PATH)

    # Step 2: analysis (Person 2)
    os.makedirs(TABLE_DIR, exist_ok=True)
    tables = {
        "sales_by_category": analysis.sales_by_category(df),
        "sales_by_region": analysis.sales_by_region(df),
        "sales_by_segment": analysis.sales_by_segment(df),
        "yearly_trend": analysis.yearly_trend(df),
        "top_customers": analysis.top_customers(df),
        "top_products": analysis.top_products(df),
        "loss_making_products": analysis.loss_making_products(df),
    }
    for name, table in tables.items():
        print(f"\n--- {name} ---")
        print(table)
        table.to_csv(os.path.join(TABLE_DIR, f"{name}.csv"))

    print("\n=== KEY INSIGHTS ===")
    for line in analysis.generate_insights(df):
        print("-", line)

    # Step 3: visualization (Person 3)
    visualization.plot_category_sales(df)
    visualization.plot_monthly_trend(df)
    visualization.plot_correlation_heatmap(df)
    visualization.plot_segment_pie(df)
    visualization.plot_region_profit(df)
    visualization.plot_discount_vs_profit(df)

    print("\nDone! Check the outputs/ folder.")


if __name__ == "__main__":
    main()