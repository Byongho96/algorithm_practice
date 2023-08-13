from collections import defaultdict
import heapq

import sys
input = sys.stdin.readline

def prim(N, adjLst, mode='min'):
    # Set the factor according the mode
    factor = 1  # Min Heap  
    if mode=='max':
        factor = -1 # Max Heap

    INF = N + 1
    weight = [INF] * (N + 1)
    visited = [False] * (N + 1)
    cnt = 0
    heap = []

    # Set the start point
    weight[0] = 0
    heapq.heappush(heap, (0, 0))

    while heap:
        w, cur = heapq.heappop(heap)

        # Ignore the invalid data
        if weight[cur] < w:
            continue

        # Confirm the visit
        visited[cur] = True
        cnt += 1
        if cnt == N + 1:
            return sum(weight)

        for w, adj in adjLst[cur]:
            w = factor * w  # Multiply the factor
            if not visited[adj] and w < weight[adj]:
                weight[adj] = w
                heapq.heappush(heap, (w, adj))

    return sum(weight)


if __name__ == "__main__":
    N, M = map(int, input().split())

    # Make adjacent nodes list dictionary
    adjLst = defaultdict(list)
    for _ in range(M + 1):
        i, j, w = map(int, input().split())
        w = 1 - w   # Adjust the weight: To the uphill road have the positive weight
        adjLst[i].append((w, j))
        adjLst[j].append((w, i))

    mn = prim(N, adjLst)
    mx = prim(N, adjLst, 'max')

    print(mx**2 - mn**2)