"""Person 2 - Data analysis (branch: feature/data-analysis)
Every function takes the cleaned DataFrame and returns a DataFrame/Series.
"""

import pandas as pd


def sales_by_category(df):
    """Total sales, profit and profit margin by category."""
    result = df.groupby("category").agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum"),
        orders=("order_id", "nunique"),
    )
    result["profit_margin_pct"] = (
        result["total_profit"] / result["total_sales"] * 100
    ).round(2)
    return result.round(2).sort_values("total_sales", ascending=False)


def sales_by_subcategory(df):
    """Sales and profit by sub-category."""
    return (
        df.groupby("sub_category")[["sales", "profit"]]
        .sum()
        .round(2)
        .sort_values("profit", ascending=False)
    )


def sales_by_region(df):
    """Sales and profit by region."""
    return (
        df.groupby("region")[["sales", "profit"]]
        .sum()
        .round(2)
        .sort_values("sales", ascending=False)
    )


def sales_by_segment(df):
    """Sales and profit by customer segment."""
    return (
        df.groupby("segment")[["sales", "profit"]]
        .sum()
        .round(2)
        .sort_values("sales", ascending=False)
    )


def monthly_trend(df):
    """Sales and profit for every month."""
    return df.groupby("year_month")[["sales", "profit"]].sum().round(2)


def yearly_trend(df):
    """Sales, profit and growth percentage per year."""
    result = df.groupby("year")[["sales", "profit"]].sum().round(2)
    result["sales_growth_pct"] = (
        result["sales"].pct_change() * 100
    ).round(2)
    return result


def top_customers(df, n=10):
    """Top n customers by total sales."""
    return (
        df.groupby("customer_name")[["sales", "profit"]]
        .sum()
        .round(2)
        .sort_values("sales", ascending=False)
        .head(n)
    )


def top_products(df, n=10):
    """Top n products by total sales."""
    return (
        df.groupby("product_name")[["sales", "profit"]]
        .sum()
        .round(2)
        .sort_values("sales", ascending=False)
        .head(n)
    )


def loss_making_products(df, n=10):
    """Products with the biggest total loss."""
    products = df.groupby("product_name")[["sales", "profit"]].sum().round(2)
    return products[products["profit"] < 0].sort_values("profit").head(n)


def discount_profit_summary(df):
    """Average profit at each discount level and correlation."""
    by_discount = (
        df.groupby("discount")["profit"].mean().round(2).to_frame("avg_profit")
    )
    corr = df["discount"].corr(df["profit"])
    return by_discount, round(corr, 3)


def generate_insights(df):
    """Generate plain-English business insights."""
    cat = sales_by_category(df)
    reg = sales_by_region(df)
    seg = sales_by_segment(df)
    yearly = yearly_trend(df)
    _, corr = discount_profit_summary(df)

    loss_count = (df.groupby("product_name")["profit"].sum() < 0).sum()

    return [
        f"Top category by sales: {cat.index[0]} (${cat['total_sales'].iloc[0]:,.0f}).",
        f"Highest profit margin category: {cat['profit_margin_pct'].idxmax()}.",
        f"Lowest profit margin category: {cat['profit_margin_pct'].idxmin()}.",
        f"Best region by sales: {reg.index[0]}; best by profit: {reg['profit'].idxmax()}.",
        f"Biggest customer segment: {seg.index[0]}.",
        f"Best year by sales: {int(yearly['sales'].idxmax())}.",
        f"Discount vs profit correlation: {corr}.",
        f"{loss_count} products are loss-making overall.",
    ]