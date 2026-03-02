import pandas as pd


def total_sales_per_customer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total sales per customer.

    Args:
        df (pd.DataFrame): Cleaned Superstore DataFrame containing
                           'Customer ID', 'Customer Name', and 'Sales'.

    Returns:
        pd.DataFrame: DataFrame with columns:
            - Customer ID
            - Customer Name
            - Total Sales
        Sorted by Total Sales descending.

    Raises:
        KeyError: If required columns are missing.
        ValueError: If no valid numeric Sales values exist.
    """
    required_columns = {"Customer ID", "Customer Name", "Sales"}
    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        raise KeyError(f"Missing required column(s): {sorted(missing)}")

    sales_series = pd.to_numeric(df["Sales"], errors="coerce")

    if sales_series.dropna().empty:
        raise ValueError("No valid numeric Sales values found.")

    summary = (
        df.assign(Sales=sales_series)
          .groupby(["Customer ID", "Customer Name"], as_index=False)["Sales"]
          .sum()
          .rename(columns={"Sales": "Total Sales"})
          .sort_values(by="Total Sales", ascending=False)
          .reset_index(drop=True)
    )

    return summary


def top_10_customers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Identify the top 10 customers by total sales.

    Args:
        df (pd.DataFrame): Cleaned Superstore DataFrame containing
                           'Customer ID', 'Customer Name', and 'Sales'.

    Returns:
        pd.DataFrame: DataFrame with columns:
            - Customer ID
            - Customer Name
            - Total Sales
        Sorted by Total Sales descending (Top 10 only).

    Raises:
        KeyError: If required columns are missing.
        ValueError: If no valid numeric Sales values exist.
    """
    full_summary = total_sales_per_customer(df)

    if full_summary.empty:
        raise ValueError("Customer sales summary is empty.")

    return full_summary.head(10)
