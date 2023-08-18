class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # set the initial DP
        DP = [0] + [1] * n

        # update DP
        for _ in range(m - 1):
            for i in range(1, n + 1):
                DP[i] += DP[i-1]

        return DP[-1]