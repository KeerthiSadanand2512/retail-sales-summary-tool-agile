
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