import pandas as pd


def total_profit(df: pd.DataFrame) -> float:
    """
    Calculate total profit from the dataset.

    Args:
        df (pd.DataFrame): Cleaned Superstore DataFrame containing 'Profit'.

    Returns:
        float: Total profit value.

    Raises:
        KeyError: If 'Profit' column is missing.
        ValueError: If no valid numeric Profit values exist.
    """
    if "Profit" not in df.columns:
        raise KeyError("Missing required column: 'Profit'")

    profit_series = pd.to_numeric(df["Profit"], errors="coerce")
    if profit_series.dropna().empty:
        raise ValueError("No valid numeric Profit values found.")

    return float(profit_series.sum(skipna=True))


def profit_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total profit grouped by category.

    Notes:
        Cleans Category values (strip + normalize whitespace) to prevent
        duplicate-looking categories caused by hidden/trailing spaces.

    Args:
        df (pd.DataFrame): Cleaned Superstore DataFrame with 'Category' and 'Profit' columns.

    Returns:
        pd.DataFrame: DataFrame with columns:
            - Category
            - Total Profit
        Sorted by Total Profit descending.

    Raises:
        KeyError: If required columns are missing.
        ValueError: If no valid numeric Profit values exist.
    """
    required_columns = {"Category", "Profit"}
    missing = required_columns - set(df.columns)
    if missing:
        raise KeyError(f"Missing required column(s): {sorted(missing)}")

    df_clean = df.copy()

    # Clean Category text to avoid duplicates like "Technology" vs "Technology "
    df_clean["Category"] = (
        df_clean["Category"]
        .astype(str)
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )

    profit_series = pd.to_numeric(df_clean["Profit"], errors="coerce")
    if profit_series.dropna().empty:
        raise ValueError("No valid numeric Profit values found.")

    summary = (
        df_clean.assign(Profit=profit_series)
        .groupby("Category", as_index=False)["Profit"]
        .sum()
        .rename(columns={"Profit": "Total Profit"})
        .sort_values(by="Total Profit", ascending=False)
        .reset_index(drop=True)
    )

    return summary


def profit_by_sub_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total profit grouped by sub-category.

    Notes:
        Cleans Sub-Category values (strip + normalize whitespace) to prevent
        duplicate-looking sub-categories caused by hidden/trailing spaces.

    Args:
        df (pd.DataFrame): Cleaned Superstore DataFrame with 'Sub-Category' and 'Profit' columns.

    Returns:
        pd.DataFrame: DataFrame with columns:
            - Sub-Category
            - Total Profit
        Sorted by Total Profit descending.

    Raises:
        KeyError: If required columns are missing.
        ValueError: If no valid numeric Profit values exist.
    """
    required_columns = {"Sub-Category", "Profit"}
    missing = required_columns - set(df.columns)
    if missing:
        raise KeyError(f"Missing required column(s): {sorted(missing)}")

    df_clean = df.copy()

    # Clean Sub-Category text (same reason as Category)
    df_clean["Sub-Category"] = (
        df_clean["Sub-Category"]
        .astype(str)
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )

    profit_series = pd.to_numeric(df_clean["Profit"], errors="coerce")
    if profit_series.dropna().empty:
        raise ValueError("No valid numeric Profit values found.")

    summary = (
        df_clean.assign(Profit=profit_series)
        .groupby("Sub-Category", as_index=False)["Profit"]
        .sum()
        .rename(columns={"Profit": "Total Profit"})
        .sort_values(by="Total Profit", ascending=False)
        .reset_index(drop=True)
    )

    return summary


def profit_report(df: pd.DataFrame) -> dict:
    """
    Generate structured profit analysis report.

    Args:
        df (pd.DataFrame): Cleaned Superstore DataFrame.

    Returns:
        dict: Dictionary containing:
            - total_profit (float)
            - profit_by_category (pd.DataFrame)
            - profit_by_sub_category (pd.DataFrame)
    """
    return {
        "total_profit": total_profit(df),
        "profit_by_category": profit_by_category(df),
        "profit_by_sub_category": profit_by_sub_category(df),
    }