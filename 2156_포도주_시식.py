import sys
input = sys.stdin.readline

N = int(input())

juices = [0] * N
for i in range(N):
    juices[i] = int(input())

# 몇 잔 연속이라는 조건을 어떻게 처리: 경우의 수를 두어서 처리
# DP[i]의 정의: N번째까지 Open 하였을 떄
# DP[i] 를 모든 경우의 수를 고려하여 계싼하는법

# 참고한 블로그: https://yabmoons.tistory.com/m/512

if N == 1:
    print(juices[0])

elif N == 2:
    print(juices[0] + juices[1])

else:
    DP = [0] * N
    DP[0] = juices[0]
    DP[1] = juices[0] + juices[1]
    DP[2] = sum(juices[:3]) - min(juices[:3])
    for i in range(3, N):
        DP[i] = max(DP[i-1], DP[i-2] + juices[i], DP[i-3] + juices[i-1] + juices[i])

    # print(DP)
    print(DP[-1])

######################################################################

# import sys
# input = sys.stdin.readline
#
# N = int(input())
#
# juices = [0] * N
# for i in range(N):
#     juices[i] = int(input())
#
# if N == 1:
#     print(juices[0])
#
# elif N == 2:
#     print(juices[0] + juices[1])
#
# else:
#     DP = [[0] * N for _ in range(2)]
#     DP[0][0] = juices[0]
#     DP[0][1] = juices[1]
#     DP[1][1] = juices[0] + juices[1]
#
#     for i in range(2, N):
#         if juices[i-1]:
#             DP[0][i] = max(DP[0][i-2], DP[1][i-2]) + juices[i]
#             DP[1][i] = DP[0][i-1] + juices[i]
#         else:
#             DP[0][i] = max(DP[0][i-1], DP[1][i-1], DP[1][i-2])
#
#     # print(DP)
#     print(max(DP[0][-1], DP[1][-1], DP[0][-2], DP[1][-2]))