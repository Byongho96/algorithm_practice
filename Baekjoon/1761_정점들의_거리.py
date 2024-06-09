import sys
import math

input = sys.stdin.readline

# lca with sparse table
def lca(depth, parent, s, e):
    if depth[s] > depth[e]:
        s, e = e, s

    # Make the depth of e the same as s
    for i in range(len(parent[0])):
        if depth[e] == depth[s]:
            break
        if (depth[e] - depth[s]) & (1 << i):
            e = parent[e][i]

    # If s and e are the same, return s
    if s == e:
        return s

    # Find the lowest common ancestor
    for i in range(len(parent[0]) - 1, -1, -1):
        if parent[s][i] != parent[e][i]:
            s = parent[s][i]
            e = parent[e][i]

    return parent[s][0]


def solution(N, adjList, targets):
    # Make tree from the root (node 1)
    depth = [0] * (N + 1)
    parent = [0] * (N + 1)
    distance = [0] * (N + 1)
    visited = [False] * (N + 1)

    logN = math.ceil(math.log2(N))
    parent = [[0] * (logN + 1) for _ in range(N + 1)]  

    stack = [(1, 0, 0)]
    while stack:
        node, par, dis = stack.pop()
        visited[node] = True
        parent[node][0] = par
        distance[node] = dis

        for nxt, w in adjList[node]:
            if not visited[nxt]:
                stack.append((nxt, node, dis + w))
                depth[nxt] = depth[node] + 1

    # Fill the sparse table (parent)
    for j in range(1, logN + 1):
        for i in range(1, N + 1):
            parent[i][j] = parent[parent[i][j-1]][j-1]

    # Get the distance with LCA
    answer = []
    for s, e in targets:
        lca_node = lca(depth, parent, s, e)
        answer.append(distance[s] + distance[e] - 2 * distance[lca_node])

    return answer


if __name__ == "__main__":
    N = int(input())

    adjList = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        i, j, w = map(int, input().split())
        adjList[i].append((j, w))
        adjList[j].append((i, w))


    M = int(input())
    targets = [tuple(map(int, input().split())) for _ in range(M)]
    
    answer = solution(N, adjList, targets)
    print(*answer, sep='\n')