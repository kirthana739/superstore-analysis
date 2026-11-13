"""Person 3 - Visualization (branch: feature/visualization)
Every function takes the cleaned DataFrame and saves a chart as PNG.
"""
import os
import matplotlib
matplotlib.use("Agg")  # saves charts without opening a window
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
CHART_DIR = "outputs/charts"


def _save(filename):
    os.makedirs(CHART_DIR, exist_ok=True)
    path = os.path.join(CHART_DIR, filename)
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"Saved chart: {path}")


def plot_category_sales(df):
    """Bar chart: sales and profit by category."""
    data = df.groupby("category")[["sales", "profit"]].sum().reset_index()
    data = data.melt(id_vars="category", var_name="metric", value_name="amount")
    plt.figure(figsize=(8, 5))
    sns.barplot(data=data, x="category", y="amount", hue="metric")
    plt.title("Sales and Profit by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount ($)")
    _save("category_sales_profit.png")


def plot_monthly_trend(df):
    """Line chart: monthly sales."""
    data = df.groupby("year_month")["sales"].sum()
    plt.figure(figsize=(12, 5))
    plt.plot(data.index, data.values, marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=90)
    _save("monthly_sales_trend.png")


def plot_correlation_heatmap(df):
    """Heatmap: correlation between numeric columns."""
    cols = ["sales", "quantity", "discount", "profit", "profit_margin", "shipping_days"]
    cols = [c for c in cols if c in df.columns]
    plt.figure(figsize=(7, 6))
    sns.heatmap(df[cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    _save("correlation_heatmap.png")


def plot_segment_pie(df):
    """Pie chart: sales share by customer segment."""
    data = df.groupby("segment")["sales"].sum()
    plt.figure(figsize=(6, 6))
    plt.pie(data.values, labels=data.index, autopct="%1.1f%%", startangle=90)
    plt.title("Sales Share by Segment")
    _save("segment_sales_pie.png")


def plot_region_profit(df):
    """Bar chart: profit by region."""
    data = df.groupby("region")["profit"].sum().sort_values(ascending=False).reset_index()
    plt.figure(figsize=(8, 5))
    sns.barplot(data=data, x="region", y="profit", color="steelblue")
    plt.title("Profit by Region")
    plt.xlabel("Region")
    plt.ylabel("Profit ($)")
    _save("region_profit.png")


def plot_discount_vs_profit(df):
    """Scatter plot: discount vs profit."""
    plt.figure(figsize=(7, 5))
    sns.scatterplot(data=df, x="discount", y="profit", alpha=0.4)
    plt.title("Discount vs Profit")
    plt.xlabel("Discount")
    plt.ylabel("Profit ($)")
    _save("discount_vs_profit.png")