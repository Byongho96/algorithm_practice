import sys
input = sys.stdin.readline

ref = {0: (0, -1), 1: (-1, 0), 2: (0, 1), 3: (1, 0)}
def dfs(i, j):
    global size
    stk = []
    stk.append((i, j))

    size = 1
    visited[i][j] = num

    while stk:
        i, j = stk.pop()
        for d in range(4):
            if not (arr[i][j] & 1 << d):  # (서, 북, 동, 남)에 벽이 없다면
                di, dj = ref[d]
                ni, nj = i + di, j + dj
                if not visited[ni][nj]:
                    size += 1
                    visited[ni][nj] = num   # dfs stk으로 구현할 경우, 이처럼 visited를 바로 추가
                    stk.append((ni, nj))

    sizes.append(size)


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
num = 0
sizes = [0]
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            num += 1
            dfs(i, j)

print(num)
print(max(sizes))

# from pprint import pprint
# pprint(visited)
# print(sizes)

mx = 0
for i in range(N):
    for j in range(M):
        for di, dj in ((1, 0), (0, 1)):
            ni, nj = i + di, j + dj
            if ni < N and nj < M:
                group_1 = visited[i][j]
                group_2 = visited[ni][nj]
                if group_1 != group_2:
                    mx = max(mx, sizes[group_1] + sizes[group_2])
print(mx)