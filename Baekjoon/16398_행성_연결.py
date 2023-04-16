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
    X = find_set(par, x)
    Y = find_set(par, y)

    X_rank = rank[X]
    Y_rank = rank[Y]

    if X_rank == Y_rank:
        par[Y] = X
        rank[X] += 1
    elif rank[X] > rank[Y]:
        par[Y] = X
    else:
        par[X] = Y

def kruskal(N, arr):
    par = [node for node in range(N)]
    rank = [1] * N

    mst_size = 0    # MST로 연결된 노드의 갯수
    sum_weight = 0  # MST를 연결하기 위한 총 비용

    # 인접행렬 arr를 힙으로 변환
    heap = []
    for i in range(N):
        for j in range(i + 1, N):
            heapq.heappush(heap, (arr[i][j], i, j))

    while heap:
        w, n1, n2 = heapq.heappop(heap)
        if find_set(par, n1) != find_set(par, n2):  # n1, n2가 다른 집합에 속해있을 경우
            union_by_rank(par, rank, n1, n2)  # par, rank모두 참조형 타입으로 넘겨준다.
            sum_weight += w
            mst_size += 1
            if mst_size == N:   # 모든 노드를 연결했다면 종료
                break
    
    return sum_weight

if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    INF = 100000000 * 1000
    start = 0
    # answer = prim(N, arr, INF, start) # 512ms
    answer = prim_with_heap(N, arr, INF, start)   # 480ms
    # answer = kruskal(N, arr)    # 2428ms

    print(answer)

