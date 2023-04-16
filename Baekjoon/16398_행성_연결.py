import heapq

def prim(N, arr, INF, start):
    weight = [INF] * N
    visited = [0] * N

    weight[start] = 0  # 시작점 셋팅

    for _ in range(N):
        mn = INF
        nearest = -1
        for node in range(N):
            if not visited[node] and weight[node] < mn:
                mn = weight[node]
                nearest = node

        visited[nearest] = True

        for adj in range(N):
            if not visited[adj]:
                adj_weight = arr[nearest][adj]
                weight[adj] = min(weight[adj], adj_weight)

    return sum(weight)

def prim_with_heap(N, arr, INF, start):
    weight = [INF] * N
    visited = [0] * N

    # 시작점 셋팅
    heap = []
    heapq.heappush(heap, (0, start))
    weight[start] = 0 

    while heap:
        w, nearest = heapq.heappop(heap)

        if weight[nearest] < w:
            continue

        visited[nearest] = 1

        for adj in range(N):
            adj_w = arr[nearest][adj]
            if not visited[adj] and adj_w < weight[adj]:
                weight[adj] = adj_w
                heapq.heappush(heap, (adj_w, adj))

    return sum(weight)

def find_set(par, x):
    while x != par[x]:
        x = par[x]
    return x

def union_by_rank(par, rank, x, y):
    X = find_set(x)
    Y = find_set(y)

    X_rank = rank[X]
    Y_rank = rank[Y]

    if X_rank == Y_rank:
        par[Y] = X
        rank[X] += 1
    elif rank[X] > rank[Y]:
        par[Y] = X
    else:
        par[X] = Y

# def kruskal(N, arr, INF, start):
#     par = [node for node in range(N)]
#     rank = [1] * N

#     mst_size = 0
#     weight = 0
#     edges.sort(key=weight)
#     for a, b, w in edges:
#         if find_set(a) != find_set(b):
#             union(a, b)
#             weight += w
#             cnt += 1
#             if cnt == V:
#                 break

if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    INF = 100000000 * 1000
    start = 0
    # answer = prim(N, arr, INF, start)
    # answer = prim_with_heap(N, arr, INF, start)
    answer = kruskal(N, arr, INF, start)

    print(answer)

