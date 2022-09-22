from pprint import pprint
from copy import deepcopy
import sys
input = sys.stdin.readline

dir = {1:(-1, 0), 2:(-1, -1), 3:(0, -1), 4:(1, -1), 5:(1, 0), 6:(1, 1), 7:(0, 1), 8:(-1, 1)}

def brute_force(si, sj, sum, arr):
    global mx
    mx = max(mx, sum)
    # 물고기 이동
    for num in range(1, 17):
        fi, fj = -1, -1
        for ii in range(4):
            for jj in range(4):
                if arr[ii][jj][0] == num:
                    fi = ii
                    fj = jj
                    break
            if fi != -1:
                break

        if fi == -1:    # 물고기가 없는 경우
            continue

        direction = arr[fi][fj][1]
        for i in range(8):  # 8번 방향 전환
            a, b = divmod(direction + i, 9)
            new_direction = a + b
            di, dj = dir[new_direction]
            n_fi = fi + di
            n_fj = fj + dj
            if 0 <= n_fi < 4 and 0 <= n_fj < 4 and arr[n_fi][n_fj][0] != 17:
                arr[fi][fj], arr[n_fi][n_fj] = arr[n_fi][n_fj], arr[fi][fj]
                break

    # 후보군 출력
    direction = arr[si][sj][1]
    di, dj = dir[direction]
    ni, nj = si+di, sj+dj
    while 0 <= ni < 4 and 0 <= nj < 4:
        print(ni, nj)
        fish = arr[ni][nj][0]
        if arr[ni][nj][0]:
            arr[si][sj][0] = 0
            arr[ni][nj][0] = 17
            brute_force(ni, nj, sum + fish, deepcopy(arr))
            arr[ni][nj][0] = fish
        ni += di
        nj += dj

arr = []
for i in range(4):
    row = list(map(int, input().split()))
    arr.append([[row[2*i], row[2*i+1]] for i in range(4)])
# pprint(arr)

mx = 0
arr[0][0][0] = 17
brute_force(0, 0, 0, deepcopy(arr))

print(mx)