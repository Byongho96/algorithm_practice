import heapq
from collections import deque

import sys

input = sys.stdin.readline

DIRECTION = ((0, 1), (1, 0), (0, -1), (-1, 0))


def find_the_distance_with_bfs_max_heap(N, M, dis, start, end):
    si, sj = start
    ei, ej = end
    visited = [[True] * (M + 2)] + [[True] + [False] * (M) + [True] for _ in range(N)] + [[True] * (M + 2)]
    heap = []

    # set the start
    visited[si][sj] = True
    heap.append((-dis[si][sj], si, sj))

    # bfs with heap
    mn = dis[si][sj]
    while heap:
        d, i, j = heapq.heappop(heap)

        # update the answer (visit the node)
        mn = min(mn, -d)

        # end condition
        if i == ei and j == ej:
            return mn

        # traverse the nodes
        for d_index in range(4):
            di, dj = DIRECTION[d_index]
            ni, nj = i + di, j + dj
            if visited[ni][nj]:
                continue
            visited[ni][nj] = True
            heapq.heappush(heap, (-dis[ni][nj], ni, nj))


# calcuate the distance from trees with bfs
def calculate_dis_with_bfs(dis, trees):
    queue = deque()

    # set the trees distance as 0
    for i, j in trees:
        dis[i][j] = 0
        queue.append((0, i, j))

    # bfs
    while queue:
        d, i, j = queue.popleft()
        for d_index in range(4):
            di, dj = DIRECTION[d_index]
            ni, nj = i + di, j + dj
            if dis[ni][nj] != INF:
                continue
            dis[ni][nj] = d + 1
            queue.append((d + 1, ni, nj))


if __name__ == "__main__":
    N, M = map(int, input().split())
    INF = N + M + 1

    arr = [[0] * (M + 2)] + [[0] + list(input()) + [0] for _ in range(N)] + [[0] * (M + 2)]
    dis = [[0] * (M + 2)] + [[0] + [INF] * M + [0] for _ in range(N)] + [[0] * (M + 2)]

    # find the trees & start & end
    trees = []
    start = None
    end = None
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if arr[i][j] == ".":
                continue
            elif arr[i][j] == "+":
                trees.append((i, j))
            elif arr[i][j] == "V":
                start = (i, j)
            else:
                end = (i, j)

    calculate_dis_with_bfs(dis, trees)
    answer = find_the_distance_with_bfs_max_heap(N, M, dis, start, end)

    print(answer)
