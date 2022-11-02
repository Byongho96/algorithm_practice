from heapq import *
import sys
input = sys.stdin.readline

# Basic Dijkstra
def dijkstra(v):
    visited = [0] * (V + 1)
    weight = [200000] * (V + 1)

    weight[v] = 0
    for _ in range(V):
        mn_idx = -1
        mn = 200000
        for i in range(1, V+1):
            if not visited[i] and weight[i] < mn:
                mn_idx = i
                mn = weight[i]
        visited[mn_idx] = 1
        for w, _, adj in adjLst[mn_idx]:
            if mn + w < weight[adj]:
                weight[adj] = mn + w
    return weight

# Dijkstra with heap
def dijkstra_heap(v):
    weight = [200000] * (V + 1)
    weight[v] = 0

    h =[(0, v)]
    heapify(h)
    while h:
        w, i = heappop(h)
        if w > weight[i]:   # 이 구문 때문에 굳이 visited를 체크할 필요가 없게됨.
            continue
        for adj_w, adj in adjLst[i]:
                cost = w + adj_w
                if cost < weight[adj]:
                    weight[adj] = cost
                    heappush(h, (cost, adj))

    return weight


V, E = map(int, input().split())
K = int(input())

adjLst = [[] for _ in range((V + 1))]
for _ in range(E):
    i, j, w = map(int, input().split())
    adjLst[i].append((w, j))

weight = dijkstra_heap(K)
for w in weight[1:]:
    if w == 200000:
        print('INF')
    else:
        print(w)