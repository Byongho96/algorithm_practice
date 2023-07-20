from collections import defaultdict
import heapq

def prim_with_heap(N, costs):     
    INF = float('inf')  # weight의 제한 사항이 주어지지 않음
        
    # 인접리스트 생성
    adjLst = defaultdict(list)
    for i, j, w in costs:
        adjLst[i].append((j, w))
        adjLst[j].append((i, w))
        
    # 초깃값 셋팅
    weight = [INF] * N
    linked = [0] * N

    # 시작점 셋팅
    start = costs[0][0]
    heap = []
    heapq.heappush(heap, (0, start))
    weight[start] = 0

    while heap:
        w, cur = heapq.heappop(heap)

        if weight[cur] < w: # 새로 거리가 갱신된 노드는 무시
            continue

        linked[cur] = 1    # MST에 해당 노드 포함

        # 새로 확정된 노드의 인접 노드들 거리 갱신
        for adj, adj_w in adjLst[cur]:
            if not linked[adj] and adj_w < weight[adj]:
                weight[adj] = adj_w
                heapq.heappush(heap, (adj_w, adj))

    return sum(weight)

# 트리의 루트 노드를 찾는 함수
def find_set(par, x):
    while x != par[x]:
        x = par[x]
    return x

# 두 트리를 병합하는 함수
def union_by_rank(par, rank, x, y):
    X = find_set(par, x)
    Y = find_set(par, y)

    X_rank = rank[X]
    Y_rank = rank[Y]

    # 트리의 rank(depth)를 기준으로, 작은 것을 큰 것에 병합
    if X_rank == Y_rank:
        par[Y] = X
        rank[X] += 1
    elif rank[X] > rank[Y]:
        par[Y] = X
    else:
        par[X] = Y

def kruskal(N, costs):
    par = [node for node in range(N)]   # 부모 노두 정보를 담는 리스트
    rank = [1] * N                      # 루트 노드의 depth

    # 간선정보를 가중치를 기준으로 오름차순 정렬
    costs.sort(key=lambda x: x[2])

    mst_size = 1    # MST로 연결된 노드의 갯수
    sum_weight = 0  # MST를 연결하기 위한 총 비용

    for node_1, node_2, weight in costs:
        if find_set(par, node_1) == find_set(par, node_2):  # 이미 같은 집합일 경우, continue
            continue
        union_by_rank(par, rank, node_1, node_2)  # 연결
        sum_weight += weight
        mst_size += 1
        if mst_size == N:   # 모든 노드를 연결했다면 종료
            break

    return sum_weight

def solution(n, costs):
    
    # Prim 6, 2, 4, 11, 3, 6, 9, 2
    # answer = prim_with_heap(n, costs)
    # Kruskal. 1, 1, 2, 3, 3, 4, 4, 2
    answer = kruskal(n, costs)
    
    return answer