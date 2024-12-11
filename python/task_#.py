import pandas as pd
import numpy as np
import time

INPUT_FILE_PATH: str = "python/day_#/input.csv"
DEBUG: bool = False

def solve(file_path: str) -> int:
    result: int = 0

    ... # DO STUFF :)

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