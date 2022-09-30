import sys
input = sys.stdin.readline

# 경로압축??
def find_set(x):
    while x != par[x]:
        x = par[x]
        par[x] = par[par[x]]
    return x

# union by rank
def union(x, y):
    X = find_set(x)
    Y = find_set(y)
    if rank[X] == rank[Y]:
        par[Y] = X
        rank[X] += 1
    elif rank[X] < rank[Y]:
        par[X] = Y
    else:
        par[Y] = X

N, M = map(int, input().split())
par = [i for i in range(N + 1)]
rank = [1] * (N + 1)
answer = []
for _ in range(M):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a, b)
    elif find_set(a) == find_set(b):
        answer.append('YES')
    else:
        answer.append('NO')
print(*answer, sep='\n')