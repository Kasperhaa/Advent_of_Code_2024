import pandas as pd
import numpy as np

def solve(file_path: str) -> int:
    result: int = 0

    df: pd.DataFrame = pd.read_csv(file_path, delimiter="", header=None, engine="python").iloc[:,1:-1]
    antennas: np.ndarray = df.to_numpy()
    antinode: np.ndarray = 1
    
    print(antennas)
    return result

def main() -> int:
    file = "python/day_8/sample.csv"
    return solve(file_path = file)

if __name__ == "__main__":
    result: int = main()
    print(result)