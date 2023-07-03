import heapq
import sys
input = sys.stdin.readline
# KRUSKAL. 352ms

# 루트 노드 찾기
def find_root(x):
    while x != par[x]:
        x = par[x]
    return x

# Union by Rank(깊이 최소)
def union_by_rank(x, y):
    X = find_root(x)
    Y = find_root(y)
    if rank[X] < rank[Y]:
        par[X] = Y
        rank[Y] += 1
    else:
        par[Y] = X
        rank[X] += 1

if __name__ == '__main__':
    V, E = map(int, input().split())
    par = [i for i in range(V + 1)] # 부모 노드
    rank = [1] * (V + 1)            # 루트 노드의 길이

    # 간선 입력 받기
    edges = [ 0 for _ in range(E)]
    for i in range(E):
        edges[i] = list(map(int, input().split()))

    # kruskal을 위해 가중치 순으로 정렬
    edges.sort(key=lambda x: x[2])
    cnt =  1
    weight = 0
    for a, b, w in edges:
        if find_root(a) == find_root(b):
            continue
        union_by_rank(a, b)
        weight += w
        cnt += 1
        if cnt == V:
            break

    print(weight)


# PRIM. 584ms
# V, E = map(int, input().split())
# adjLst = [[] for _ in range(V + 1)]
# for i in range(E):
#     a, b, w = map(int, input().split())
#     adjLst[a].append([w, a, b])
#     adjLst[b].append([w, b, a])

# MST = [0] * (V + 1)
# MST[1] = 1
# heap = adjLst[1]
# heapq.heapify(heap)
# weight = 0

# tree = []
# while heap:
#     w, a, b = heapq.heappop(heap)
#     if not MST[b]:
#         MST[b] = 1
#         weight += w
#         for edge in adjLst[b]:      # WARNING: for문이 무한반복되는 경우, adjLst가 바뀜!!
#             if not MST[edge[2]]:
#                 heapq.heappush(heap, edge)

# print(weight)