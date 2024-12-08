import pandas as pd
import numpy as np

def solve(file_path: str) -> int:
    df: pd.DataFrame  = pd.read_csv(file_path, header=None)
    left:  np.ndarray = df.iloc[:,0].to_numpy()
    right: np.ndarray = df.iloc[:,1].to_numpy()
    result: int = 0

    left.sort()
    right.sort()
    result = sum(np.abs(left - right))

    return result

def main() -> int:
    file = "python/day_1/input.csv"
    return solve(file_path = file)

if __name__ == "__main__":
    result: int = main()
    print(result)