import pandas as pd


def total_sales(df: pd.DataFrame) -> float:
    """
    Calculate total sales from the Superstore dataset.

    Args:
        df: Cleaned Superstore DataFrame with a 'Sales' column.

    Returns:
        Total sales as a float.

    Raises:
        KeyError: If 'Sales' column is missing.
        ValueError: If Sales contains no valid numeric values.
    """
    if "Sales" not in df.columns:
        raise KeyError("Missing required column: 'Sales'")

    sales_series = pd.to_numeric(df["Sales"], errors="coerce")
    total = float(sales_series.sum(skipna=True))

    if pd.isna(total):
        raise ValueError("Total sales could not be calculated (no valid Sales values).")

    return total


def sales_by_region(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total sales grouped by region from the Superstore dataset.

    Args:
        df: Cleaned Superstore DataFrame with 'Region' and 'Sales' columns.

    Returns:
        DataFrame with total sales per region sorted in descending order.

    Raises:
        KeyError: If required columns are missing.
        ValueError: If no valid numeric sales values are found.
    """
    required_columns = {"Region", "Sales"}

    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        raise KeyError(f"Missing required column(s): {missing}")

    sales_series = pd.to_numeric(df["Sales"], errors="coerce")

    if sales_series.dropna().empty:
        raise ValueError("No valid numeric Sales values found.")

    region_sales = (
    df.assign(Sales=sales_series)
      .groupby("Region", as_index=False)["Sales"]
      .sum()
      .rename(columns={"Sales": "Total Sales"})
      .sort_values(by="Total Sales", ascending=False)
      .reset_index(drop=True)
)

    return region_sales

def sales_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total sales grouped by category from the Superstore dataset.

    Args:
        df: Cleaned Superstore DataFrame with 'Category' and 'Sales' columns.

    Returns:
        DataFrame with total sales per category sorted in descending order.

    Raises:
        KeyError: If required columns are missing.
        ValueError: If no valid numeric sales values are found.
    """
    required_columns = {"Category", "Sales"}

    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        raise KeyError(f"Missing required column(s): {missing}")

    sales_series = pd.to_numeric(df["Sales"], errors="coerce")

    if sales_series.dropna().empty:
        raise ValueError("No valid numeric Sales values found.")

    category_sales = (
    df.assign(Sales=sales_series)
      .groupby("Category", as_index=False)["Sales"]
      .sum()
      .rename(columns={"Sales": "Total Sales"})
      .sort_values(by="Total Sales", ascending=False)
      .reset_index(drop=True)
)

    return category_sales

def sales_summary_report(df: pd.DataFrame) -> dict:
    """
    Return a structured sales report as reusable objects.
    No printing—only returns results.
    """
    return {
        "total_sales": total_sales(df),
        "sales_by_region": sales_by_region(df),
        "sales_by_category": sales_by_category(df),
    }
