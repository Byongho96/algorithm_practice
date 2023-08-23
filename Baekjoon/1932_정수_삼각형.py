import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # create & initiate DP array
    DP = arr[-1][:]

    # fill the DP
    for i in range(N - 2, -1, -1):
        for j in range(i + 1):
            DP[j] = max(DP[j], DP[j + 1]) + arr[i][j]

    print(DP[0]) 