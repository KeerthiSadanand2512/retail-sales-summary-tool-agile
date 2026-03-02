import pandas as pd


def total_sales(df: pd.DataFrame) -> float:
    """
    Calculate total sales from the Superstore dataset.

    Args:
        df (pd.DataFrame): Cleaned Superstore DataFrame containing a 'Sales' column.

    Returns:
        float: Total sales value.

    Raises:
        KeyError: If 'Sales' column is missing.
        ValueError: If 'Sales' contains no valid numeric values.
    """
    if "Sales" not in df.columns:
        raise KeyError("Missing required column: 'Sales'")

    sales_series = pd.to_numeric(df["Sales"], errors="coerce")
    if sales_series.dropna().empty:
        raise ValueError("No valid numeric Sales values found.")

    total = float(sales_series.sum(skipna=True))
    return total


def sales_by_region(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total sales grouped by region.

    Args:
        df (pd.DataFrame): Cleaned Superstore DataFrame with 'Region' and 'Sales' columns.

    Returns:
        pd.DataFrame: DataFrame with columns:
            - Region
            - Total Sales
        Sorted by Total Sales descending.

    Raises:
        KeyError: If required columns are missing.
        ValueError: If 'Sales' contains no valid numeric values.
    """
    required_columns = {"Region", "Sales"}
    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        raise KeyError(f"Missing required column(s): {sorted(missing)}")

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
    Calculate total sales grouped by category.

    Notes:
        This function does not mutate the input DataFrame. It makes a copy before
        applying Category cleaning.

    Args:
        df (pd.DataFrame): Cleaned Superstore DataFrame with 'Category' and 'Sales' columns.

    Returns:
        pd.DataFrame: DataFrame with columns:
            - Category
            - Total Sales
        Sorted by Total Sales descending.

    Raises:
        KeyError: If required columns are missing.
        ValueError: If 'Sales' contains no valid numeric values.
    """
    required_columns = {"Category", "Sales"}
    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        raise KeyError(f"Missing required column(s): {sorted(missing)}")

    df_clean = df.copy()

    # Clean Category column (strip, normalize whitespace)
    df_clean["Category"] = (
        df_clean["Category"]
        .astype(str)
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )

    sales_series = pd.to_numeric(df_clean["Sales"], errors="coerce")
    if sales_series.dropna().empty:
        raise ValueError("No valid numeric Sales values found.")

    category_sales = (
        df_clean.assign(Sales=sales_series)
          .groupby("Category", as_index=False)["Sales"]
          .sum()
          .rename(columns={"Sales": "Total Sales"})
          .sort_values(by="Total Sales", ascending=False)
          .reset_index(drop=True)
    )

    return category_sales

# Return type annotation added to enforce clear function contract
# and strengthen separation of logic from presentation

def sales_summary_report(df: pd.DataFrame) -> dict[str, object]:
    """
    Generate a structured sales summary report.

    Args:
        df (pd.DataFrame): Cleaned Superstore DataFrame.

    Returns:
        dict: Dictionary containing:
            - total_sales (float)
            - sales_by_region (pd.DataFrame)
            - sales_by_category (pd.DataFrame)
    """
    return {
        "total_sales": total_sales(df),
        "sales_by_region": sales_by_region(df),
        "sales_by_category": sales_by_category(df),
    }