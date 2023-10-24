class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        T1 = len(text1)
        T2 = len(text2)
        DP = [[0] * (T2 + 1) for _ in range(T1 + 1)]

        for i in range(1, T1 + 1):
            for j in range(1, T2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    DP[i][j] = DP[i - 1][j - 1] + 1
                else:
                    DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

        return DP[-1][-1]
