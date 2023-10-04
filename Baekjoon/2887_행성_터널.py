import sys

input = sys.stdin.readline


# find the root
def find_set(par, x):
    while x != par[x]:
        x = par[x]
    return x


# unino set by depth
def union_by_depth(par, rank, x, y):
    r_x = rank[x]
    r_y = rank[y]

    if r_x > r_y:
        par[y] = x
    elif r_x < r_y:
        par[x] = y
    else:
        par[y] = x
        rank[x] += 1


def kruskal(N, edges):
    par = [node for node in range(N)]
    rank = [0] * N

    mst_size = 1
    sum_weight = 0
    for weight, n1, n2 in edges:
        N1 = find_set(par, n1)
        N2 = find_set(par, n2)
        if N1 == N2:
            continue

        # link the nodes
        union_by_depth(par, rank, N1, N2)
        sum_weight += weight
        mst_size += 1

        # end condition
        if mst_size == N:
            break

    return sum_weight


if __name__ == "__main__":
    N = int(input())

    # add node number when get the input
    nodes = [list(map(int, input().split())) + [n] for n in range(N)]

    # make essential edges
    edges = []
    nodes.sort(key=lambda x: x[0])
    for i in range(1, N):
        edges.append([abs(nodes[i][0] - nodes[i - 1][0]), nodes[i][3], nodes[i - 1][3]])
    nodes.sort(key=lambda x: x[1])
    for i in range(1, N):
        edges.append([abs(nodes[i][1] - nodes[i - 1][1]), nodes[i][3], nodes[i - 1][3]])
    nodes.sort(key=lambda x: x[2])
    for i in range(1, N):
        edges.append([abs(nodes[i][2] - nodes[i - 1][2]), nodes[i][3], nodes[i - 1][3]])

    # run kruskal with essential nodes
    edges.sort(key=lambda x: x[0])
    answer = kruskal(N, edges)
    print(answer)
