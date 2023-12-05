import sys, heapq

input = sys.stdin.readline

DIRECTION = ((1, 0), (0, 1), (-1, 0), (0, -1))


def bfs_shortest(N, M, arr):
    INF = N * M
    visited = (
        [[0] * (N + 2)] + [[0] + [INF] * N + [0] for _ in range(M)] + [[0] * (N + 2)]
    )

    heap = [(0, -1, -1)]
    visited[1][1] = 0

    while heap:
        w, i, j = heapq.heappop(heap)
        i = -i
        j = -j

        # filter the invalid
        if visited[i][j] < w:
            continue

        # end condition
        if i == M and j == N:
            return w

        # traverse the adjacent nodes
        for di, dj in DIRECTION:
            ni = i + di
            nj = j + dj

            # filter edges
            if arr[ni][nj] < 0:
                continue

            # valid adjacent
            new_w = arr[ni][nj] + w
            if new_w < visited[ni][nj]:
                visited[ni][nj] = new_w
                heapq.heappush(heap, (new_w, -ni, -nj))


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = (
        [[-1] * (N + 2)]
        + [[-1] + list(map(int, input().rstrip())) + [-1] for _ in range(M)]
        + [[-1] * (N + 2)]
    )

    answer = bfs_shortest(N, M, arr)
    print(answer)
