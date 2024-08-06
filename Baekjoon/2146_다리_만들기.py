import sys
from collections import deque

input = sys.stdin.readline  

DIRECTION = ((-1, 0), (0, 1), (1, 0), (0, -1))

def mark_territory(N, arr, i, j, type):
    starts = []
    starts.append((i, j))
    arr[i][j] = type

    while starts:
        i, j = starts.pop()

        for di, dj in DIRECTION:
            ni, nj = i + di, j + dj
            if -1 < ni < N and -1 < nj < N and arr[ni][nj] == 1:
                starts.append((ni, nj))
                arr[ni][nj] = type


def solution(N, arr):
    # mark territory
    mark_type = 2
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                mark_territory(N, arr, i, j, mark_type)
                mark_type += 1

    # find shortest bridge
    starts = deque()
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                starts.append((i, j))

    INF = N ** 2
    cur = 0 # 하나의 턴을 모두 확인해야함
    mn = INF
    while starts:
        i, j = starts.popleft()

        if cur != visited[i][j]:
            if mn == INF:
                cur = visited[i][j]
            else:
                return mn

        for di, dj in DIRECTION:
            ni, nj = i + di, j + dj
            if -1 < ni < N and -1 < nj < N  and arr[ni][nj] != arr[i][j]:
                if not arr[ni][nj]:
                    arr[ni][nj] = arr[i][j]
                    visited[ni][nj] = visited[i][j] + 1
                    starts.append((ni, nj))
                else:
                    mn = min(mn, visited[i][j] + visited[ni][nj])

    return 0

if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = solution(N, arr)
    print(answer)