import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Read a csv file using a path, print the dimension and
    return a Pandas DataFrame of the csv file.
    - Return None if the csv file couldn't be read."""
    try:
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except Exception:
        return None
