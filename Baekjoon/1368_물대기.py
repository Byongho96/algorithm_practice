import sys
import heapq

input = sys.stdin.readline


def prim2(N, dig_cost, adjLst):
    weight = [100001] * N
    visited = [False] * N
    heap = []

    for i in range(N):
        heapq.heappush(heap, (dig_cost[i], i))

    # run prim
    while heap:
        w, cur = heapq.heappop(heap)

        # filter invalid info
        if weight[cur] < w:
            continue

        # visit node
        visited[cur] = True
        weight[cur] = w

        # traverse adjacent nodes
        for adj in range(N):
            w = adjLst[cur][adj]
            if not visited[adj] and w < weight[adj]:
                weight[adj] = w
                heapq.heappush(heap, (w, adj))

    return sum(weight)


if __name__ == "__main__":
    N = int(input())
    dig_cost = [int(input()) for _ in range(N)]
    adjLst = [list(map(int, input().split())) for _ in range(N)]

    answer = prim2(N, dig_cost, adjLst)
    print(answer)
