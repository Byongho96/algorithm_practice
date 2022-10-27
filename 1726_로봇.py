import sys
from pprint import pprint
from collections import deque
input = sys.stdin.readline

ref = {1: (0, 0, 2, 1, 1), 2: (0, 2, 0, 1, 1), 3: (0, 1, 1, 0, 2), 4: (0, 1, 1, 2, 0)}

dir_ref = {0: (0, 1), 1: (0, -1), 2: (1, 0), 3: (-1, 0)}
turn_ref = {0: (2, 3), 1: (2, 3), 2: (0, 1), 3: (0, 1)}

def bfs():  #344ms
    INF= 20002
    visited = [[INF] * (M + 2) for _ in range(N + 2)]
    q = deque()

    visited[si][sj] = 0
    q.append((si, sj, sd, 0, 3))

    mn = INF
    while q:
        i, j, d, cost, dist = q.popleft()
        if i == ei and j == ej:
            mn = min(mn, cost + ref[d][ed])
        for di, dj, nd in ((0, 1, 1), (0, -1, 2), (1, 0, 3), (-1, 0, 4)):
            ni = i + di
            nj = j + dj
            if not arr[ni][nj]:
                if d != nd:
                    new_cost = cost + ref[d][nd] + 1
                    new_dist = 1
                elif dist != 3:
                    new_cost = cost
                    new_dist = dist + 1
                else:
                    new_cost = cost + 1
                    new_dist = 1
                if new_cost <= visited[ni][nj]:
                    visited[ni][nj] = new_cost
                    q.append((ni, nj, nd, new_cost, new_dist))
                elif new_cost == visited[ni][nj] + 1:
                    q.append((ni, nj, nd, new_cost, new_dist))
    # pprint(visited)
    print(mn)

def bfs2(): # 100ms
    INF= 20002
    visited = [[[0] * 4 for _ in range(M)] for _ in range(N)]
    q = deque()

    visited[si-1][sj-1][sd-1] = 1
    q.append((si-1, sj-1, sd-1))

    while q:
        i, j, d = q.popleft()
        if i == ei-1 and j == ej-1 and d == ed-1:
            return visited[ei-1][ej-1][ed-1] - 1

        # 무조건 1씩 증가하도록 설계
        # 거리증가
        for dist in range(1, 4):
            ni = i + dir_ref[d][0] * dist
            nj = j + dir_ref[d][1] * dist
            if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj]:
                if not visited[ni][nj][d]:
                    q.append((ni, nj, d))
                    visited[ni][nj][d] = visited[i][j][d] + 1
            else:
                break

        # 방향변환
        for nd in turn_ref[d]:
            if not visited[i][j][nd]:
                q.append((i, j, nd))
                visited[i][j][nd] = visited[i][j][d] + 1
    pprint(visited)

N, M = map(int, input().split())
# arr = [[1]*(M+2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + [[1]*(M+2)]
arr = [list(map(int, input().split())) for _ in range(N)]
si, sj, sd = map(int, input().split())
ei, ej, ed = map(int, input().split())

# bfs()
print(bfs2())
# mn = 20002
# dfs(si, sj, sd, 0, 3)
# print(mn)



