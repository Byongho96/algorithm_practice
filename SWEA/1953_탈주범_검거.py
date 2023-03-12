import sys
from collections import deque
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

out_dict = {0: [], 1: [(1, 0), (0, 1), (-1, 0), (0, -1)], 2: [(1, 0), (-1, 0)], 3:[(0, 1), (0, -1)],
       4: [(-1, 0), (0, 1)], 5:[(1, 0), (0, 1)], 6:[(1, 0), (0, -1)], 7:[(-1, 0), (0, -1)]}
in_dict = {0: [], 1: [(1, 0), (0, 1), (-1, 0), (0, -1)], 2: [(1, 0), (-1, 0)], 3:[(0, 1), (0, -1)],
       4: [(1, 0), (0, -1)], 5:[(-1, 0), (0, -1)], 6:[(-1, 0), (0, 1)], 7:[(1, 0), (0, 1)]}

def bfs(i, j):
    visited = [[0] * M for _ in range(N)]
    q = deque()

    visited[i][j] = 1
    cnt = 0
    q.append((i, j))

    while q:
        i, j = q.popleft()
        if visited[i][j] == L + 1:
            return cnt
        cnt += 1
        for di, dj in out_dict[arr[i][j]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and (di, dj) in in_dict[arr[ni][nj]]:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N, M, si, sj, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = bfs(si, sj)

    print(f'#{tc} {result}')