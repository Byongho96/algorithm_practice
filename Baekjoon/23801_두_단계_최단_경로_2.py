import heapq
import sys

input = sys.stdin.readline


def dijkstra(INF, N, S, adjLst):
    dis = [INF] * (N + 1)
    heap = []

    # set start point
    dis[S] = 0
    heapq.heappush(heap, (0, S))

    # run dikjstra
    while heap:
        d, cur = heapq.heappop(heap)

        # filter invalid info
        if dis[cur] < d:
            continue

        for w, adj in adjLst[cur]:
            new_dis = w + d
            if new_dis < dis[adj]:
                dis[adj] = new_dis
                heapq.heappush(heap, (new_dis, adj))

    return dis


if __name__ == "__main__":
    # node & edge
    N, M = map(int, input().split())

    # make adjacent list
    adjLst = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        adjLst[u].append((w, v))
        adjLst[v].append((w, u))

    # start & end
    S, E = map(int, input().split())

    # stopover points
    P = int(input())
    points = list(map(int, input().split()))

    # run dijkstra two time
    INF = 2 * 1000000 * N + 1
    distance_S = dijkstra(INF, N, S, adjLst)
    distance_E = dijkstra(INF, N, E, adjLst)

    # check all the points
    answer = INF
    for p in points:
        answer = min(answer, distance_S[p] + distance_E[p])

    print(answer if answer < INF else -1)
