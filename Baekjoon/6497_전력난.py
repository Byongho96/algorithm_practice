import sys
import heapq

input = sys.stdin.readline


def prim(N, adjLst):
    INF = 2**31
    weight = [INF] * N
    visited = 0

    heap = [(0, 0)]
    weight[0] = 0

    cnt = 0
    while heap:
        w, cur = heapq.heappop(heap)

        if weight[cur] < w:
            continue

        visited |= 1 << cur
        cnt += 1
        if cnt == N:
            return sum(weight)

        for adj_w, adj in adjLst[cur]:
            if visited >> adj & 1 or adj_w > weight[adj] - 1:
                continue
            weight[adj] = adj_w
            heapq.heappush(heap, (adj_w, adj))

    return False


if __name__ == "__main__":
    while True:
        N, M = map(int, input().split())

        if not N:
            break

        TOTAL = 0
        adjLst = [[] for _ in range(N)]
        for _ in range(M):
            i, j, w = map(int, input().split())
            adjLst[i].append((w, j))
            adjLst[j].append((w, i))
            TOTAL += w

        print(TOTAL - prim(N, adjLst))
