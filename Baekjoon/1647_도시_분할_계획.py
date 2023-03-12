from heapq import *
import sys
input = sys.stdin.readline

# 최소스패닝 트리를 만든 후, 최댓값을 빼기.

# # Prim
# def prim(s):
#     visited = [0] * (N + 1)
#     weight = [1001] * (N + 1)
#     weight[s] = 0
#
#     mx = 0
#     for _ in range(N):
#         mn = 1001
#         mn_idx = -1
#         for i in range(1, N+1):
#             if not visited[i] and weight[i] < mn:
#                 mn = weight[i]
#                 mn_idx = i
#         mx = max(mx, mn)
#         next = mn_idx
#         visited[next] = 1
#         for w, adj in adjLst[next]:
#             if not visited[adj] and w < weight[adj]:
#                 weight[adj] = w
#
#     return sum(weight[1:]) - mx
#
# # Prim with heap
# def prim_heap(s):
#     visited = [0] * (N + 1)
#     weight = [1001] * (N + 1)
#     weight[s] = 0
#
#     h = [(0, s)]
#     heapify(h)
#     while h:
#         _, i = heappop(h)
#         if not visited[i]:          # 최소스패닝 트리이기 때문에 dijkstra처럼 비교연산자는 불가능
#             visited[i] = 1
#             for w, adj in adjLst[i]:
#                 if not visited[adj] and w < weight[adj]:    # not visited도 dijsktra와 다른 점
#                     weight[adj] = w
#                     heappush(h, (w, adj))
#     return sum(weight[1:]) - max(weight[1:])
#
#
# N, M = map(int, input().split())
# adjLst = [[] for _ in range(N + 1)]
#
# for _ in range(M):
#     i, j, w = map(int, input().split())
#     adjLst[i].append((w, j))
#     adjLst[j].append((w, i))
#
# print(prim_heap(1))

# Kruskal
def kruskal():
    # find_set
    def find_set(x):
        while x != par[x]:
            x = par[x]
        return x

    # union_by_rank
    def union(X, Y):
        if rank[X] == rank[Y]:
            par[Y] = X
            rank[X] += 1
        elif rank[X] < rank[Y]:
            par[X] = Y
        else:
            par[Y] = X

    par = [i for i in range(N + 1)]
    rank = [1] * (N + 1)

    cnt = 1
    weight = 0
    mx = 0
    edges.sort(key=lambda x: x[2])
    for i, j, w in edges:
        I = find_set(i)
        J = find_set(j)
        if I != J:
            union(I, J)
            cnt += 1
            weight += w
            mx = max(mx, w)
            if cnt == N:
                break
    print(weight - mx)

N, M = map(int, input().split())
edges = [[0, 0, 0] for _ in range(M)]
for i in range(M):
    edges[i][0], edges[i][1], edges[i][2] = map(int, input().split())

kruskal()