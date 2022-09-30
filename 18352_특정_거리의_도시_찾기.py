from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    distance = [N] * (N + 1)
    q = deque()
    q.append(v)
    distance[v] = 0

    cities = []
    while q:
        v = q.popleft()
        if distance[v] == K:
            cities.append(v)
        elif distance[v] > K:
            cities.sort()
            return cities
        for w in adjLst[v]:
            if distance[v] + 1 < distance[w]:
                distance[w] = distance[v] + 1
                q.append(w)
    cities.sort()
    return cities

# def dijkstra(v):
#     d = [N] * (N + 1)
#     d[v] = 0
#
#     U = []
#     cities = []
#     for _ in range(N):
#         w = v
#         mn = N
#         for i in range(1, N + 1):
#             if i not in U and d[i] < mn:
#                 w = i
#                 mn = d[i]
#         U.append(w)
#         if d[w] == K:
#             cities.append(w)
#         elif d[w] > K:
#             cities.sort()
#             return cities
#         for adj in adjLst[w]:
#             if adj not in U:
#                 d[adj] = min(d[adj], d[w] + 1)
#     cities.sort()
#     return cities

N, M, K, X = list(map(int, input().split()))
adjLst = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjLst[a].append(b)

# result = dijkstra(X)
result = bfs(X)
if not result:
    print(-1)
else:
    print(*result, sep='\n')