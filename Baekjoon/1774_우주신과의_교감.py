import math

import sys
input = sys.stdin.readline

# find the root node
def find_set(par, x):
    while x != par[x]:
        x = par[x]
    return x

# union two set by rank(size)
def union_by_rank(par, rank, x, y):
    # find the rank(size) fo the set
    rank_x, rank_y  = rank[x], rank[y]

    # union by rank
    if rank_x > rank_y:
        par[y] = x
    elif rank_y < rank_x:
        par[x] = y
    else:
        par[x] = y
        rank[y] += 1


def kruskal(N, par, rank, edges):
    # sort the edges by weight
    edges.sort(key=lambda x: x[0])

    # run kruskal
    sum_weight = 0

    for w, n1, n2 in edges:
        # find the root node
        n1, n2 = find_set(par, n1), find_set(par, n2)
        if n1 != n2:
            union_by_rank(par, rank, n1, n2)
            sum_weight += w

    return sum_weight


if __name__ == '__main__':
    N, M = map(int, input().split())

    # the variables for Kruskal
    par = [node for node in range(N + 1)]
    rank = [1] * (N + 1)

    # nodes
    nodes = [0] + [tuple(map(int, input().split())) for _ in range(N)]

    # already connected nodes
    for _ in range(M):
        n1, n2 = map(int, input().split())
        n1, n2 = find_set(par, n1), find_set(par, n2)
        if n1 != n2:
            union_by_rank(par, rank, n1, n2)

    # make edges
    edges = []
    for n1 in range(1, N + 1):
        for n2 in range(n1 + 1, N + 1):
            i1, j1 = nodes[n1]
            i2, j2 = nodes[n2]
            w = math.sqrt((i1 - i2) ** 2 + (j1 - j2) ** 2)
            edges.append((w, n1, n2))

    # run Kruskal
    answer = kruskal(N, par, rank, edges)

    print(f'{answer:.2f}')
