import os
import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load the Superstore dataset from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.

    Raises:
        FileNotFoundError: If file does not exist.
        ValueError: If dataset is empty.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError("Loaded dataset is empty.")

    return df