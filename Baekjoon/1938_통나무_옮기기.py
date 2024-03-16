import sys
from typing import List
from collections import deque

input = sys.stdin.readline

INF = 50 * 50 * 4 

def is_rotationable(N:int, arr: List[List[str]], i: int, j: int) -> bool:
    if i < 1 or i > N - 2:
        return False
    
    if j < 1 or j > N - 2:
        return False
    
    for di in range(-1, 2, 1):
        for dj in range(-1, 2, 1):
            if arr[i + di][j + dj] == 1:
                return False
    
    return True
 
def solution(N: int, arr: List[List[str]]) -> int | bool:
    # [horizontal, vertical]
    visited = [[[INF, INF] for _ in range(N)] for _ in range(N)]
    queue = deque()

    # find start & end
    b = 0; e = 0
    si = 0; sj = 0; s_is_vertical = 0
    ei = 0; ej = 0; e_is_vertical = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '1':
                arr[i][j] = 1
                continue

            elif arr[i][j] == 'B':
                b += 1
                if b == 2:
                    si = i
                    sj = j
                    if i < N -1 and arr[i + 1][j] == 'B':
                        s_is_vertical = 1

            elif arr[i][j] == 'E':
                e += 1
                if e == 2:
                    ei = i
                    ej = j
                    if i < N -1 and arr[i + 1][j] == 'E':
                        e_is_vertical = 1
            
            arr[i][j] = 0

    # set the start
    visited[si][sj][s_is_vertical] = 0
    queue.append((si, sj, s_is_vertical))

    # bfs algorithm
    while queue:
        i, j, is_vertical = queue.popleft()
        distance = visited[i][j][is_vertical]

        # found answer
        if i == ei and j == ej and is_vertical == e_is_vertical:
            return distance

        # the tree is in vertical direction
        if is_vertical:
            # left
            if j > 0 and not arr[i - 1][j - 1] and not arr[i][j - 1] and not arr[i + 1][j - 1] and distance + 1 < visited[i][j - 1][is_vertical]:
                visited[i][j - 1][is_vertical] = distance + 1
                queue.append((i, j - 1, is_vertical))

            # right
            if j < N - 1 and not arr[i - 1][j + 1] and not arr[i][j + 1] and not arr[i + 1][j + 1]  and distance + 1 < visited[i][j + 1][is_vertical]:
                visited[i][j + 1][is_vertical] = distance + 1
                queue.append((i, j + 1, is_vertical))

            # up
            if i > 1 and not arr[i - 2][j] and distance + 1 < visited[i - 1][j][is_vertical]:
                visited[i - 1][j][is_vertical] = distance + 1
                queue.append((i - 1, j, is_vertical))

            # down
            if i < N - 2 and not arr[i + 2][j] and distance + 1 < visited[i + 1][j][is_vertical]:
                visited[i + 1][j][is_vertical] = distance + 1
                queue.append((i + 1, j, is_vertical))

        # the tree is in horizontal direction
        else:
            # left
            if j > 1 and not arr[i][j - 2] and distance + 1 < visited[i][j - 1][is_vertical]:
                visited[i][j - 1][is_vertical] = distance + 1
                queue.append((i, j - 1, is_vertical))

            # right
            if j < N - 2 and not arr[i][j + 2] and distance + 1 < visited[i][j + 1][is_vertical]:
                visited[i][j + 1][is_vertical] = distance + 1
                queue.append((i, j + 1, is_vertical))

            # up
            if i > 0 and not arr[i - 1][j - 1] and not arr[i - 1][j] and not arr[i - 1][j + 1] and distance + 1 < visited[i - 1][j][is_vertical]:
                visited[i - 1][j][is_vertical] = distance + 1
                queue.append((i - 1, j, is_vertical))

            # down
            if i < N - 1 and not arr[i + 1][j - 1] and not arr[i + 1][j] and not arr[i + 1][j + 1] and distance + 1 < visited[i + 1][j][is_vertical]:
                visited[i + 1][j][is_vertical] = distance + 1
                queue.append((i + 1, j, is_vertical))

        # rotate
        if is_rotationable(N, arr, i, j) and distance + 1 < visited[i][j][1 - is_vertical]:
            visited[i][j][1 - is_vertical] = distance + 1
            queue.append((i, j, 1 - is_vertical))

    return False


if __name__ == "__main__":
    N = int(input())
    arr = [list(input().rstrip()) for _ in range(N)]

    answer = solution(N, arr)
    print(answer if answer else 0)