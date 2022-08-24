# 2976ms...
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

def Backtracking(m, permu):
    global result
    # 종료조건
    if m == M + 1:
        result.append(permu)
    # 가지치기
    # 후보군 콜
    else:
        for i in range(1, N + 1):
            Backtracking(m+1, permu + [i])


permu = []
result = []
Backtracking(1, permu)

for ele in result:
    print(*ele)

############################################
# 이런식으로 s 하나의 값만 가지고, 전달하지 않으면서 푸는게 더 빠름
# 1472ms
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

s = []


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        s.append(i)
        dfs()
        s.pop()


dfs()