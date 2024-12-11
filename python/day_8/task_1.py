import pandas as pd
import numpy as np
import time

INPUT_FILE_PATH: str = "python/day_8/input.csv"
DEBUG: bool = False

def solve(file_path: str) -> int:
    result: int = 0

    df: pd.DataFrame = pd.read_csv(file_path, delimiter="", header=None, engine="python").iloc[:,1:-1]
    antennas_array: np.ndarray = df.to_numpy()
    antinodes_array: np.ndarray = (antennas_array * 0) + '.'
    antennas_pos: dict = {}
    antinodes_pos: dict = {}
    shape: np.ndarray = np.array(df.shape) - 1 

    if DEBUG:
        for row in antennas_array:
            print(*row, sep="")

    for row_idx, line in enumerate(antennas_array):
        for col_idx, val in enumerate(line):
            if val == '.':
                continue
            antennas_pos[val] = antennas_pos.get(val, []) + [np.array((row_idx, col_idx))]
    
    for frequency_pos in antennas_pos.values():
        for idx, pos in enumerate(frequency_pos):
            for other_pos in frequency_pos[idx+1:]:
                diff = other_pos - pos
                antinode = np.array([pos-diff, other_pos+diff])
                
                for x, y in antinode:
                    if x < 0 or y < 0 or x > shape[0] or y > shape[1]:
                        if DEBUG:
                            print(f"for {tuple(pos)} and {tuple(other_pos)} :")
                            print(f"{tuple(antinode)} out of bounds!")
                            print(f"{tuple(diff)}")
                        continue
                    if DEBUG:
                        antinodes_array[x][y] = "#" # Only for visualization
                    antinodes_pos[f"{x},{y}"] = 1

    if DEBUG:
        for row in antinodes_array:
            print(*row, sep="")

    result = sum(antinodes_pos.values())
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
    print(f"{result = }")