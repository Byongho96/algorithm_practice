from pprint import pprint
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
    arr_tmp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(2):                      # 0, 1 열
            if arr[i][j] > 4:                       # 문제조건상 4이하면 실질적으로 확산이 안됨
                spread = arr[i][j] // 5
                if i < R - 1 and arr[i+1][j] != -1:     # down
                    arr_tmp[i + 1][j] += spread
                    arr[i][j] -= spread
                if i > 0 and arr[i-1][j] != -1:         # up
                    arr_tmp[i - 1][j] += spread
                    arr[i][j] -= spread
                if j < C - 1:                           # right
                    arr_tmp[i][j + 1] += spread
                    arr[i][j] -= spread
                if j > 0 and arr[i][j-1] != -1:         # left
                    arr_tmp[i][j - 1] += spread
                    arr[i][j] -= spread
            arr_tmp[i][j] += arr[i][j]
        for j in range(2, C):                   # 2열 이상
            if arr[i][j] > 4:                       # 문제조건상 4이하면 실질적으로 확산이 안됨
                spread = arr[i][j] // 5
                if i < R - 1:                           # down
                    arr_tmp[i + 1][j] += spread
                    arr[i][j] -= spread
                if i > 0:                               # up
                    arr_tmp[i - 1][j] += spread
                    arr[i][j] -= spread
                if j < C - 1:                           # right
                    arr_tmp[i][j + 1] += spread
                    arr[i][j] -= spread
                arr_tmp[i][j - 1] += spread             # left
                arr[i][j] -= spread
            arr_tmp[i][j] += arr[i][j]

    arr = arr_tmp

    # 공기 청정
    # Counter_ClockWise
    for i in range(A1 - 1, 0, -1):
        arr[i][0] = arr[i-1][0]
    arr[0][:C-1] = arr[0][1:C]
    for i in range(A1):
        arr[i][C-1] = arr[i+1][C-1]
    arr[A1][2:C] = arr[A1][1:C - 1]
    arr[A1][1] = 0

    # ClockWise
    for i in range(A2 + 1, R-1):
        arr[i][0] = arr[i+1][0]
    arr[R-1][:C-1] = arr[R-1][1:C]
    for i in range(R-1, A2, -1):
        arr[i][C-1] = arr[i-1][C-1]
    arr[A2][2:C] = arr[A2][1:C - 1]
    arr[A2][1] = 0

result = 0
for row in arr:
    result += sum(row)
print(result + 2)