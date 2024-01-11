import sys

input = sys.stdin.readline

DIRECTION = ((1, 0), (0, 1), (-1, 0), (0, -1))


def numbering_islands(N, M, arr):
    is_numbered = [[False] * (M + 2) for _ in range(N + 2)]
    island_num = 0

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            # filter invalid conditon
            if not arr[i][j] or is_numbered[i][j]:
                continue
            # if find an unnumbered island
            island_num += 1
            arr[i][j] = island_num
            is_numbered[i][j] = True
            # bfs
            stack = [(i, j)]
            while stack:
                ci, cj = stack.pop()
                for d in range(4):
                    di, dj = DIRECTION[d]
                    ni = ci + di
                    nj = cj + dj
                    if arr[ni][nj] and not is_numbered[ni][nj]:
                        stack.append((ni, nj))
                        arr[ni][nj] = island_num
                        is_numbered[ni][nj] = True

    return island_num


def find_edges(N, M, arr):
    edges = []
    bridges = [[0] * (M + 2) for _ in range(N + 2)]
    for i in range(1, N + 1):
        distance = 0
        for j in range(1, M + 1):
            if not arr[i][j]:
                bridges[i][j] = bridges[i][j - 1]
                distance += 1
            else:
                bridges[i][j] = arr[i][j]
                if distance > 1 and bridges[i][j - 1]:
                    edges.append((distance, bridges[i][j], bridges[i][j - 1]))
                distance = 0

    for j in range(1, M + 1):
        distance = 0
        for i in range(1, N + 1):
            if not arr[i][j]:
                bridges[i][j] = bridges[i - 1][j]
                distance += 1
            else:
                bridges[i][j] = arr[i][j]
                if distance > 1 and bridges[i - 1][j]:
                    edges.append((distance, bridges[i][j], bridges[i - 1][j]))
                distance = 0

    return edges


def find_set(par, x):
    while x != par[x]:
        x = par[x]
    return x


def union_by_rank(par, rank, x, y):
    if rank[x] == rank[y]:
        par[y] = x
        rank[x] += 1
    elif rank[x] > rank[y]:
        par[y] = x
    else:
        par[x] = y


def kruskal(N, edges):
    par = [i for i in range(N + 1)]
    rank = [1] * (N + 1)

    edges.sort()

    sum_weight = 0
    mst = 1
    for weight, x, y in edges:
        X, Y = find_set(par, x), find_set(par, y)
        if X == Y:
            continue
        union_by_rank(par, rank, X, Y)
        sum_weight += weight
        mst += 1
        if mst == N:
            return sum_weight

    return -1


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = (
        [[0] * (M + 2)]
        + [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
        + [[0] * (M + 2)]
    )

    max_num = numbering_islands(N, M, arr)
    edges = find_edges(N, M, arr)
    answer = kruskal(max_num, edges)

    print(answer)
