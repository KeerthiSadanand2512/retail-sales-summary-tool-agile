import pandas as pd


def total_profit(df: pd.DataFrame) -> float:
    """
    Calculate total profit from the dataset.

    Returns:
        Total profit as a float.
    """
    if "Profit" not in df.columns:
        raise KeyError("Missing required column: 'Profit'")

    profit_series = pd.to_numeric(df["Profit"], errors="coerce")
    total = float(profit_series.sum(skipna=True))

    if pd.isna(total):
        raise ValueError("Total profit could not be calculated (no valid Profit values).")

    return total


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

def profit_by_sub_category(df: pd.DataFrame) -> pd.DataFrame:
    required_columns = {"Sub-Category", "Profit"}
    missing = required_columns - set(df.columns)
    if missing:
        raise KeyError(f"Missing required column(s): {sorted(missing)}")

    profit_series = pd.to_numeric(df["Profit"], errors="coerce")
    if profit_series.dropna().empty:
        raise ValueError("Profit could not be calculated (no valid Profit values).")

    summary = (
        df.assign(Profit=profit_series)
          .groupby("Sub-Category", as_index=False)["Profit"]
          .sum()
          .rename(columns={"Profit": "Total Profit"})
          .sort_values(by="Total Profit", ascending=False)
          .reset_index(drop=True)
    )

    return summary


def profit_report(df: pd.DataFrame) -> dict:
    return {
        "total_profit": total_profit(df),
        "profit_by_category": profit_by_category(df),
        "profit_by_sub_category": profit_by_sub_category(df),
    }