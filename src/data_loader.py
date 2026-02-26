import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load the Superstore dataset from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.

    Raises:
        FileNotFoundError: If file is not found.
        ValueError: If dataset is empty.
    """

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    if df.empty:
        raise ValueError("Loaded dataset is empty.")

    return df