from typing import List, Tuple
import heapq
import sys

input = sys.stdin.readline

INF = 10**9


def dijkstra(N, adjLst, start, end, disabled):
    distance = [INF] * (N + 1)

    distance[start] = 0
    heap = [(0, start)]

    while heap:
        dis, cur = heapq.heappop(heap)

        # Filter invalid condition
        if distance[cur] < dis:
            continue

        # End condition
        if cur == end:
            return dis

        # Traverse adjancent nodes
        for w, adj in adjLst[cur]:
            # Disabled node
            if disabled and adj == disabled:
                continue
            new_dis = dis + w
            if new_dis < distance[adj]:
                distance[adj] = new_dis
                heapq.heappush(heap, (new_dis, adj))
    return -1


def main(N: int, M: int, adjLst: List[Tuple[int, int]], X: int, Y: int, Z: int):
    # Pass through Y
    x_to_y = dijkstra(N, adjLst, X, Y, None)
    y_to_z = -1
    if x_to_y > 0:
        y_to_z = dijkstra(N, adjLst, Y, Z, None)

    # Don't pass through Y
    x_to_z = dijkstra(N, adjLst, X, Z, Y)

    print(-1 if y_to_z < 0 else x_to_y + y_to_z, x_to_z)


if __name__ == "__main__":
    N, M = map(int, input().split())
    adjLst = [[] for _ in range(N + 1)]

    for i in range(M):
        i, j, w = map(int, input().split())
        adjLst[i].append((w, j))

    X, Y, Z = map(int, input().split())

    main(N, M, adjLst, X, Y, Z)
