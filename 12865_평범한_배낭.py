import sys
input = sys.stdin.readline

N, K = map(int, input().split())
weight = [0] * (N + 1)  # DP배열의 행과 인덱스를 맞추기 위해서
value = [0] * (N + 1)   # DP배열의 행과 인덱스를 맞추기 위해서
for i in range(1, N + 1):
    weight[i], value[i] = map(int, input().split())

# # [1]. 2차원 DP [228MB, 6956ms]
# DP = [[0] * (K + 1) for _ in range(N + 1)]
# for cur_object in range(1, N + 1):
#     for limit in range(1, K + 1):
#         if limit >= weight[cur_object]:
#             DP[cur_object][limit] = max(DP[cur_object-1][limit], DP[cur_object-1][limit-weight[cur_object]] + value[cur_object])
#         else:
#             DP[cur_object][limit] = DP[cur_object - 1][limit]
# print(DP[-1][-1])

# # [2]. 1차원 DP [34MB, 5140ms]
# DP = [0] * (K + 1)
# for cur_object in range(1, N + 1):
#     for limit in range(K, 0, -1):   # 그래야지 DP[cur_object-1][]값을 유효하게 참조할 수 있다.
#         if limit >= weight[cur_object]:
#             DP[limit] = max(DP[limit], DP[limit-weight[cur_object]] + value[cur_object])
# print(DP[-1])

# # [3]. 메모이제이션 [139MB, 3048ms]
# # memoization 할 필요가 없음. 상태공간이 겹칠 확률이 매우 적기는 하다.
# def memoization(i, j):
#     if i <= 0 or j <= 0:
#         return 0
#     if DP[i][j]:
#         return DP[i][j]
#     if j >= weight[i]:
#         DP[i][j] = max(memoization(i-1, j), memoization(i-1, j-weight[i]) + value[i])
#     else:
#         DP[i][j] = memoization(i-1, j)
#     return DP[i][j]
#
# DP = [[0] * (K + 1) for _ in range(N + 1)]
# print(memoization(N, K))

# [4]. 메모이제이션 없는 재귀호출 [시간초과]
def recursive(i, j):
    if i <= 0 or j <= 0:
        return 0
    if j >= weight[i]:
        return max(recursive(i-1, j), recursive(i-1, j-weight[i]) + value[i])
    else:
        return recursive(i-1, j)

print(recursive(N, K))
