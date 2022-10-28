import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

A1 = -1
A2 = -1
for i in range(R):
    if arr[i][0] == -1:
        A1 = i
        A2 = i + 1
        break

for _ in range(T):
    # 확산
    for i in range(R):
        for j in range(C):
            if i == 0:
            elif i == R-1:
            if j == 0:
            elif j == C-1:
            arr[i][]
    # 공기 청정기

result = 0
for row in arr:
    result += sum(row)
print(result)