import sys
input = sys.stdin.readline

def backtracking(n, time, back):
    global mn_time
    if n == K:
        mn_time = min(mn_time, time)
        return
    if n > K + 1:
        return
    backtracking(n-1, time + 1, back + 1)
    backtracking(n+1, time + 1, 0)
    backtracking(2*n, time, 0)

N, K = map(int, input())

if K <= N:
    print(N - K)
else:
    mn_time = K - N
    backtracking(N, 0, 0)

