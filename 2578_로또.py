import sys
sys.setrecursionlimit(20000)    # min(2*2000 , 10*2000)
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    # [1]. DP, 2484ms
    DP = [[1] + [0] * N for _ in range(M + 1)]
    for num_range in range(1, M + 1):
        for num_target in range(1, N + 1):
            if num_range >= num_target:
                DP[num_range][num_target] = DP[num_range//2][num_target-1] + DP[num_range-1][num_target]
            else:
                break
    print(DP[-1][-1])

    # [2]. 메모이제이션, 1244ms
    def memoization(i, j):
        if DP[i][j] != -1:
            return DP[i][j]
        DP[i][j] = memoization(i//2, j-1) + memoization(i-1, j)
        return DP[i][j]

    DP = [[1] + [0] * N] + [[1] + [-1] * N for _ in range(M)]
    print(memoization(M, N))