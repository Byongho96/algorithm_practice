import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp= [[0] * N for _ in range(N)]
dp[0][0] = 1
for n in range(2 * N - 2):              # 좌하향하는 대각선 탐색 코드: 여기부터 ~
    if n < N:                           # 그냥 내 생각대로 맘대로 짰다
        i = 0
        j = n
    else:
        i = n - N + 1
        j = N - 1
    for m in range(N - abs(n + 1 - N)):
        ci, cj = i + m, j - m               # ~ 여기까지
        jump = arr[ci][cj]                  # 현재위치 (ci, cj)에서의 점프 값
        path = dp[ci][cj]                   # 현재위치 DP값(시작지점부터 현재위치까지의 경로 수) 읽어오기
        if ci + jump < N:
            dp[ci + jump][cj] += path           # 아래쪽 점프위치 DP 업데이트
        if cj + jump < N:
            dp[ci][cj + jump] += path           # 오른쪽 점프위치 DP 업데이트
print(dp[-1][-1])

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def memoization(i, j):
    if i > N - 1 or j > N - 1:
        return 0
    if memo[i][j]:
        return memo[i][j]

    jump = arr[i][j]
    memo[i][j] = memoization(i + jump, j) + memoization(i, j + jump)
    return memo[i][j]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

memo = [[0] * N for _ in range(N)]
memo[-1][-1] = 1
print(memoization(0, 0))


import sys
input = sys.stdin.readline

def backtracking(i, j):
    global path
    # 가지치기
    if i >= N or j >= N:
        return

    # 종료조건
    if i == N - 1 and j == N - 1:
        path += 1
        return

    # 후보군 출력
    jump = arr[i][j]
    backtracking(i + jump, j)
    backtracking(i, j + jump)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

path = 0
backtracking(0, 0)
print(path)