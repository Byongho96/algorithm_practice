import sys, heapq
from typing import List

input = sys.stdin.readline


def alphabet_to_num(s: str):
    result = ord(s)

    if result < ord("a"):
        return result - ord("A") + 27
    else:
        return result - ord("a") + 1


def prim(N: int, adjLst: List[List[int]]):
    INF = N * 52
    weight = [INF] * N
    visited = [False] * N

    # set the start
    heap = [(0, 0)]
    weight[0] = 0

    cnt = 0
    while heap:
        w, cur = heapq.heappop(heap)

        # filter invalid
        if weight[cur] < w:
            continue

        # visit the node
        visited[cur] = True
        cnt += 1
        if cnt == N:
            return sum(weight)

        # traverse the adjacent nodes
        for w, adj in adjLst[cur]:
            if visited[adj] or w > weight[adj] - 1:
                continue
            weight[adj] = w
            heapq.heappush(heap, (w, adj))

    return -1


if __name__ == "__main__":
    N = int(input())
    arr = [list(input().rstrip()) for _ in range(N)]

    # make adjacent node lists
    total = 0
    adjLst = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "0":
                continue
            w = alphabet_to_num(arr[i][j])
            total += w
            adjLst[i].append((w, j))
            adjLst[j].append((w, i))

    # run prim
    required = prim(N, adjLst)

    # print the answer
    print(total - required if required > -1 else -1)
