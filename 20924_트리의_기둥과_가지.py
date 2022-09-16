from collections import deque
import sys
input = sys.stdin.readline

def bfs_root(v):
    visited = [-1] * (N + 1)
    q = deque()

    visited[v[0]] = v[1]
    q.append(v)

    trunk = 0
    giga = 0
    while q:
        v = q.popleft()
        if not giga and len(adjLst[v[0]]) > 2:
            trunk = visited[v[0]]
            giga = 1
        for w in adjLst[v[0]]:
            if visited[w[0]] == -1:
                q.append(w)
                visited[w[0]] = visited[v[0]] + w[1]

    if not giga:
        trunk = max(visited)
    return trunk, max(visited) - trunk


N, R = map(int, input().split())

adjLst = [[] for _ in range(N + 1)]
for _ in range(N-1):
    a, b, d = map(int, input().split())
    adjLst[a].append((b, d))
    adjLst[b].append((a, d))

trunk, branch = bfs_root((1, 0))

print(trunk, branch)
