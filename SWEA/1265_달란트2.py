import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

T = int(input())

for t in range(1, T+1):

    N, P = map(int, input().split())
    divide = [0] * N
    ave = N // P
    res = N % P

    mx = (ave ** (P - res)) * ((ave + 1) ** res)

    print(f'#{t} {mx}')

#############################################################################

# def dfs_recursive(n, cnt):
#     global mx
#     if cnt == P - 1:
#         mul = 1
#         i_pre = 0
#         for i in range(N):
#             if divide[i] == 1:
#                 mul *= (i - i_pre)
#                 i_pre = i
#         mul *= (N - i_pre)
#         if mx < mul:
#             mx = mul
#         return
#     elif n == N:
#         return
#     else:
#         divide[n] = 1
#         dfs_recursive(n + 1, cnt + 1)
#         divide[n] = 0
#         dfs_recursive(n + 1, cnt)
#         return
#
#
# T = int(input())
#
# for t in range(1, T+1):
#
#     N, P = map(int, input().split())
#     divide = [0] * N
#     mx = 0
#     dfs_recursive(1, 0)
#
#     print(f'#{t} {mx}')