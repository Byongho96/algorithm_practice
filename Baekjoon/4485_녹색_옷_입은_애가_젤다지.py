import heapq
import sys
from typing import List

input = sys.stdin.readline


DIRECTION = ((1, 0), (0, 1), (-1, 0), (0, -1))


def find_min_cost(N: int, arr: List[List[int]]):
    visited = [[False] * N for _ in range(N)]
    heap = [(arr[0][0], 0, 0)]

    while heap:
        cost, i, j = heapq.heappop(heap)

        if i == N - 1 and j == N - 1:
            return cost

        for di, dj in DIRECTION:
            ni = i + di
            nj = j + dj
            if -1 < ni < N and -1 < nj < N and not visited[ni][nj]:
                visited[ni][nj] = True
                heapq.heappush(heap, (cost + arr[ni][nj], ni, nj))


if __name__ == "__main__":
    t = 0
    while True:
        t += 1
        N = int(input())

        if not N:
            break

        arr = [list(map(int, input().split())) for _ in range(N)]

        print(f"Problem {t}:", find_min_cost(N, arr))
