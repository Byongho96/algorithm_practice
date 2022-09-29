# Python 612ms, Pypy 380ms
import sys
input = sys.stdin.readline

def backtracking_black(n, cnt):
    global mx_black
    # 종료조건
    if n == B:
        mx_black = max(mx_black, cnt)
        return
    # 가지치기
    if B - n + cnt <= mx_black: # 나머지 칸에 모두 비숍을 놓아도 최댓값을 못 넘는 경우
        return
    # 후보군 출력
    i, j = black[n]
    if not B1[i - j + N] and not B2[i + j]:
        B1[i - j + N] = 1
        B2[i + j] = 1
        backtracking_black(n + 1, cnt + 1)
        B1[i - j + N] = 0
        B2[i + j] = 0
    backtracking_black(n + 1, cnt)

def backtracking_white(n, cnt):
    global mx_white
    # 종료조건
    if n == W:
        mx_white = max(mx_white, cnt)
        return
    # 가지치기
    if W - n + cnt <= mx_white: # 나머지 칸에 모두 비숍을 놓아도 최댓값을 못 넘는 경우
        return
    # 후보군 출력
    i, j = white[n]
    if not B1[i - j + N] and not B2[i + j]:
        B1[i - j + N] = 1
        B2[i + j] = 1
        backtracking_white(n + 1, cnt + 1)
        B1[i - j + N] = 0
        B2[i + j] = 0
    backtracking_white(n + 1, cnt)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

white = []          # 비숍을 놓을 수 있는 흰색 좌표를 저장할 리스트
black = []          # 비숍을 놓을 수 있는 검은색 좌표를 저장할 리스트
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            if (i + j) % 2:
                black.append((i, j))
            else:
                white.append((i, j))

B1 = [0] * (2 * N + 1)  # 대각 방향 (i - j + N) 비숍을 체크할 리스트: -(N-1) ~ (N-1)
B2 = [0] * (2 * N + 1)  # 대각 방향 (i + j) 비숍을 체크할 리스트: 0 ~ 2(N-1)

# 흰색 좌표 백트래킹
W = len(white)
mx_white = 0
backtracking_white(0, 0)

# 검은색 좌표 백트래킹
B = len(black)
mx_black = 0
backtracking_black(0, 0)

# 흰색 좌표 최대 비숍 갯수 + 검은색 좌표 최대 비숍 갯수
print(mx_white + mx_black)


# import time
# start = time.time()
# import sys
# input = sys.stdin.readline
#
# def backtracking(n, cnt):
#     # print(n, cnt)
#     global mx
#     # 종료조건
#     if n == 2 * N:
#         mx = max(mx, cnt)
#         return
#     # 가지치기
#     if 2 * N - n + cnt <= mx:
#         return
#     # 후보군 출력
#     if n < N:       # 좌측 상단
#         for i in range(n + 1):
#             for j in range(n, -1, -1):
#                 if arr[i][j] and not B1[i - j + N - 1] and not B2[i + j]:
#                     B1[i - j + N - 1] = 1
#                     B2[i + j] = 1
#                     backtracking(n + 1, cnt + 1)
#                     B1[i - j + N - 1] = 0
#                     B2[i + j] = 0
#         backtracking(n + 1, cnt)
#
#     else:           # 우측 하단
#         for i in range(n - N + 1, N):
#             for j in range(N - 1, n - N, -1):
#                 if arr[i][j] and not B1[i - j + N - 1] and not B2[i + j]:
#                     B1[i - j + N - 1] = 1
#                     B2[i + j] = 1
#                     backtracking(n + 1, cnt + 1)
#                     B1[i - j + N - 1] = 0
#                     B2[i + j] = 0
#         backtracking(n + 1, cnt)
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# mx = 0
# B1 = [0] * (2 * N - 1)
# B2 = [0] * (2 * N - 1)
# backtracking(0, 0)
# print(mx)
# print("time: ", time.time()-start)
#
