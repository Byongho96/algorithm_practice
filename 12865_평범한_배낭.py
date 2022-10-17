import sys
input = sys.stdin.readline

N, K = int(input())
weight = [0] * N
value = [0] * N
for i in range(N):
    weight[i], value[i] = map(int, input().split())

dp = [[0] * K for _ in range(N)]
# dp[n][restweight] : 1번부터 n번
dp[][]