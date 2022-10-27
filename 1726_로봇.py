from pprint import pprint
import sys
from collections import deque
input = sys.stdin.readline

# 동서남북에 대한 동서남북으로 방향전환 시 비용
ref = {1: (0, 0, 2, 1, 1), 2: (0, 2, 0, 1, 1), 3: (0, 1, 1, 0, 2), 4: (0, 1, 1, 2, 0)}

def bfs(si, sj, sd, ei, ej, ed):
    visited = [[20002] * (M + 2) for _ in range(N + 2)]
    q = deque()

    visited[si][sj] = 0
    q.append((si, sj, sd, 3, 0))

    mn = 20002
    while q:
        i, j, d, m, c = q.popleft()
        # visit((i, j))
        if i == ei and j == ej:
            mn = min(mn, c + ref[d][ed])
            continue
        for di, dj, dm in ((0, 1, 1), (0, -1, 2), (1, 0, 3), (-1, 0, 4)):
            ni = i + di
            nj = j + dj
            if d != dm:
                nc = c + ref[d][dm] + 1
                nm = 1
            elif m != 3:
                nc = c
                nm = m + 1
            else:
                nc = c + 1
                nm = 1
            # print(ni, nj, c, d, dm)
            if not arr[ni][nj] and nc <= visited[ni][nj]:
                visited[ni][nj] = nc
                q.append((ni, nj, dm, nm, nc))

    # pprint(visited)
    print(mn)

N, M = map(int, input().split())
arr = [[1]*(M+2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + [[1]*(M+2)]
si, sj, sd = map(int, input().split())
ei, ej, ed = map(int, input().split())

bfs(si, sj, sd, ei, ej, ed)

# 4 2
# 0 0
# 0 0
# 1 0
# 0 0
# 1 1 3
# 4 1 3




