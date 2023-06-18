import sys
input = sys.stdin.readline

def cal_chicken_length(arr):
    global N
    global H
    global chicken_length_lst

    chicken_length_per_house = [2 * N] * H
    for c in range(len(arr)):
        if not arr[c]:
            continue
        for h in range(H):
            chicken_length_per_house[h] = min(chicken_length_per_house[h], chicken_length_lst[h][c])
    
    return sum(chicken_length_per_house)


def backtracking_comb(idx, cur_num, target_num, arr):
    global answer

    # 종료 조건
    if cur_num == target_num:
        case = cal_chicken_length(arr)
        answer = min(answer, case)
        return

    # 가지 치기
    if idx > len(arr) - 1:  # 이미 모든 치킨집을 다 돌았을 경우
        return

    if cur_num + len(arr) - idx < target_num: # 모든 치킨집을 다 돌아도 target _num을 만족하지 못하는 ㅕㅇ우
        return

    # 후보군 출력
    arr[idx] = True
    backtracking_comb(idx + 1, cur_num + 1, target_num, arr)
    arr[idx] = False
    backtracking_comb(idx + 1, cur_num, target_num, arr)


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())   # N: 도시의 크기, M: 폐업시키지 않을 치킨집의 최대 개수  
    arr = [list(map(int, input().rstrip().split())) for _ in range(N)]  # 0: 빈칸, 1: 집, 2: 치킨집

    # 치킨집과 집의 좌표를 담은 배열 생성
    chickens = []
    houses = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                houses.append((i, j))
            if arr[i][j] == 2:
                chickens.append((i, j))

    C = len(chickens)   # 현재 치킨집의 갯수
    H = len(houses)

    # chicken_length_lst[house][chicken] = 치킨거리
    chicken_length_lst = [[0] * C for _ in range(H)]
    for h in range(H):
        for c in range(C):
            house_i, house_j = houses[h]
            chicken_i, chicken_j = chickens[c]
            chicken_length_lst[h][c] = abs(house_i - chicken_i) +  abs(house_j - chicken_j)

    answer = 2 * N * H
    backtracking_comb(0, 0, M, [False] * C)

    print(answer)


##########################################################################################################

from itertools import combinations

def cal_chicken_length(arr):
    global N
    global M
    global H
    global chicken_length_lst

    # 선택된 치킨집에 대해서 치킨거리 계산
    chicken_length_per_house = [2 * N] * H
    for c in arr:
        for h in range(H):
            chicken_length_per_house[h] = min(chicken_length_per_house[h], chicken_length_lst[h][c])
    
    return sum(chicken_length_per_house)

if __name__ == "__main__":
    N, M = map(int, input().split())    # N: 도시의 크기, M: 폐업시키지 않을 치킨집의 최대 개수  
    arr = [list(map(int, input().split())) for _ in range(N)]   # 0: 빈칸, 1: 집, 2: 치킨집

    # 치킨집과 집의 좌표를 담은 배열 생성
    chickens = []
    houses = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                houses.append((i, j))
            if arr[i][j] == 2:
                chickens.append((i, j))

    C = len(chickens)   # 현재 치킨집의 갯수
    H = len(houses)

    # chicken_length_lst[house][chicken] = 치킨거리
    chicken_length_lst = [[0] * C for _ in range(H)]
    for h in range(H):
        for c in range(C):
            house_i, house_j = houses[h]
            chicken_i, chicken_j = chickens[c]
            chicken_length_lst[h][c] = abs(house_i - chicken_i) +  abs(house_j - chicken_j)

    answer = 2 * N * H
    for selected_chickens in combinations(list(range(C)), M):
        answer = min(answer, cal_chicken_length(selected_chickens))

    print(answer)
