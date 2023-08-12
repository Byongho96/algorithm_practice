# Dijkstra -> MST

import heapq
from collections import defaultdict

# To prevent timeout
import sys
input = sys.stdin.readline


def dijkstra(N, adjLst):
    INF = 1000 * 10
    distance = [INF] * (N + 1)
    previous = [0] * (N + 1)
    heap = []

    # Set the start point
    distance[1] = 0
    for weight, adj in adjLst[1]:
        distance[adj] = weight
        previous[adj] = 1
        heapq.heappush(heap, (weight, adj)) 

    while heap:
        dis, cur = heapq.heappop(heap)

        # Discard the invalid data
        if distance[cur] > dis:
            continue
        
        # Traverse the adjacnet nodes
        for weight, adj in adjLst[cur]:
            new_dis = dis + weight
            if new_dis < distance[adj]:
                distance[adj] = new_dis
                previous[adj] = cur
                heapq.heappush(heap, (new_dis, adj)) 
    
    return previous


if __name__ == "__main__":
    N, M = map(int, input().split())

    # Make the adjacent nodes list dictionary
    adjLst = defaultdict(list)
    for _ in range(M):
        i, j, w  = map(int, input().split())
        adjLst[i].append((w, j))
        adjLst[j].append((w, i))

    # Run dijkstra
    networks = dijkstra(N, adjLst)

    print(N - 1)
    for i in range(2, N + 1):
        print(i, networks[i])
