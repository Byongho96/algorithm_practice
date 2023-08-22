import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())

    # make DP
    DP = [[0] * 3 for _ in range(N)]

    # set the initial data
    DP[0] = list(map(int, input().split()))

    # fill DP
    for i in range(1, N):
        R, G, B = map(int, input().split())
        DP[i][0] = min(DP[i-1][1], DP[i-1][2]) + R
        DP[i][1] = min(DP[i-1][0], DP[i-1][2]) + G
        DP[i][2] = min(DP[i-1][0], DP[i-1][1]) + B

    print(min(DP[-1]))