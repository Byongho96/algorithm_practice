import sys
import heapq
from typing import List, Tuple

input = sys.stdin.readline

INF = 9 * 500 * 500
DIRECTION = ((0, 1), (1, 0), (0, -1), (-1, 0))

def slide(N: int, M: int, arr: List[List[int]], i: int, j: int, di: int, dj: int) -> Tuple[int]:
    t = 0
    while True:
        i += di
        j += dj

        if i < 0 or i > N - 1 or j < 0 or j > M - 1:
            return i - di, j - dj, INF
        
        if arr[i][j] == 'R':
            return i - di, j - dj, t
        
        if arr[i][j] == 'H':
            return i, j, INF
        
        if arr[i][j] == 'E':
            return i, j, t

        t += arr[i][j]


# Bekjoon 20926: 얼음 미로
def solution(N: int, M: int, arr: List[List[str]]) -> int:
    distance = [[INF] * M for _ in range(N)]

    # set the start
    si, sj = 0, 0
    for i in range(N):
        for j in range(M):
            if arr[i][j].isdigit():
                arr[i][j] = int(arr[i][j])
            if arr[i][j] == 'T':
                si, sj = i, j
                arr[i][j] = INF

    # Set the start
    distance[si][sj] = 0
    heap = [(0, si, sj)]

    while heap:
        dis, i, j  = heapq.heappop(heap)

        if distance[i][j] < dis:
            continue

        # visit the node
        if arr[i][j] == 'E':
            return dis
        
        if arr[i][j] == 'H':
            continue

        # traverse adjacent nodes
        for di, dj in DIRECTION:
            ni, nj, time = slide(N, M, arr, i, j, di, dj)

            if distance[ni][nj] < distance[i][j] + time + 1:
                continue

            distance[ni][nj] = distance[i][j] + time
            heapq.heappush(heap, (distance[i][j] + time, ni, nj))
    
    return -1

    
if __name__ == "__main__":
    M, N = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(N)]

    answer = solution(N, M, arr)
    print(answer)