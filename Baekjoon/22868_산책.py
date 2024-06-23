import sys
from collections import deque
input = sys.stdin.readline

INF = 10001

def solution(N, M, adjLst, S, E, path):
    visited = [False] * (N + 1)

    # mark visited nodes
    for node in path:
        visited[node] = True

    # set the start
    visited[S] = True
    queue = deque([(0, S, [])])

    # dijkstra
    while queue:
        dis, cur, path = deque.popleft(queue)
    
        if cur == E:
            return dis, path

        for adj in adjLst[cur]:
            if visited[adj]:
                continue
            visited[adj] = True
            queue.append([dis + 1, adj, path + [adj]])


if __name__ == "__main__":
    N, M = map(int, input().split())

    adjLst = [[] for _ in range(N + 1)]
    for _ in range(M):
        i, j = map(int, input().split())
        adjLst[i].append(j)
        adjLst[j].append(i)

    for i in range(1, N + 1):
        adjLst[i].sort()

    S, E = map(int, input().split())
    go_dis, go_path = solution(N, M, adjLst, S, E, [])
    back_dis, _ = solution(N, M, adjLst, E, S, go_path)
    print(go_dis + back_dis)