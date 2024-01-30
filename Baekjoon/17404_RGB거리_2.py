import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    INF = 1000 * N + 1
    RGB = [list(map(int, input().split())) for _ in range(N)]

    # Fill DP
    answer = INF
    for start in range(3):
        # Set the start color
        DP = [[INF, INF, INF], [0, 0, 0]]
        DP[0][start] = RGB[0][start]

        cur, prev = 0, 0
        for n in range(1, N):
            cur = n % 2
            prev = 1 - cur

            DP[cur][0] = RGB[n][0] + (
                DP[prev][1] if DP[prev][1] < DP[prev][2] else DP[prev][2]
            )
            DP[cur][1] = RGB[n][1] + (
                DP[prev][0] if DP[prev][0] < DP[prev][2] else DP[prev][2]
            )
            DP[cur][2] = RGB[n][2] + (
                DP[prev][0] if DP[prev][0] < DP[prev][1] else DP[prev][1]
            )

        # Update answer
        answer = min(answer, DP[cur][(start + 1) % 3], DP[cur][(start + 2) % 3])

    print(answer)
