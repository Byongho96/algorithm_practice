# 172 ms
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                continue
            elif arr[i][k] + arr[k][j] == 2:
                arr[i][j] = 1

for row in arr:
    print(*row)