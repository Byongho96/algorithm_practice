import sys
input = sys.stdin.readline

N = int(input())
stones = list(map(int, input().split()))

# # [1]. 이분탐색 & DP. Pypy3 2448ms
# start = 0
# end = 5000 * 1000000
# while start <= end:
#     middle = (start + end) // 2
#     K = middle
#     DP = [1] + [0] * (N - 1)
#     for j in range(1, N):
#         for i in range(max(0, j - K), j):
#             if DP[i] and (j - i) * (1 + abs(stones[j] - stones[i])) <= K:
#                 DP[j] = 1
#                 break
#     if DP[-1]:
#         end = middle - 1
#     else:
#         start = middle + 1
#
# print(start)

# [2]. DP Pypy3 236ms
MAX = 5000 * 1000000
DP = [0] + [MAX] * (N - 1)
for j in range(1, N):
    for i in range(j):
        power = max(DP[i], (j - i) * (1 + abs(stones[j] - stones[i])))
        DP[j] = min(DP[j], power)

print(DP[-1])