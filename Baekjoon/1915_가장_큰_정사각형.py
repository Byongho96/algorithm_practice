import sys
input = sys.stdin.readline

import pprint
def solution(N, M, arr):
    mx = 0

    # make and init DP
    DP = [[0] * M for _ in range(N)]

    for i in range(N):
        DP[i][0] = arr[i][0]
        mx = max(mx, DP[i][0])

    for j in range(M):
        DP[0][j] = arr[0][j]
        mx = max(mx, DP[0][j])

    # fill the DP
    for i in range(1, N):
        for j in range(1, M):
            if not arr[i][j]:
                continue
            DP[i][j] = min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1]) + 1
            mx = max(mx, DP[i][j])

    return mx ** 2

if __name__ =="__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().rstrip())) for _ in range(N)]

    answer = solution(N, M, arr)
    print(answer)