import sys
from typing import List
from collections import deque

input = sys.stdin.readline

INF = 50 * 50 * 4 

def is_rotationable(N:int, arr: List[List[str]], i: int, j: int) -> bool:
    if i < 1 or i > N -2:
        return False
    
    if j < 1 or j > N -2:
        return False
    
    for di in range(-1, 2, 1):
        for dj in range(-1, 2, 1):
            if arr[i + di][j + dj] == '1':
                return False
    
    return True
 
def solution(N: int, arr: List[List[str]]) -> int | bool:
    # [horizontal, vertical]
    visited = [[[INF, INF] for _ in range(N)] for _ in range(N)]
    queue = deque()

    # find start & end
    si = 0; sj = 0; s_is_vertical = 0
    ei = 0; ej = 0; e_is_vertical = 0
    for i in range(N):
        for j in range(N):

    # set the start
    visited[si][sj][s_is_vertical] = 0
    queue.append((si, sj, s_is_vertical))

    # bfs algorithm
    while queue:
        i, j, is_vertical = queue.popleft()
        v = visited[i][j][is_vertical]

        # answer
        if i == ei and j == ej and is_vertical == e_is_vertical:
            return v

        if is_vertical:
            # left

            # right

            # up

            # down

        else:
            # left

            # right

            # up

            # down

        # rotate
        if is_rotationable(N, arr, i, j):

    return False


if __name__ == "__main__":
    N = int(input())
    arr = [list(input().rstrip()) for _ in range(N)]

    answer = solution(N, arr)
    print(answer if answer else 0)