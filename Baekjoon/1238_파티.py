import heapq

import sys
input=sys.stdin.readline


def dijkstra(N, adjLst, start, is_return=False):
    INF = 100 * N
    heap = []
    distance = [INF] * (N + 1)
    
    # set the start
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        dis, cur = heapq.heappop(heap)

        # filter the invalid data
        if distance[cur] < dis:
            continue

        # early end condition
        if is_return and cur == X:
            return distance

        for w, adj in adjLst[cur]:
            new_dis = dis + w
            if new_dis < distance[adj]:
                distance[adj] = new_dis
                heapq.heappush(heap, (new_dis, adj))

    return distance


if __name__ == '__main__':
    N, M, X = map(int, input().split())

    # make adjacent node list
    adjLst = [[] for _ in range(N +1)]
    for _ in range(M):
        i, j, w = map(int, input().split())
        adjLst[i].append((w, j))

    # get the returning distance
    return_distance = dijkstra(N, adjLst, X)

    # calculate the total distance for all the child
    max_dis = 0
    for n in range(1, N + 1):
        if n == X:
            continue
        dis = dijkstra(N, adjLst, n, True)[X] + return_distance[n]
        if dis > max_dis:
            max_dis = dis

    print(max_dis)
