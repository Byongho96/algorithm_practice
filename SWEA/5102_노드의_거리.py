import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

def bfs(S, G):
    visited = [0] * (V + 1)
    q = []

    q.append(S)
    visited[S] = 1

    while q:
        v = q.pop(0)
        if v == G:
            return visited[v] - 1
        for w in adjLst[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1
    return 0

T = int(input())
for t in range(1, T+1):

    V, E = map(int, input().split())

    adjLst = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adjLst[a].append(b)
        adjLst[b].append(a)

    S, G = map(int, input().split())

    result = bfs(S, G)

    print(f'#{t} {result}')