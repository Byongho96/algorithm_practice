import heapq

def dijkstra(N, M, start, items, adjLst):
    # 초깃값
    INF = 15 * 100
    distance = [INF] * (N + 1)

    # 시작점 지정
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    collected_items = 0
    while heap:
        dist, nearest = heapq.heappop(heap) # 가장 낮은 가중치의 노드를 pop

        if distance[nearest] > M:
            return collected_items

        if distance[nearest] < dist:    # 이미 거리 계산이 완료된 노드 무시
            continue

        # 실제로 완료된 거리 계산이 완료된 노드에 포함되는 시점
        collected_items += items[nearest]

        for adj, weight in adjLst[nearest]: # 인접 노드들의 거리를 계산하여 heap에 push
            new_dist  = dist + weight
            if new_dist < distance[adj]:
                distance[adj] = new_dist
                heapq.heappush(heap, (new_dist, adj))

    return collected_items

if __name__ == "__main__":
    N, M, E = map(int, input().split()) # 노드 갯수, 수색 가능 값, 엣지 갯수
    items = [0] + list(map(int, input().split())) # 노드에 대응하는 아이템 갯수

    # adjLst 생성 
    adjLst = [[] for _ in range(N + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adjLst[n1].append((n2, w))
        adjLst[n2].append((n1, w))

    max_item = 0
    for start in range(1, N + 1): # 모든 노드를 한번씩 시작점으로 해서, dijkstra알고리즘을 돌린다.
        max_item = max(max_item, dijkstra(N, M, start, items, adjLst))

    print(max_item)




# node, mx_search, road = map(int, input().split())

# treasures = [0] + list(map(int, input().split()))

# adjLst = [[] for _ in range(node + 1)]
# for i in range(road):
#     n1, n2, w = map(int, input().split())
#     adjLst[n1].append((w, n2))
#     adjLst[n2].append((w, n1))

# def dijkstra(s):
#     distance = [16] * (node + 1)
#     visited = [0] * (node + 1)

#     distance[s] = 0
#     gathered = 0

#     for _ in range(node):
#         mn = mx_search + 1
#         i_mn = 0
#         for i in range(1, node + 1):
#             if not visited[i] and distance[i] < mn:
#                 mn = distance[i]
#                 i_mn = i
#         if not i_mn:
#             break
#         visited[i_mn] = 1
#         gathered += treasures[i_mn]
#         for weight, node2 in adjLst[i_mn]:
#             distance[node2] = min(distance[node2], distance[i_mn] + weight)

#     return gathered

# result = 0
# for i in range(1, node + 1):
#     result = max(result, dijkstra(i))

# print(result)