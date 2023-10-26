import sys
import heapq

input = sys.stdin.readline


def find(par, x):
    while par[x] != x:
        x = par[x]
    return x


def union_by_rank(rank, par, x, y):
    X, Y = find(par, x), find(par, y)

    if X == Y:
        return False

    if rank[X] < rank[Y]:
        par[X] = Y
    elif rank[X] > rank[Y]:
        par[Y] = X
    else:
        par[X] = Y
        rank[Y] += 1
    return True


if __name__ == "__main__":
    N, M = map(int, input().split())

    par = [i for i in range(N + 1)]
    rank = [0] * (N + 1)

    # connect already connected edges
    MST = 1
    for _ in range(M):
        x, y = map(int, input().split())
        if union_by_rank(rank, par, x, y):
            MST += 1
            # early end condition 1
            if MST > N - 2:
                print(0, 0)
                exit()

    # connect new edges
    edges = []
    for cur in range(1, N + 1):
        adjLst = list(map(int, input().split()))
        if cur == 1:
            continue
        # only half of the edges
        for adj in range(cur + 1, N + 1):
            heapq.heappush(edges, (adjLst[adj - 1], cur, adj))

    # kruskal
    cnt = 0
    cost = 0
    new_connected = []
    while edges:
        w, x, y = heapq.heappop(edges)
        if union_by_rank(rank, par, x, y):
            MST += 1
            cnt += 1
            cost += w
            new_connected.append((x, y))
            # early end condition 2
            if MST > N - 2:
                break

    print(cost, cnt)
    for i, j in new_connected:
        print(i, j)
