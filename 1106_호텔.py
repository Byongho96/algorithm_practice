import sys
input = sys.stdin.readline

# 참조 블로그: https://hongcoding.tistory.com/m/50

# C, N = map(int, input().split())    # C: 목표인원, N: 도시갯수
# price = [0] * (N + 1)
# customer = [0] * (N + 1)
# for i in range(1, N + 1):
#     price[i], customer[i] = map(int, input().split())

# # [1]. 2차원 DP [30840KB, 7000ms]
# MAX = 100001
# DP = [[0] + [MAX] * C for _ in range(N + 1)]    # DP 배열로 초깃값 주의
# for cur_city in range(1, N + 1):
#     for target_num in range(1, C + 1):
#         m = 0
#         while True:
#             invited = customer[cur_city] * m
#             cost = price[cur_city] * m
#             if target_num >= invited:
#                 DP[cur_city][target_num] = min(DP[cur_city][target_num], DP[cur_city - 1][target_num - invited] + cost)
#             else:
#                 DP[cur_city][target_num] = min(DP[cur_city][target_num], cost)
#                 break
#             m += 1
#
# print(DP[-1][-1])

# # [2]. 1차원 DP [30840KB, 6004ms]
# MAX = 100001
# DP = [0] + [MAX] * C    # DP 배열로 초깃값 주의
# for cur_city in range(1, N + 1):
#     for target_num in range(C, 0, -1):
#         m = 0
#         while True:
#             invited = customer[cur_city] * m
#             cost = price[cur_city] * m
#             if target_num >= invited:
#                 DP[target_num] = min(DP[target_num], DP[target_num - invited] + cost)
#             else:
#                 DP[target_num] = min(DP[target_num], cost)
#                 break
#             m += 1
#
# print(DP[-1])

#################################################################################################
# [3]. 메모이제이션 [30840KB, 6132ms]
def memoization(i, j):
    if j <= 0:
        return 0
    if i == 0:
        return MAX
    if DP[i][j] != MAX:
        return DP[i][j]
    m = 0
    while True:
        cost = p_c[i][0] * m
        invited = p_c[i][1] * m
        if j >= invited:
            DP[i][j] = min(DP[i][j], memoization(i-1, j - invited) + cost)
        else:
            DP[i][j] = min(DP[i][j], cost)
            break
        m += 1
    if DP[i][j] == MAX:
        DP[i][j] += 1
    return DP[i][j]

C, N = map(int, input().split())    # C: 목표인원, N: 도시갯수
p_c = [[] for _ in range(N + 1)]
p_c[0] = [0, 101]
for i in range(1, N + 1):
    p_c[i] = list(map(int, input().split()))

p_c.sort(key=lambda x: x[1], reverse=True)  # 생각보다 별 효과 없음
MAX = 100001
DP = [[MAX] * (C + 1) for _ in range(N + 1)]

print(memoization(N, C))

