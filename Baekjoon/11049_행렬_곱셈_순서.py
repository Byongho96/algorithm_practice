if __name__ == "__main__":
    N = int(input())
    mats = [tuple(map(int, input().split())) for _ in range(N)]

    # create & initiate DP
    DP = [[0] * N for _ in range(N)]

    # fill DP
    for diff in range(1, N):
        for start in range(N - diff):
            end = start + diff

            # find the minimum
            mn = float("inf")
            for mid in range(start, end):
                result = DP[start][mid] + DP[mid + 1][end] + mats[start][0] * mats[mid][1] * mats[end][1]
                if result < mn:
                    mn = result

            DP[start][end] = mn

    print(DP[0][-1])
