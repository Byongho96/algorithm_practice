import sys
input = sys.stdin.readline

# 참조한 글: https://star7sss.tistory.com/m/377

N = int(input())
T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())

DP = [0] * (N + 1)  # 인덱스 에러 방지
for i in range(N - 1, -1, -1):
    if i + T[i] - 1 < N:
        DP[i] = max(P[i] + DP[i+T[i]], DP[i+1])
    else:
        DP[i] = DP[i+1]

print(DP[0])