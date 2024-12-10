import pandas as pd
import numpy as np

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

def main() -> int:
    file = "python/day_1/input.csv"
    return solve(file_path = file)

if __name__ == "__main__":
    result: int = main()
    print(result)