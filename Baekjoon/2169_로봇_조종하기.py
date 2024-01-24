import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [[0] * (M + 2)] + [
        [0] + list(map(int, input().split())) + [0] for _ in range(N)
    ]

    # DP Array
    DP = [[0] * (M + 2) for _ in range(N + 1)]

    # Fill DP First array
    for j in range(1, M + 1):
        DP[1][j] = DP[1][j - 1] + arr[1][j]

    # Fill DP the rest array
    NEGATIVE_INF = -101 * N * M
    ltr = [NEGATIVE_INF] + [0] * (M) + [NEGATIVE_INF]
    rtl = [NEGATIVE_INF] + [0] * (M) + [NEGATIVE_INF]
    for i in range(2, N + 1):
        for j in range(1, M + 1):
            # From left to right
            ltr[j] = max(DP[i - 1][j], ltr[j - 1]) + arr[i][j]
            # From right to left
            nj = M + 1 - j
            rtl[nj] = max(DP[i - 1][nj], rtl[nj + 1]) + arr[i][nj]

        # Update DP
        for j in range(1, M + 1):
            DP[i][j] = max(ltr[j], rtl[j])

    print(DP[N][M])
