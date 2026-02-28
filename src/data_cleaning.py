import pandas as pd


def convert_dates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert Order Date and Ship Date columns to datetime.

    Returns a NEW DataFrame (does not mutate the original).
    """
    df_clean = df.copy()

    # Superstore commonly has these exact column names
    date_cols = ["Order Date", "Ship Date"]

    for col in date_cols:
        if col in df_clean.columns:
            df_clean[col] = pd.to_datetime(df_clean[col], errors="coerce")
        else:
            raise KeyError(f"Missing expected column: '{col}'")

    return df_clean


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values with a simple, explainable strategy:
    - Drop rows where critical fields are missing (Sales/Profit/Quantity)
    - Fill missing Discount with 0 (common assumption in retail data)
    - Leave non-critical text fields as-is (or fill with 'Unknown' if needed)

    Returns a NEW DataFrame.
    """
    df_clean = df.copy()

    # Drop rows missing critical numeric fields (cannot analyze these reliably)
    critical_cols = ["Sales", "Profit", "Quantity"]
    existing_critical = [c for c in critical_cols if c in df_clean.columns]
    if existing_critical:
        df_clean = df_clean.dropna(subset=existing_critical)

    # Fill discount missing with 0 (assumption: no discount recorded => 0)
    if "Discount" in df_clean.columns:
        df_clean["Discount"] = df_clean["Discount"].fillna(0)
        return df_clean

def validate_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    df_clean = df.copy()

    for col in ["Sales", "Profit", "Quantity", "Discount"]:
        if col in df_clean.columns:
            df_clean[col] = pd.to_numeric(df_clean[col], errors="coerce")
        else:
            if col == "Discount":
                df_clean["Discount"] = 0.0
            else:
                raise KeyError(f"Missing expected numeric column: '{col}'")

    df_clean = df_clean.dropna(subset=["Sales", "Profit", "Quantity", "Discount"])

    df_clean["Quantity"] = df_clean["Quantity"].astype(int)

    return df_clean

