import sys
from collections import deque

input = sys.stdin.readline

def solution(N, R, Q, adjLst, roots):
    # make tree recording path
    visited = [False] * (N + 1)
    path = []

    queue = deque([R])
    visited[R] = True

    # bfs
    while queue:
        cur = queue.popleft()

        for adj in adjLst[cur]:
            if visited[adj]:
                continue
            visited[adj] = True
            path.append((cur, adj))
            queue.append(adj)

    # trace back counting number of sub trees
    num_sub_trees = [1] * (N + 1)
    for par, child in path[::-1]:
        num_sub_trees[par] += num_sub_trees[child]

    # get answers
    answers = [0] * Q
    for i in range(Q):
        root = roots[i]
        answers[i] = num_sub_trees[root]

    return answers

if __name__ == "__main__":
    N, R, Q = map(int, input().split())
    adjLst = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        adjLst[u].append(v)
        adjLst[v].append(u)
    roots = [int(input()) for _ in range(Q)]

    answer = solution(N, R, Q, adjLst, roots)   
    print(*answer, sep = "\n")