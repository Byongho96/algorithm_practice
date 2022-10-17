import sys
input = sys.stdin.readline

# 참조 블로그: https://hongcoding.tistory.com/m/50
C, N = map(int, input().split())

price = [0] * (N + 1)
customer = [0] * (N + 1)
for i in range(1, N + 1):
    price[i], customer[i] = map(int, input().split())

DP = [[0] * (C + 1) for _ in range(N+1)]

for i in range(1, N + 1):
    for j in range(1, C + 1):
        if
