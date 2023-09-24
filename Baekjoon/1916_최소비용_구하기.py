import heapq

import sys

input = sys.stdin.readline


def dijkstra(N, adjLst, s, e):
    """
    find the minimum distance from s to e
    """

    # make the data
    INF = N * 100000
    distance = [INF] * (N + 1)
    heap = []

    # set the start
    distance[s] = 0
    heapq.heappush(heap, (0, s))

    while heap:
        dis, cur = heapq.heappop(heap)

        # filter the invalid data
        if dis > distance[cur]:
            continue

        # end condition
        if cur == e:
            return distance[cur]

        # traverse the adjacent nodes
        for w, adj in adjLst[cur]:
            new_dis = dis + w
            if new_dis < distance[adj]:
                distance[adj] = new_dis
                heapq.heappush(heap, (new_dis, adj))


if __name__ == "__main__":
    N = int(input())
    M = int(input())

    # make adjacent node list
    adjLst = [[] for _ in range(N + 1)]
    for _ in range(M):
        i, j, w = map(int, input().split())
        adjLst[i].append((w, j))

    s, e = map(int, input().split())
    result = dijkstra(N, adjLst, s, e)
    print(result)
