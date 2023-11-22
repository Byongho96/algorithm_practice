import sys
import heapq

input = sys.stdin.readline


# Dijkstra with heap
def dijkstra(INF, N, adjLst, start):
    weight = ["INF"] * (N + 1)

    # set the start
    weight[start] = 0
    heap = [(0, start)]

    while heap:
        w, cur = heapq.heappop(heap)

        # filter the invalid
        if w > weight[cur]:
            continue

        # traverse the adjacents
        for adj_w, adj in adjLst[cur]:
            new_w = w + adj_w
            if weight[adj] == "INF" or new_w < weight[adj]:
                weight[adj] = new_w
                heapq.heappush(heap, (new_w, adj))

    return weight


if __name__ == "__main__":
    V, E = map(int, input().split())
    K = int(input())
    INF = 10 * V

    adjLst = [[] for _ in range((V + 1))]
    for _ in range(E):
        i, j, w = map(int, input().split())
        adjLst[i].append((w, j))

    print(*dijkstra(INF, V, adjLst, K)[1:], sep="\n")
