from pprint import pprint
from copy import deepcopy
import sys
input = sys.stdin.readline

dir = {1:(-1, 0), 2:(-1, -1), 3:(0, -1), 4:(1, -1), 5:(1, 0), 6:(1, 1), 7:(0, 1), 8:(-1, 1)}

def brute_force(si, sj, sum, arr):
    global mx
    mx = max(mx, sum)           # 매 재귀마다 상어가 먹은 물고기 번호 합을 업데이트

    # 물고기 이동
    for num in range(1, 17):    # 1 ~ 16번까지 물고기 하나 선택
        fi, fj = -1, -1
        for ii in range(4):
            for jj in range(4):
                if arr[ii][jj][0] == num:
                    fi = ii
                    fj = jj
                    break
            if fi != -1:
                break

        if fi == -1:                # 물고기가 없는 경우는 그냥 패스
            continue

        direction = arr[fi][fj][1]  # 물고기 방향 번호
        for i in range(8):          # 최대 8번의 방향 전환
            a, b = divmod(direction + i, 9) # 9 이상이 되는 경우, 9로 나눈 몫과 나머지를 더해 줌. 9가 되었을 경우 0이 아닌 1로 돌아가야하기 때문에
            new_direction = a + b
            di, dj = dir[new_direction]     # 딕셔너리에서 실제 방향 값을 읽어온다
            n_fi = fi + di
            n_fj = fj + dj
            if 0 <= n_fi < 4 and 0 <= n_fj < 4 and arr[n_fi][n_fj][0] != 17:    # 이동할 방향이 범위 이내이고, 상어가 없을 경우
                arr[fi][fj][1] = new_direction                                      # WARNING!!!: 자리 체인지 하기 전에, 원래 물고기 방햐 업데이트!!!
                arr[fi][fj], arr[n_fi][n_fj] = arr[n_fi][n_fj], arr[fi][fj]         # 자리 체인지
                break                                                               # 반복문 탈출

    # 상어 이동 후, 후보군 출력
    direction = arr[si][sj][1]      # 상어의 방향 번호
    di, dj = dir[direction]         # 딕셔너리에서 실제 방향 값을 가져 옴
    for m in range(1, 4):           # 최대 3번까지 나아갈 수 있음
        ni = si + di * m
        nj = sj + dj * m
        if 0 <= ni < 4 and 0 <= nj < 4 and arr[ni][nj][0]:    # 이동할 방향이 범위 이내이고, 물고기가 있을 경우
            # arr 업데이트 (상어이동)
            fish = arr[ni][nj][0]
            arr[si][sj][0] = 0
            arr[ni][nj][0] = 17
            brute_force(ni, nj, sum + fish, deepcopy(arr))  # 업데이트한 정보로 재귀호출, arr는 deepcopy하여 보내줌. 함수 리턴시 복원이 너무 어렵고, 4*4이기 때문에 재귀 깊이가 깊지 않음
            # arr 복원 (다음 후보군 출력을 위해)
            arr[si][sj][0] = 17
            arr[ni][nj][0] = fish

arr = []
for i in range(4):
    row = list(map(int, input().split()))
    arr.append([[row[2*i], row[2*i+1]] for i in range(4)])
# pprint(arr)

mx = 0
first_fish = arr[0][0][0]
arr[0][0][0] = 17   # (0, 0)위치에 상어 위치. 상어는 17로 표기
brute_force(0, 0, first_fish, arr)

print(mx)