import sys
from collections import defaultdict

input = sys.stdin.readline

DIRECTION = ((0, 1), (0, -1), (1, 0), (-1, 0))

def melt_iceberg(ice_bergs, arr):
    visited = [[False] * M for _ in range(N)]
    melted_ice = defaultdict(int)

    stack = [(ice_bergs[0][0], ice_bergs[0][1])]
    visited[ice_bergs[0][0]][ice_bergs[0][1]] = True
    cnt = 1

    while stack:
        i, j = stack.pop()

        for di, dj in DIRECTION:
            ni, nj = i + di, j + dj

            if arr[ni][nj] == 0:
                melted_ice[(i, j)] += 1
                continue

            elif not visited[ni][nj]:
                cnt += 1
                visited[ni][nj] = True
                stack.append((ni, nj))

    if cnt != len(ice_bergs):
        return False

    for (i, j), melt in melted_ice.items():
        if arr[i][j] > melt:
            arr[i][j] -= melt
        else:
            arr[i][j] = 0
            ice_bergs.remove((i, j))

    return True

def solution(N, M, arr):
    # collect ice_bergs
    ice_bergs = []
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                ice_bergs.append((i, j))

    # melt
    step = 0
    while len(ice_bergs):
        step += 1
        
        # melt ice_bergs
        was_connected = melt_iceberg(ice_bergs, arr)

        if not was_connected:
            return step - 1
        

    return 0




if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = solution(N, M, arr)
    print(answer)