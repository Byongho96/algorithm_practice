from typing import List


def rotate(arr: List[List[int]], k: int, l: int):
    if k == 1:
        pass
    elif k == 2:
        pass
    elif k == 3:
        pass
    elif k == 4:
        pass
    elif k == 5:
        pass
    elif k == 6:
        pass
    elif k == 7:
        pass
    else:
        pass


if __name__ == "__main__":
    N, R = map(int, input())

    arr = [list(map(int, input().split())) for _ in range(2**N)]

    for _ in range(R):
        k, l = map(int, input().split())
        rotate(arr, k, l)

    for row in arr:
        print(*row)
