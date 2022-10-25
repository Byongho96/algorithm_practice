from heapq import *
import sys
input = sys.stdin.readline

# def prim1(s):
#     INF = 10001
#     weight = [INF] * (N + 1)
#     visited = [0] * (N + 1)
#
#     weight[s] = 0
#     for _ in range(N-1):
#         mn = INF
#         i_min = 0
#         for i in range(1, N + 1):
#             if not visited[i] and weight[i] < mn:
#                 mn = weight[i]
#                 i_min = i
#         visited[i_min] = 1
#         for adj, w in adjLst[i_min]:
#             if not visited[adj] and weight[adj] > w:
#                 weight[adj] = w
#
#     print(sum(weight[1:]))
#
# def prim2(s):
#     INF = 10001
#     weight = [INF] * (N + 1)
#     weight[s] = 0
#
#     visited = [0] * (N + 1)
#     edges_heap = adjLst[s] + [(0, s)]
#     heapify(edges_heap)
#
#     while edges_heap:
#         mn, i_min = heappop(edges_heap)
#         if not visited[i_min]:
#             visited[i_min] = 1
#             for w, adj in adjLst[i_min]:
#                 if not visited[adj] and weight[adj] > w:
#                     weight[adj] = w
#                     heappush(edges_heap, (w, adj))
#     print(sum(weight[1:])

def kruskal():
    def find_set(x):
        while x != par[x]:
            x = par[x]
        return x

    # union by rank
    def union(x, y):
        X = find_set(x)
        Y = find_set(y)
        if rank[X] == rank[Y]:
            par[Y] = X
            rank[X] += 1
        elif rank[X] < rank[Y]:
            par[X] = Y
        else:
            par[Y] = X

    par = [i for i in range(N + 1)]
    rank = [0] * (N + 1)

    cnt = 0
    weight = 0
    edges.sort(key = lambda x: x[2])
    for i, j, w in edges:
        if find_set(i) != find_set(j):
            union(i, j)
            weight += w
            cnt += 1
            if cnt == N:
                break

    print(weight)

N = int(input())
M = int(input())

# adjLst = [[] for _ in range(N + 1)]
# for _ in range(M):
#     i, j, w = map(int, input().split())
#     adjLst[i].append((j, w))
#     adjLst[j].append((i, w))
# prim1(1)

# adjLst = [[] for _ in range(N + 1)]
# for _ in range(M):
#     i, j, w = map(int, input().split())
#     adjLst[i].append((w, j))
#     adjLst[j].append((w, i))
#
# prim2(1)

edges = [[0, 0, 0] for _ in range(M)]
for idx in range(M):
    edges[idx][0], edges[idx][1], edges[idx][2] = map(int, input().split())
kruskal()