import pandas as pd
import numpy as np
import time

INPUT_FILE_PATH: str = "python/day_1/input.csv"
DEBUG: bool = False

def solve(file_path: str) -> int:
    df: pd.DataFrame  = pd.read_csv(file_path, header=None, delimiter="   ", engine="python")
    left:  np.ndarray = df.iloc[:,0].to_numpy()
    right: np.ndarray = df.iloc[:,1].to_numpy()
    result: int = 0

    left.sort()
    right.sort()
    result = sum(np.abs(left - right))

    return result

def calculate_time(func, *args):
    begin = time.time()
    result = func(*args)
    end = time.time()
    print(f"completed in : {end - begin:.6f} ms")

    return result

def main() -> int:
    result: int = solve(file_path = INPUT_FILE_PATH)
    return result

if __name__ == "__main__":
    result: int = main()
    print(result)