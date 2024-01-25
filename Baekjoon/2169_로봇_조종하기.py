import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    DP = [0] + list(map(int, input().split()))

    # Fill DP the first line
    for j in range(2, M + 1):
        DP[j] += DP[j - 1]

    # Fill DP the rest lines
    ltr = [0] * (M + 1)
    rtl = [0] * (M + 1)
    for i in range(2, N + 1):
        value = [0] + list(map(int, input().split()))
        ltr[1] = DP[1] + value[1]
        rtl[M] = DP[M] + value[M]

        for j in range(2, M + 1):
            # From left to right
            ltr[j] = max(DP[j], ltr[j - 1]) + value[j]

            # From right to left
            nj = M + 1 - j
            rtl[nj] = max(DP[nj], rtl[nj + 1]) + value[nj]

        # Update DP
        for j in range(1, M + 1):
            DP[j] = max(ltr[j], rtl[j])

    print(DP[-1])
