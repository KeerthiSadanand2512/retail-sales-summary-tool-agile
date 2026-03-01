import pandas as pd


def total_profit(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total profit from the dataset.

    Returns:
        A structured DataFrame with:
        - Metric
        - Value
    """

    if "Profit" not in df.columns:
        raise KeyError("Missing required column: 'Profit'")

    # Ensure Profit is numeric
    profit_series = pd.to_numeric(df["Profit"], errors="coerce")

    total = profit_series.sum()

    result = pd.DataFrame({
        "Metric": ["Total Profit"],
        "Value": [total]
    })

    return result


def profit_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total profit grouped by Category.

    Args:
        df: Cleaned Superstore DataFrame with 'Category' and 'Profit' columns.

    Returns:
        DataFrame with columns: Category, Total Profit (sorted desc).

    Raises:
        KeyError: If required columns are missing.
        ValueError: If Profit contains no valid numeric values.
    """
    required_columns = {"Category", "Profit"}
    missing = required_columns - set(df.columns)
    if missing:
        raise KeyError(f"Missing required column(s): {sorted(missing)}")

    profit_series = pd.to_numeric(df["Profit"], errors="coerce")
    if profit_series.dropna().empty:
        raise ValueError("No valid numeric Profit values found.")

    summary = (
        df.assign(Profit=profit_series)
          .groupby("Category", as_index=False)["Profit"]
          .sum()
          .rename(columns={"Profit": "Total Profit"})
          .sort_values(by="Total Profit", ascending=False)
          .reset_index(drop=True)
    )

    return summary