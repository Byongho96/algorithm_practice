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
    distance = [INF] * (N + 1)              # 출발지로부터 모든 노드까지의 최단경로를 저장할 리스트
    distance[s] = 0                         # 출발지 자기 자신까지는 비용이 0

    heap = []
    heapq.heappush(heap, (0, s))            # 출발지 노드를 초깃값으로 입력 (비용, 노드)

    while heap:
        dist, now = heapq.heappop(heap)     # 주변 노드 중 가장 비용이 짧은 노드를 pop
        if distance[now] < dist:            # 현재 노드가 처리된적 있다면 무시
            continue
        for next in range(1, N + 1):        # 현재 노드의 주변 노드를 탐색
            cost = dist + arr[now][next]        # 현재 노드를 거치는 값을 임시로 계산
            if cost < distance[next]:           # 현재 노드를 거치는 것이 더 빠를 경우
                distance[next] = cost               # 해당 노드의 최단경로 갱신
                heapq.heappush(heap, (cost, next))  # 힙에 노드정보 입력 (비용, 노드)

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
    if record[s]:                       # record[s]가 비어있지 않다면 바로 값을 읽어와서 결과를 출력한다.
        if record[s][e] <= t:
            print('Enjoy other party')
        else:
            print('Stay here')
    else:                               # record[s]가 비어있다면 다익스트라 연산을 수행한다.
        if dijkstra2_2(s, e) <= t:
            print('Enjoy other party')
        else:
            print('Stay here')


#####################################################################################

# # https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-11265-%EB%81%9D%EB%82%98%EC%A7%80-%EC%95%8A%EB%8A%94-%ED%8C%8C%ED%8B%B0-Floyd-Warshall
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for n1 in range(N):
        for n2 in range(N):
            # arr[n1][n2] = min(arr[n1][n2], arr[n1][k] + arr[k][n2])
            if arr[n1][n2] > arr[n1][k] + arr[k][n2]:   # 시간개선: 위에 코드로 무작정 min연산 하지 말고, 조건문을 걸어준다.
                arr[n1][n2] = arr[n1][k] + arr[k][n2]

result = []
for _ in range(M):  # 시간개선: for i in range 대신 for _ in range를 쓴다.
    s, e, t = map(int, input().split())
    if arr[s-1][e-1] <= t:
        print('Enjoy other party')
    else:
        print('Stay here')

# print('\n'.join(result))
