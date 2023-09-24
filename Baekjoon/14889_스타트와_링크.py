# 2nd
import sys

input = sys.stdin.readline


def comb_backtracking(n, idx):
    global mn
    if n == N // 2:
        p1, p2 = 0, 0
        for i in range(N):
            for j in range(N):
                if i in t1 and j in t1:  # in을 쓸꺼면 집합으로, 더 좋은건 리스트 인덱스로
                    p1 += arr[i][j]
                elif not (i in t1 or j in t1):
                    p2 += arr[i][j]
        mn = min(mn, abs(p1 - p2))
        return
    if N - idx + n < N // 2 or not mn:
        return
    t1.add(idx)
    comb_backtracking(n + 1, idx + 1)
    t1.remove(idx)
    comb_backtracking(n, idx + 1)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

mn = 100 * 20 * 20
t1 = []
comb_backtracking(0, 0)
print(mn)

#######################################################################################################################

import sys

input = sys.stdin.readline


def comb_backtracking(n, idx):
    global mn
    if n == N // 2:
        p1, p2 = 0, 0
        for i in range(N):
            for j in range(i + 1, N):
                if t1[i] and t1[j]:  # 리스트 인덱스 후 반만 탐색!
                    p1 += arr[i][j] + arr[j][i]
                elif not (t1[i] or t1[j]):
                    p2 += arr[i][j] + arr[j][i]
        mn = min(mn, abs(p1 - p2))
        return
    if N - idx + n < N // 2 or not mn:
        return
    t1[idx] = 1
    comb_backtracking(n + 1, idx + 1)
    t1[idx] = 0
    comb_backtracking(n, idx + 1)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

mn = 100 * 20 * 20
t1 = [0] * N
comb_backtracking(0, 0)
print(mn)

#######################################################################################################################
# 으아아아아 대단쓰!!!!
import sys

input = sys.stdin.readline


def DFS(L, s, a):
    global res
    if L == N // 2:
        res = min(res, abs(s))
        return
    for i in range(a, N):
        DFS(L + 1, s - row[i] - col[i], i + 1)


N = int(input())
gra = [list(map(int, input().split())) for _ in range(N)]
row = [0] * N
col = [0] * N

tot = 0
for i in range(N):
    for j in range(N):
        row[i] += gra[i][j]
        col[j] += gra[i][j]
        tot += gra[i][j]
res = 2147000000
DFS(1, tot - row[0] - col[0], 1)
print(res)
#######################################################################################################################
#######################################################################################################################
# ## PyPy3 11512ms
# import sys
# input = sys.stdin.readline
#
# def dfs_while(n, cnt):
#     global mn
#     # 종료조건
#     if cnt == N // 2:           # 팀이 형성되었을 때
#         # print(start)
#         st_p, li_p = 0, 0
#         for i in range(1, N+1):
#             for j in range(1, N+1):
#                 if start[i] and start[j]:
#                     st_p += table[i][j]
#                 elif not start[i] and not start[j]:
#                     li_p += table[i][j]
#         mn = min(mn, abs(st_p-li_p))
#         # if abs(st_p-li_p) == 0:
#         #     print(start, cnt)
#         return
#     # 가지치기
#     # elif not mn:
#     #     return
#     # elif n == N+1:
#     #     return
#     elif cnt + N - n + 1 < N//2:    # 현재부터 모든 사람을 골라도 팀이 안 만들어질 때, 종료조건 포함 n == N+1
#         return
#     # 후보군 출력
#     else:                           # 나중에 start를 이용해서 계산해야 하는데 , return 할때 0으로 초기화가 안되면, 중간에 cnt를 채워 계산할 때 오류!!
#         # print(n)
#         dfs_while(n + 1, cnt)
#         start[n] = 1
#         dfs_while(n + 1, cnt + 1)
#         start[n] = 0                # 중요!!!!!!!!!!!!
#         return
#
#         ## 아래와 같은 식으로 후보군 출력도 가능, 단 dfs_while()인자와 관련하여 조금씩 수정해야 함
#         # for start in range(N + 1):
#         #     if start[n] == 1:
#         #         continue
#         #     start[n] = True
#         #     dfs_while(cnt + 1)
#         #     start[n] = 0
#         # return
#
# N = int(input())
# table = [[0] * (N+1)] + [[0] + list(map(int, input().rstrip().split())) for _ in range(N)]
#
# mn = 99 * 20
# start = [0] * (N +1)
# dfs_while(1, 0)
# print(mn)
