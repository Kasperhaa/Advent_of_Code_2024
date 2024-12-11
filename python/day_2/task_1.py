import pandas as pd
import numpy as np
import time

INPUT_FILE_PATH: str = "python/day_2/input.csv"
DEBUG: bool = False

def solve(file_path: str) -> int:
    result: int = 0
    data: list[int] = []

    with open(file_path) as file:
        for line in file:
            row = list(map(int, line.strip().split(' ')))
            data.append(row)


    for row in data:
        dl = row[0] - row[1]
        if (0 > dl > 4): continue
        for e1, e2 in zip(row[1:-1], row[2:]):
            dn = e1 - e2
            if (
                (0 > dn > 4) or
                (dn < 0 < dl) or
                (dn > 0 > dl)
                ):
               break
        else: 
            result += 1

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