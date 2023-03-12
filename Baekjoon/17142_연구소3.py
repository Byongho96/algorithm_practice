from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

# 1. 빈공간에 전염되었을 경우에만, time update
# 2. 전염때마다 count해서 arr의 빈공간의 갯수와 비교

def bfs(viruses):
    global mn
    arr2 = [item[:] for item in arr]
    q = deque()

    for i, j in viruses:
        arr2[i][j] = 1
        q.append((i, j))

    time = 1
    while q:
        i, j = q.popleft()

        for di, dj in ((1, 0), (0, -1), (0, 1), (-1, 0), ):
            ni = i + di
            nj = j + dj
            if arr2[ni][nj] == '2':
                q.append((ni, nj))
                arr2[ni][nj] = arr2[i][j] + 1
            elif arr2[ni][nj] == '0':
                q.append((ni, nj))
                arr2[ni][nj] = arr2[i][j] + 1
                time = arr2[ni][nj]

    for row in arr2:
        if '0' in row:
            break
    else:
        return time-1

    return N**2

# def bfs(viruses_chosen):
#     global mn
#     arr2 = [item[:] for item in arr]
#     q = deque()
#
#     for idx in range(len(viruses_chosen)):
#         if viruses_chosen[idx]:
#             i, j = viruses[idx]
#             arr2[i][j] = 1
#             q.append((i, j))
#
#     time_pre = 0
#     while q:
#         i, j = q.popleft()
#         # visit(v))
#         time = arr2[i][j]
#         if time > time_pre:
#             if time > mn:
#                 return N**2
#             for row in arr2:
#                 if '0' in row:
#                     break
#             else:
#                 return time - 1
#             time_pre = time
#
#         for di, dj in ((1, 0), (0, -1), (0, 1), (-1, 0), ):
#             ni = i + di
#             nj = j + dj
#             if arr2[ni][nj] == '0' or arr2[ni][nj] == '2':
#                 q.append((ni, nj))
#                 arr2[ni][nj] = arr2[i][j] + 1
#
#     return N**2

# def comb_backtracking(n, idx):
#     global mn
#     # 종료조건
#     if n == M:
#         result = bfs(visited)
#         mn = min(mn, result)
#     # 후보군 출력
#     else:
#         for i in range(idx + 1, V):
#             visited[i] = 1
#             comb_backtracking(n+1, i)
#             visited[i] = 0

N, M = map(int, input().split())
arr = [['1'] * (N + 2)] + [['1'] + input().rstrip().split() + ['1'] for _ in range(N)] + [['1'] * (N + 2)]

viruses = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if arr[i][j] == '2':
            viruses.append((i, j))

mn = N**2
V = len(viruses)
visited = [0] * V
# comb_backtracking(0, -1)

for comb in combinations(viruses, M):
    result = bfs(comb)
    mn = min(mn, result)

if mn == N**2:
    print(-1)
else:
    print(mn)