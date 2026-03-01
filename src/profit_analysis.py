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