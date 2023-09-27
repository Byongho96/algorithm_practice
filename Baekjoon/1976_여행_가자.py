def find_parent(par, x):
    while par[x] != x:
        x = par[x]
    return x


def union_by_rank(par, rank, x, y):
    rx = rank[x]
    ry = rank[y]

    if rx > ry:
        par[y] = x
    elif rx < ry:
        par[x] = y
    else:
        par[y] = x
        rank[x] += 1


if __name__ == "__main__":
    N = int(input())
    M = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    travels = list(map(int, input().split()))

    # union the linked nodes
    par = [n for n in range(N)]
    rank = [0] * N
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                X = find_parent(par, i)
                Y = find_parent(par, j)
                if X != Y:
                    union_by_rank(par, rank, X, Y)

    # check the travel nodes are in the same set
    answer = "YES"
    for i in range(1, M):
        if find_parent(par, travels[i - 1] - 1) != find_parent(par, travels[i] - 1):
            answer = "NO"
            break

    print(answer)
