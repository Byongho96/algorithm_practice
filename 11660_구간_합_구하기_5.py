from pprint import pprint
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

DP = [[0] * (N + 1) for _ in range(N + 1)]
DP[1][1] = arr[1][1]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + arr[i][j]

# for sm in range(3, 2 * N + 1):
#     if sm <= N + 1:
#         si, sj = 1, sm-1
#     else:
#         si, sj = sm - N, N
#     for mv in range(N - abs(sm - 1 - N)):
#         ci, cj = si + mv, sj - mv
#         DP[ci][cj] = DP[ci-1][cj] + DP[ci][cj-1] - DP[ci-1][cj-1] + arr[ci][cj]
pprint(DP)
for _ in range(M):
    i1, j1, i2, j2 = map(int, input().split())
    print(DP[i2][j2] + DP[i1-1][j1-1] - DP[i2][j1-1] - DP[i1-1][j2])

