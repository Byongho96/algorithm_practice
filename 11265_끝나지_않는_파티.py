import sys
from collections import deque
import heapq

input = sys.stdin.readline

# def dijkstra1(s, e):
#     INF = 1000000001
#     distance = [INF] * (N + 1)
#     visited = [0] * (N + 1)
#
#     distance[s] = 0
#     for _ in range(N):
#         mn = INF
#         i_min = 0
#         for i in range(1, N + 1):
#             if not visited[i] and distance[i] < mn:
#                 mn = distance[i]
#                 i_min = i
#         visited[i_min] = 1
#         for w in range(1, N + 1):
#             # if not visited[w]:
#             distance[w] = min(distance[w], distance[i_min] + arr[i_min-1][w-1])
#
#     record[s] = distance
#     return distance[e]


# def dijkstra2(s, e):
#     INF = 1000000001
#     distance = [INF] * (N + 1)
#
#     heap = []
#     heapq.heappush(heap, (0, s))
#     distance[s] = 0
#
#     while heap:
#         dist, now = heapq.heappop(heap)
#         if distance[now] < dist:  # 현재 노드가 처리된적 있다면 무시
#             continue
#         for next in range(1, N + 1):  # 현재 노드의 주변 노드를 탐색
#             cost = dist + arr[now-1][next-1]
#             if cost < distance[next]:  # 현재 노드를 거치는 것이 더 빠를 경우
#                 distance[next] = cost
#                 heapq.heappush(heap, (cost, next))
#
#     record[s] = distance
#     return distance[e]

def dijkstra2_2(s, e):
    INF = 1000000001
    distance = [INF] * (N + 1)

    heap = []
    heapq.heappush(heap, (0, s))
    distance[s] = 0

    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:  # 현재 노드가 처리된적 있다면 무시
            continue
        for next in range(1, N + 1):  # 현재 노드의 주변 노드를 탐색
            cost = dist + arr[now][next]
            if cost < distance[next]:  # 현재 노드를 거치는 것이 더 빠를 경우
                distance[next] = cost
                heapq.heappush(heap, (cost, next))

    record[s] = distance
    return distance[e]

# def bfs(s, e):
#     INF = 1000000001
#     distance = [INF] * (N + 1)
#     q = deque()
#
#     q.append(s)
#     distance[s] = 0
#
#     while q:
#         v = q.popleft()
#         for w in range(1, N + 1):
#             if distance[w] > distance[v] + arr[v-1][w-1]:
#                 distance[w] = distance[v] + arr[v-1][w-1]
#                 q.append(w)
#
#     record[s] = distance
#     return distance[e]


N, M = map(int, input().split())
arr = [[]] + [[0] + list(map(int, input().split())) for _ in range(N)]

record = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    if record[s]:
        if record[s][e] <= t:
            print('Enjoy other party')
        else:
            print('Stay here')
    else:
        if dijkstra2_2(s, e) <= t:
            print('Enjoy other party')
        else:
            print('Stay here')


#####################################################################################

# # https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-11265-%EB%81%9D%EB%82%98%EC%A7%80-%EC%95%8A%EB%8A%94-%ED%8C%8C%ED%8B%B0-Floyd-Warshall
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# for k in range(N):
#     for n1 in range(N):
#         for n2 in range(N):
#             # arr[n1][n2] = min(arr[n1][n2], arr[n1][k] + arr[k][n2])
#             if arr[n1][n2] > arr[n1][k] + arr[k][n2]:
#                 arr[n1][n2] = arr[n1][k] + arr[k][n2]
#
# result = []
# for _ in range(M):
#     s, e, t = map(int, input().split())
#     if arr[s-1][e-1] <= t:
#         print('Enjoy other party')
#     else:
#         print('Stay here')
#
# # print('\n'.join(result))
