import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [0] * N
for i in range(N):
    coins[i] = int(input())

DP = [0] * (K + 1)
DP[0] = 1
for coin in coins:
    for k in range(coin, K + 1):
        DP[k] += DP[k-coin]

# print(DP)
print(DP[K])