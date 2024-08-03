import sys
import heapq

input = sys.stdin.readline

DIRECTION = ((1, 0), (0, -1), (-1, 0), (0, 1)) # clockwise

def solution(N, arr):
    # find source and target
    si, sj, ti, tj = 0, 0, 0, 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] == "#":
                if si == 0:
                    si, sj = i, j
                else:
                    ti, tj = i, j
                    break
        if ti != 0:
            break

    # heap
    heap = []
    visited = [[[0] *(N + 2) for _ in range(N + 2)] for _ in range(4)]

    # find start direction
    for idx, (di, dj) in enumerate(DIRECTION):
        ni, nj = si + di, sj + dj
        if arr[ni][nj] != "*":
            heapq.heappush(heap, (0, ni, nj, idx)) # cost, i, j, direction

    while heap:
        cost, i, j, direction = heapq.heappop(heap)
        
        if visited[direction][i][j] and cost > visited[direction][i][j] - 1:
            continue

        visited[direction][i][j] = cost
        
        if i == ti and j == tj: # target
            return cost
        
        if arr[i][j] == '*':
            continue

        elif arr[i][j] == ".":
            di, dj = DIRECTION[direction]
            while arr[i][j] == ".":
                i += di
                j += dj
            heapq.heappush(heap, (cost, i, j, direction))

        elif arr[i][j] == "!":
            di, dj = DIRECTION[direction]
            heapq.heappush(heap, (cost, i + di, j + dj, direction))

            # clockwise 90 degree
            di, dj = DIRECTION[(direction + 1) % 4]
            heapq.heappush(heap, (cost + 1, i + di, j + dj, (direction + 1) % 4))

            # counter clockwise 90 degree
            di, dj = DIRECTION[(direction - 1) % 4]
            heapq.heappush(heap, (cost + 1, i + di, j + dj, (direction - 1) % 4))
    
    return -1


if __name__ == "__main__":
    N = int(input())
    arr = [['*'] * (N + 2)] + [['*'] + list(input()) + ['*'] for _ in range(N)] + [['*'] * (N + 2)]
    answer = solution(N, arr)

    print(answer)