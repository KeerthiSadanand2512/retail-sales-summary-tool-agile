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