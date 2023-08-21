if __name__ == '__main__':
    N = int(input())
    RGB = tuple(tuple(map(int, input().split())) for _ in range(N))

    # make DP
    DP = [[0] * 3 for _ in range(N)]

    # set the initial data
    DP[0] = RGB[0]

    # fill DP
    for i in range(1, N):
        DP[i][0] = min(DP[i-1][1] + RGB[i][0], DP[i-1][2] + RGB[i][0])
        DP[i][1] = min(DP[i-1][0] + RGB[i][1], DP[i-1][2] + RGB[i][1])
        DP[i][2] = min(DP[i-1][0] + RGB[i][2], DP[i-1][1] + RGB[i][2])

    print(min(DP[-1]))