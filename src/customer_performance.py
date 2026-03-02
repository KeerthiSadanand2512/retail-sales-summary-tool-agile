
import pandas as pd


#userstory5- totalsales_per customer
def total_sales_per_customer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total sales per customer.

    Args:
        df (pd.DataFrame): Cleaned Superstore DataFrame.

    Returns:
        pd.DataFrame: DataFrame with total sales per customer.

    Raises:
        KeyError: If required columns are missing.
        ValueError: If Sales column has no valid numeric values.
    """

    required_columns = ["Customer ID", "Customer Name", "Sales"]

    for col in required_columns:
        if col not in df.columns:
            raise KeyError(f"Missing required column: '{col}'")

    # Convert Sales to numeric
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

    if df["Sales"].notna().sum() == 0:
        raise ValueError("Sales column contains no valid numeric values.")

    # Group by customer
    sales_per_customer = (
        df.groupby(["Customer ID", "Customer Name"])["Sales"]
        .sum()
        .reset_index()
        .sort_values(by="Sales", ascending=False)
    )

    return sales_per_customer

def top_10_customers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Identify top 10 customers by total sales.

    Args:
        df: Cleaned Superstore DataFrame with 
        - 'Customer Name'
        - 'Sales' columns.

    Returns:
        DataFrame with columns:
            - Customer Name
            - Total Sales
        Sorted by Total Sales descending.

    Raises:
        KeyError: If required columns are missing.
        ValueError: If no valid sales values exist.
    """
    required = {"Customer Name", "Sales"}
    missing = required - set(df.columns)
    if missing:
        raise KeyError(f"Missing required column(s): {sorted(missing)}")

    sales_series = pd.to_numeric(df["Sales"], errors="coerce")
    #if sales_series.dropna().empty:
    if sales_series.isna().all():
        raise ValueError("No valid numeric Sales values found.")

    Top_10 = (
        df.assign(Sales=sales_series)
          .groupby("Customer Name", as_index=False)["Sales"]
          .sum()
          .rename(columns={"Sales": "Total Sales"})
          .sort_values(by="Total Sales", ascending=False)
          .head(10)
          .reset_index(drop=True)
    )

    return Top_10