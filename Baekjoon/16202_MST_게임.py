import sys

input = sys.stdin.readline


def find_parent(par, x):
    while par[x] != x:
        x = par[x]
    return x


def uninon_by_rank(par, rank, x, y):
    RX = rank[x]
    RY = rank[y]

    if RX < RY:
        par[x] = y
    elif RY < RX:
        par[y] = x
    else:
        par[x] = y
        rank[y] += 1


def kruskal(N, E, edges, t):
    par = [n for n in range(N + 1)]
    rank = [0] * (N + 1)

    cnt = 1
    sm = 0
    for i in range(t, E):
        w, x, y = edges[i]
        X = find_parent(par, x)
        Y = find_parent(par, y)
        if X == Y:
            continue
        uninon_by_rank(par, rank, X, Y)
        cnt += 1
        sm += w
        if cnt == N:
            return sm

    if cnt != N:
        return False


if __name__ == "__main__":
    N, M, T = map(int, input().split())

    edges = []
    for w in range(1, M + 1):
        i, j = map(int, input().split())
        edges.append((w, i, j))

    is_possible = True
    answers = []
    for t in range(T):
        if not is_possible:
            answers.append(0)
            continue

        result = kruskal(N, M, edges, t)

        if result:
            answers.append(result)
        else:
            is_possible = False
            answers.append(0)

    print(*answers)
