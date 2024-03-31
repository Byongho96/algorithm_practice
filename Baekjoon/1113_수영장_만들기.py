import sys
from typing import List

input = sys.stdin.readline

DIRECTION = ((0, 1), (1, 0), (0, -1), (-1, 0))

def bfs(N: int, M: int, arr: List[List[int]], height: int) -> int:
    total = 0
    visited = [[False] * M for _ in range(N)]

    for i in range(1, N - 1):
        for j in range(1, M - 1):

            if visited[i][j] or arr[i][j] > height -1:
                continue

            cnt = 0
            is_closed = True

            stack = [(i, j)]
            while stack:
                ci, cj = stack.pop()
        
                # it's opend
                if ci == 0 or ci == N - 1 or cj == 0 or cj == M - 1:
                    is_closed = False
                    continue

                if visited[ci][cj]:
                    continue
                
                cnt += 1
                visited[ci][cj] = True

                # traverse adjacent nodes
                for di, dj in DIRECTION:
                    ni = ci + di
                    nj = cj + dj
                    if arr[ni][nj] < height and not visited[ni][nj]:
                        stack.append((ni, nj))

            total += cnt * int(is_closed) 

    return total

def solution(N: int, M: int, arr: List[List[int]]) -> int:
    total = 0

    # check each layer
    is_filled_once = False
    for height in range(2, 10):
        layer_total = bfs(N, M, arr, height)

        if layer_total > 0 :
            is_filled_once = True    

        if layer_total == 0 and is_filled_once:
            break
        total += layer_total

    return total


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().rstrip())) for _ in range(N)]

    answer  = solution(N, M, arr)
    print(answer)