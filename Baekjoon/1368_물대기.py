import sys
import heapq
from typing import List

input = sys.stdin.readline

INF = 100001

def solution_prim(N: int, start:int, adjLst: List[List[int]]):
    weight = [INF] * (N + 1)
    visited = [False] * (N + 1)

    # set the start
    heap = [(0, start)]
    weight[start] = 0

    while heap:
        w, cur = heapq.heappop(heap)

        # filter the invalid
        if weight[cur] < w:
            continue

        visited[cur] = True  

        # traverse the adjacents
        for adj in range(N + 1):
            if not visited[adj] and adjLst[cur][adj] < weight[adj]:
                weight[adj] = adjLst[cur][adj]
                heapq.heappush(heap, (adjLst[cur][adj], adj))

    return sum(weight)


if __name__ == "__main__":
    # the number of fields
    N = int(input())

    # digging cost
    dig_costs = [0] * N
    for i in range(N):
        dig_costs[i] = int(input())

    # connect costs including water source
    adjLst = [[0] + dig_costs] + [[dig_costs[i]] + list(map(int, input().split())) for i in range(N)]

    answer = solution_prim(N, 0, adjLst)
    print(answer)


# import sys
# import heapq

# input = sys.stdin.readline


# def prim2(N, dig_cost, adjLst):
#     weight = [100001] * N
#     visited = [False] * N
#     heap = []

#     for i in range(N):
#         heapq.heappush(heap, (dig_cost[i], i))

#     # run prim
#     while heap:
#         w, cur = heapq.heappop(heap)

#         # filter invalid info
#         if weight[cur] < w:
#             continue

#         # visit node
#         visited[cur] = True
#         weight[cur] = w

#         # traverse adjacent nodes
#         for adj in range(N):
#             w = adjLst[cur][adj]
#             if not visited[adj] and w < weight[adj]:
#                 weight[adj] = w
#                 heapq.heappush(heap, (w, adj))

#     return sum(weight)


# if __name__ == "__main__":
#     N = int(input())
#     dig_cost = [int(input()) for _ in range(N)]
#     adjLst = [list(map(int, input().split())) for _ in range(N)]

#     answer = prim2(N, dig_cost, adjLst)
#     print(answer)
