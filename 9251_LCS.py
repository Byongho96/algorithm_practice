str1 = input()
str2 = input()
S1 = len(str1)
S2 = len(str2)

DP = [[0] * (S1 + 1) for _ in range(S2 + 1)]
for i in range(1, S2 + 1):
    for j in range(1, S1 + 1):
        if str1[j - 1] == str2[i - 1]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])

print(DP[-1][-1])