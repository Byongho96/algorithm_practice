from itertools import combinations
import sys
input = sys.stdin.readline

DIRECTION = None
mn_contaminated = 0

def dfs(N, M, arr, start_points):
    global mn_contaminated
    visited = [False] * (N * M)
    stack = [*start_points]

    for point in start_points:
        visited[point] = True

    contaminated = 0
    while stack:
        cur = stack.pop()

        if not arr[cur]:
            contaminated += 1

        if contaminated > mn_contaminated - 1:
            return contaminated

        for d in DIRECTION:
            nxt = cur + d
            if visited[nxt] or arr[nxt]:
                continue
            visited[nxt] = True
            stack.append(nxt)

    return contaminated


def solution(N, M, arr):
    global DIRECTION
    global mn_contaminated

    possible_walls = []
    start_points = []
    for i in range(M + 1, N * M - M - 1):
        if not arr[i]:
            possible_walls.append(i)
        elif arr[i] == 2:
            start_points.append(i)

    DIRECTION = (M, -M, 1, -1)
    mn_contaminated = len(possible_walls)

    for w1, w2, w3 in list(combinations(possible_walls, 3)):
        arr[w1] = 1
        arr[w2] = 1
        arr[w3] = 1

        mn_contaminated = min(mn_contaminated, dfs(N, M, arr, start_points))

        arr[w1] = 0
        arr[w2] = 0
        arr[w3] = 0

    return len(possible_walls) - mn_contaminated - 3

if __name__ == "__main__":
    N, M = map(int, input().split())
    N += 2
    M += 2

    # 가장자리를 1로 감싸서 1차원 배열로 받기
    arr = [1] * (N * M)
    for i in range(1, N - 1):
        arr[i * M + 1: (i + 1) * M - 1] = list(map(int, input().split()))

    answer = solution(N, M, arr)
    print(answer)
