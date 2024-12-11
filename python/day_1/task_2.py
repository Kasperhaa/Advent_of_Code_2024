import pandas as pd
import numpy as np
import time

INPUT_FILE_PATH: str = "python/day_1/input.csv"
DEBUG: bool = False

def solve(file_path: str) -> int:
    df: pd.DataFrame  = pd.read_csv(file_path, header=None, delimiter="   ", engine="python")
    left:  np.ndarray = df.iloc[:,0].to_numpy()
    right: np.ndarray = df.iloc[:,1].to_numpy()
    sim_dict: dict = {}
    result: int = 0

    for val in left:
        sim_dict[val] = sim_dict.get(val, 0) + np.count_nonzero(right == val) * val
    result = sum(sim_dict.values())
    
    return result

def calculate_time(func, *args) -> int:
    begin = time.time()
    result = func(*args)
    end = time.time()
    print(f"completed in : {end - begin:.6f} ms")

    return result

def main() -> int:
    result: int = calculate_time(solve, INPUT_FILE_PATH)
    return result

if __name__ == "__main__":
    result: int = main()
    print(result)