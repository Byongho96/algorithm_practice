from heapq import *
import sys
input = sys.stdin.readline

# def prim(s):
#     INF = 10001
#     visited = [0] * (N + 1)     # MST에 포함된 노드들, 인덱스를 위해 (N+1)개
#     weight = [INF] * (N + 1)    # 각 노드별 MST에 포함될 때의 소비한 가중치, 인덱스를 윌해 (N+1)개
#
#     weight[s] = 0               # 시작노드는 가중치 0
#     for _ in range(N):          # 총 N개의 노드를 MST에 포함시킬 때까지 반복
#
#         # MST에 넣을 노드 선택 (MST에 인접한 노드 중 가장 가중치가 작은 것)
#         mn = INF
#         i_min = 0
#         for i in range(1, N + 1):   # 모든 노드를 돌면서, 인접하고 & 가중치가 가장 작은 것
#             if not visited[i] and weight[i] < mn:
#                 mn = weight[i]
#                 i_min = i
#         visited[i_min] = 1          # MST에 포함
#
#         # 새로 MST에 추가된 노드에 대해서 인접 노드 가중치 최솟값으로 업데이트
#         for w, adj in adjLst[i_min]:
#             if not visited[adj] and weight[adj] > w:    # MST의 인접노드이며 & 최솟값일 경우 업데이트
#                 weight[adj] = w
#
#     print(sum(weight[1:]))      # 임의로 추가한 0번 인덱스외의 값을 더해서 출력
#

def prim2(s):
    INF = 10001
    visited = [0] * (N + 1)     # MST에 포함된 노드들, 인덱스를 위해 (N+1)개
    weight = [INF] * (N + 1)    # 각 노드별 MST에 포함될 때의 소비한 가중치, 인덱스를 윌해 (N+1)개

    weight[s] = 0               # 시작노드는 가중치 0
    edges_heap = [(0, s)]       # 시작노드에 대한 정보를 heap에 넣어줘야 함 (가중치, 노드)
    heapify(edges_heap)         # heapify함수로 원래 list였던 edges_heap을 자료구조 heap으로 변경시켜줌

    while edges_heap:           # 힙이 소진될 때까지 반복
        mn, i_min = heappop(edges_heap) # python의 heapq는 최소힙으로, 항상 최소 가중치의 노드가 나옴
        if not visited[i_min]:          # 아직 MST에 포함되지 않은 인접 노드일 경우, 연산진행
            visited[i_min] = 1              # MST에 포함시킴
            for w, adj in adjLst[i_min]:    # 새로 MST에 추가된 노드에 대해서 인접 노드 가중치 최솟값으로 업데이트
                if not visited[adj] and weight[adj] > w:    # MST의 인접노드이며 & 최솟값일 경우 업데이트
                    weight[adj] = w
                    heappush(edges_heap, (w, adj))          # 해당 정보는 heap에 넣어줌 (가중치, 노드)

    print(sum(weight[1:]))

N = int(input())
M = int(input())

# adjLst = [[] for _ in range(N + 1)]
# for _ in range(M):
#     i, j, w = map(int, input().split())
#     adjLst[i].append((w, j))
#     adjLst[j].append((w, i))
# prim(1)

adjLst = [[] for _ in range(N + 1)]
for _ in range(M):
    i, j, w = map(int, input().split())
    adjLst[i].append((w, j))
    adjLst[j].append((w, i))

prim2(1)

################################################################
def kruskal():
    # find set
    def find_set(x):
        while x != par[x]:
            x = par[x]
        return x

    # union by rank
    def union(x, y):
        X = find_set(x)
        Y = find_set(y)
        if rank[X] == rank[Y]:  # 둘 set의 rank가 같을 경우
            par[Y] = X              # Y집합을 X집합에 달아주고
            rank[X] += 1            # X집합의 rank를 +1 해준다.
        elif rank[X] < rank[Y]: # X집합의 rank가 Y집합보다 작을 경우
            par[X] = Y              # X집합을 Y집합에 달아준다
        else:                   # Y집합의 rank가 X집합보다 작을 경우
            par[Y] = X              # Y집합을 X집합에 달아준다.

    par = [i for i in range(N + 1)] # 모든 집합이 분리되어있다.
    rank = [1] * (N + 1)            # 모든 분리집합은 초기에 자기 자신밖에 없으므로 rank가 1이다.

    cnt = 0                         # 연결된 노드 수
    weight = 0                      # 노드를 연결할 때의 가중치 합
    edges.sort(key = lambda x: x[2])# 모든 간선을 가중치가 작은 순서대로 정렬해준다.
    for i, j, w in edges:
        if find_set(i) != find_set(j):  # 노드 i와 노드 j가 다른 집합에 있을 경우에만
            union(i, j)                     # 둘을 union해준다
            weight += w                     # 가중치합 업데이트
            cnt += 1                        # 연결된 노드 수 +1
            if cnt == N:                    # N개의 노드가 연결되었다면 반복문 탈출
                break
    print(weight)

N = int(input())
M = int(input())


edges = [[0, 0, 0] for _ in range(M)]
for idx in range(M):    # (노드1, 노드2, 간선)의 튜플 구조로 간선정보 저장
    edges[idx][0], edges[idx][1], edges[idx][2] = map(int, input().split())
kruskal()