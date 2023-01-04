node, mx_search, road = map(int, input().split())

treasures = [0] + list(map(int, input().split()))

adjLst = [[] for _ in range(node + 1)]
for i in range(road):
    n1, n2, w = map(int, input().split())
    adjLst[n1].append((w, n2))
    adjLst[n2].append((w, n1))

def dijkstra(s):
    distance = [16] * (node + 1)
    visited = [0] * (node + 1)

    distance[s] = 0
    gathered = 0

    for _ in range(node):
        mn = mx_search + 1
        i_mn = 0
        for i in range(1, node + 1):
            if not visited[i] and distance[i] < mn:
                mn = distance[i]
                i_mn = i
        if not i_mn:
            break
        visited[i_mn] = 1
        gathered += treasures[i_mn]
        for weight, node2 in adjLst[i_mn]:
            distance[node2] = min(distance[node2], distance[i_mn] + weight)

    return gathered

import heapq

def dijkstra2(s):
    distance = [16] * (node + 1)
    
    heap = []
    heapq.heappush(heap, (0, s))
    distance[s] = 0
    
    gathered = 0

    while heap:
        weight, now = heapq.heappop(heap)
        if weight > mx_search:
            break
        if distance[now] < weight:
            continue
        gathered += treasures[now]
        for weight, node2 in adjLst[now]:
            cost = distance[now] + weight
            if cost < distance[node2]:
                distance[node2] = cost
                heapq.heappush(heap, (cost, node2))

    return gathered


result = 0
for i in range(1, node + 1):
    result = max(result, dijkstra2(i))

print(result)