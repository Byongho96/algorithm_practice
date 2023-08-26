import sys
sys.stdin.readline

# find the the farthest node from the start using DFS
def find_the_farthest(N, adjLst, start):
    visited = [0] * (N + 1)
    stack = []

    # set the start
    stack.append((1, start))

    # dfs
    max_node = 1
    max_dis = 0
    while stack:
        dis, cur = stack.pop()

        # visit the node
        visited[cur] = dis

        # update the max
        if dis > max_dis:
            max_dis = dis
            max_node = cur

        # traverse the adjacnet nodes
        for w, adj in adjLst[cur]:
            if visited[adj]:
                continue
            new_dis = dis + w
            stack.append((new_dis, adj))
        
    # return the result
    return max_node, max_dis - 1

if __name__ == '__main__':
    V = int(input())

    # make adjacent node lists from the input
    adjLst = [[] for _ in range(V + 1)]
    for _ in range(V):
        edge = list(map(int, input().split()))
        node = edge[0]
        E = len(edge)
        for i in range(1, E - 1, 2):
            adj, w = edge[i], edge[i + 1]
            adjLst[node].append((w, adj))

    # calculate the distance by runngind dfs 2 time
    one, _ = find_the_farthest(V, adjLst, 1)
    the_other, distance = find_the_farthest(V, adjLst, one)

    print(distance)