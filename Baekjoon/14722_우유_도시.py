import sys
input = sys.stdin.readline

def solution(N, arr) -> int:
    dp = [[0, 0, 0] for _ in range(N)]  # [딸기, 바나나, 초코]

    # first row
    dp[0][0] = 1 if arr[0][0] == 0 else 0
    for j in range(1, N):
        dp[j][0] = dp[j-1][2] + 1 if arr[0][j] == 0 else dp[j-1][0]
        dp[j][1] = dp[j-1][0] + 1 if arr[0][j] == 1 and dp[j-1][0] else dp[j-1][1]
        dp[j][2] = dp[j-1][1] + 1 if arr[0][j] == 2 and dp[j-1][1] else dp[j-1][2]

    # fil DP
    for i in range(1, N):
        for j in range(N):
            if not j:
                dp[j][0] = dp[j][2] + 1 if arr[i][j] == 0 else dp[j][0]
                dp[j][1] = dp[j][0] + 1 if arr[i][j] == 1 and dp[j][0] else dp[j][1]
                dp[j][2] = dp[j][1] + 1 if arr[i][j] == 2 and dp[j][1] else dp[j][2]
            else:
                dp[j][0] = max(dp[j][2] + 1 if arr[i][j] == 0 else dp[j][0], dp[j-1][2] + 1 if arr[i][j] == 0 else dp[j-1][0])
                dp[j][1] = max(dp[j][0] + 1 if arr[i][j] == 1 and dp[j][0] else dp[j][1], dp[j-1][0] + 1 if arr[i][j] == 1 and dp[j-1][0] else dp[j-1][1])
                dp[j][2] = max(dp[j][1] + 1 if arr[i][j] == 2 and dp[j][1] else dp[j][2], dp[j-1][1] + 1 if arr[i][j] == 2 and dp[j-1][1] else dp[j-1][2])

    return max(dp[-1])

if __name__ =="__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, arr))