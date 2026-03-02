import pandas as pd


def convert_dates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert 'Order Date' and 'Ship Date' columns to datetime.

    Args:
        df (pd.DataFrame): Raw dataset containing date columns.

    Returns:
        pd.DataFrame: Copy of the dataset with datetime-converted date columns.

    Raises:
        KeyError: If 'Order Date' or 'Ship Date' columns are missing.
    """
    df_clean = df.copy()
    date_cols = ["Order Date", "Ship Date"]

    for col in date_cols:
        if col in df_clean.columns:
            df_clean[col] = pd.to_datetime(df_clean[col], errors="coerce")
        else:
            raise KeyError(f"Missing expected column: '{col}'")

    return df_clean


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values using a simple, explainable strategy.

    Strategy:
    - Drop rows where critical fields are missing (Sales/Profit/Quantity)
    - Fill missing Discount with 0 (common assumption in retail data)
    - Leave non-critical text fields unchanged

    Args:
        df (pd.DataFrame): Dataset after date conversion (or raw).

    Returns:
        pd.DataFrame: Cleaned dataset with missing values handled.
    """
    df_clean = df.copy()

    critical_cols = ["Sales", "Profit", "Quantity"]
    existing_critical = [c for c in critical_cols if c in df_clean.columns]
    if existing_critical:
        df_clean = df_clean.dropna(subset=existing_critical)

    if "Discount" in df_clean.columns:
        df_clean["Discount"] = df_clean["Discount"].fillna(0)

    return df_clean


def validate_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validate and enforce numeric datatypes for key numeric columns.

    Columns enforced:
    - Sales, Profit, Quantity, Discount

    Rules:
    - Convert numeric columns using pd.to_numeric(errors='coerce')
    - If Discount column is missing, create it with default 0.0
    - Drop rows where Sales/Profit/Quantity become NaN after conversion
    - Convert Quantity to int after cleaning

    Args:
        df (pd.DataFrame): Dataset after missing value handling.

    Returns:
        pd.DataFrame: Dataset with validated numeric columns.

    Raises:
        KeyError: If Sales, Profit, or Quantity columns are missing.
        ValueError: If no valid rows remain after validation.
    """
    df_clean = df.copy()

    required_numeric = ["Sales", "Profit", "Quantity"]
    for col in required_numeric:
        if col not in df_clean.columns:
            raise KeyError(f"Missing expected numeric column: '{col}'")

    if "Discount" not in df_clean.columns:
        df_clean["Discount"] = 0.0

    for col in ["Sales", "Profit", "Quantity", "Discount"]:
        df_clean[col] = pd.to_numeric(df_clean[col], errors="coerce")

    df_clean = df_clean.dropna(subset=["Sales", "Profit", "Quantity"])

    if df_clean.empty:
        raise ValueError("No valid rows remain after numeric validation.")

    df_clean["Quantity"] = df_clean["Quantity"].astype(int)

    return df_clean