N = int(input())

DP = [[0] * N for _ in range(10)]
for num in range(1, 10):
    DP[num][0] = 1

for n in range(1, N):
    DP[0][n] = DP[1][n - 1]
    for num in range(1, 9):
        DP[num][n] = DP[num-1][n-1] + DP[num+1][n-1]
    DP[9][n] = DP[8][n - 1]

result = 0
for num in range(10):
    result += DP[num][-1]
print(result % 1000000000)
