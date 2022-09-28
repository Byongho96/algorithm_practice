from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline

def bfs(si, sj):
    visited = [[0] * (M + 1) for _ in range(N + 1)]
    q = deque()

    visited[si][sj] = 1
    q.append((si, sj))

    while q:
        i, j = q.popleft()
        # print(i, j)
        # print(adjLst[i][j])
        for ni, nj in adjLst[i][j]:
            if not visited[ni][nj]:
                if ni == ei and nj == ej:
                    return visited[i][j]
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))


M, N = map(int, input().split())
K = int(input())

direction = [0] * (K + 1)
starts = [0] * (K + 1)
ends = [0] * (K + 1)
for _ in range(K):
    i, j1, i1, j2, i2 = map(int, input().split())
    if j1 == j2:        # 세로방향
        direction[i] = 1
        if i1 <= i2:
            starts[i] = (i1, j1)
            ends[i] = (i2, j2)
        else:
            starts[i] = (i2, j2)
            ends[i] = (i1, j1)
    else:               # 가로방향
        if j1 <= j2:
            starts[i] = (i1, j1)
            ends[i] = (i2, j2)
        else:
            starts[i] = (i2, j2)
            ends[i] = (i1, j1)


sj, si, ej, ei = map(int, input().split())

# 인접 리스트 만들기
# 규칙 1. 노드: 서로 다른 방향의 노선이 만나는 점은 노드
# 규칙 2. 노드: 서로 같은 방향의 한 노선 끝 지점이 다른 노선에 있으면 노드
# 규칙 3. 노드: 시작 지점과 끝 지점도 노드
# 규칙 4. 엣지: 같은 노선 위에 모든 노드들은 연결
adjLst = [[[] for _ in range(M + 1)] for _ in range(N + 1)]
for idx in range(1, K + 1):
    d = direction[idx]
    fi, fj = starts[idx]
    li, lj = ends[idx]

    nodes = []
    for bus in range(1, K + 1):
        if bus == idx:
            pass
        elif direction[bus] == d:   # 같은 방향 노선일 경우
            fi2, fj2 = starts[bus]
            li2, lj2 = ends[bus]
            if d and fj == fj2:                     # 세로 방향
                if fi2 <= fi <= li2:
                    nodes.append((fi, fj))
                if fi2 <= li <= li2:
                    nodes.append((li, lj))
            elif not d and fi == fi2:               # 가로 방향
                if fj2 <= fj <= lj2:
                    nodes.append((fi, fj))
                if fj2 <= lj <= lj2:
                    nodes.append((li, lj))
        else:                       # 다른 방향 노선일 경우
            fi2, fj2 = starts[bus]
            li2, lj2 = ends[bus]
            if d and fi <= fi2 <= li:                       # 세로 방향
                if fj2 <= fj <= lj2:
                    nodes.append((fi2, fj))
            elif not d and fj <= fj2 <= lj:                       # 가로방향
                if fi2 <= fi <= li2:
                    nodes.append((fi, fj2))
    if d:
        if sj == fj and fi <= si <= li:
            nodes.append((si, sj))
        if ej == fj and fi <= ei <= li:
            nodes.append((ei, ej))
    else:
        if si == fi and fj <= sj <= lj:
            nodes.append((si, sj))
        if ei == fi and fj <= ej <= lj:
            nodes.append((ei, ej))


    for i, j in nodes:
        adjLst[i][j].extend(nodes)

# bfs 탐색
print(bfs(si, sj))