import heapq
import sys
input = sys.stdin.readline

# # KRUSKAL. 352ms
# # 경로압축??
# def find_set(x):
#     while x != par[x]:
#         x = par[x]
#     return x
#
# # union by rank
# def union(x, y):
#     X = find_set(x)
#     Y = find_set(y)
#     if rank[X] == rank[Y]:
#         par[Y] = X
#         rank[X] += 1
#     elif rank[X] < rank[Y]:
#         par[X] = Y
#     else:
#         par[Y] = X
#
# V, E = map(int, input().split())
# par = [i for i in range(V + 1)]
# rank = [0] * (V + 1)
#
# edges = [[] for _ in range(E)]
# for i in range(E):
#     edges[i] = list(map(int, input().split()))
#
# edges.sort(key=lambda x: x[2])
#
# cnt = 0
# weight = 0
# for a, b, w in edges:
#     if find_set(a) != find_set(b):
#         union(a, b)
#         weight += w
#         cnt += 1
#         if cnt == V - 1:
#             break
# print(weight)


# PRIM. 584ms
V, E = map(int, input().split())
adjLst = [[] for _ in range(V + 1)]
for i in range(E):
    a, b, w = map(int, input().split())
    adjLst[a].append([w, a, b])
    adjLst[b].append([w, b, a])

MST = [0] * (V + 1)
MST[1] = 1
heap = adjLst[1]
heapq.heapify(heap)
weight = 0

tree = []
while heap:
    w, a, b = heapq.heappop(heap)
    if not MST[b]:
        MST[b] = 1
        weight += w
        for edge in adjLst[b]:      # WARNING: for문이 무한반복되는 경우, adjLst가 바뀜!!
            if not MST[edge[2]]:
                heapq.heappush(heap, edge)

print(weight)