import numpy as np

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


def main() -> int:
    file = "python/day_2/input.csv"
    return solve(file_path = file)

if __name__ == "__main__":
    result: int = main()
    print(result)