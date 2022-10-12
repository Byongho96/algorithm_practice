import sys
input = sys.stdin.readline

def dfs(v):
    visited = [0] * N
    visited[v] = 1

    stk = []
    while True:
        if visited[v] == 5:
            return 1
        for w in adjLst[v]:
            if not visited[w]:
                stk.append(w)
                visited[w] = visited[v] + 1
                v = w
        else:
            if stk:
                visited[v] = 0
                v = stk.pop()
            else:
                break
    return 0


N, M = map(int, input().split())
adjLst = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    adjLst[a].append(b)
    adjLst[b].append(a)

for i in range(N):
    if dfs(i):
        print(1)
        break
else:
    print(0)