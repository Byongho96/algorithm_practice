import heapq

import sys

input = sys.stdin.readline


def prim(N, univ_type, adjLst, start):
    # make initial data
    INF = 1001
    weight = [INF] * (N + 1)
    weight[0] = 0
    visited = [False] * (N + 1)
    heap = []

    # set the start apoint
    weight[start] = 0
    heap.append((0, start))

    # prim algorithm
    mst = 0
    while heap:
        w, cur = heapq.heappop(heap)

        # filter the invalid data
        if weight[cur] < w:
            continue

        # visit the node
        visited[cur] = True
        mst += 1

        # traverse the adjacent nodes
        for new_w, adj in adjLst[cur]:
            if visited[adj]:
                continue
            if univ_type[cur] == univ_type[adj]:
                continue
            if new_w < weight[adj]:
                weight[adj] = new_w
                heapq.heappush(heap, (new_w, adj))

    # reuturn the result
    if mst == N:
        return sum(weight)
    else:
        return -1


if __name__ == "__main__":
    N, M = map(int, input().split())
    univ_type = [0] + input().split()  # Add 0 at the front -> to match index

    # create adjacent node list
    adjLst = [[] for _ in range(N + 1)]
    for _ in range(M):
        i, j, w = map(int, input().split())
        adjLst[i].append((w, j))
        adjLst[j].append((w, i))

    # print answer
    answer = prim(N, univ_type, adjLst, 1)
    print(answer)
