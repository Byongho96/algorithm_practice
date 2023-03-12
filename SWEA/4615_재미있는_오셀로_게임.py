import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

def backtracking(i, j, color):
    ref = {1: 2, 2: 1}  # 참조할 딕셔너리 {검은돌: 흰돌, 흰돌: 검은돌 =}

    # 처음 놓는 돌
    arr[i][j] = color
    stones[color] += 1

    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)):   # 8방향 탐색
        ni = i + di
        nj = j + dj
        if arr[ni][nj] == ref[color]:           # 어떤 방향에 다른 색의 돌이 있으면
            change_list = [(ni, nj)]                # 바꿀 수 있는 돌들의 리스트
            while arr[ni][nj] == ref[color]:        # 더 이상 다른 색의 돌이 나오지 않을 때까지 진행
                ni += di
                nj += dj
                change_list.append((ni, nj))
            if arr[ni][nj] == color:                # 처음 둔 돌과 동일한 색을 만났을 때, (그 외의 경우: 빈칸(0), 벽(3))
                for change in change_list[:-1]:         # 저장해둔 돌 들의 리스트 색을 바꿈 (마지막은 자기와 같은 색의 돌)
                    arr[change[0]][change[1]] = color
                stones[color] += (len(change_list) - 1)         # 자기 바둑돌 갯수 업데이트
                stones[ref[color]] -= (len(change_list) - 1)    # 상대편 바둑볼 갯수 업데이트

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 바둑판 배열 3으로 감싸서 입력받고, 초기 바둑돌 4개 셋팅
    arr = [[3] * (N + 2)] + [[3] + [0] * N + [3] for _ in range(N)] + [[3] * (N + 2)]
    arr[N // 2][N // 2] = 2
    arr[N // 2][N // 2 + 1] = 1
    arr[N // 2 + 1][N // 2] = 1
    arr[N // 2 + 1][N // 2 + 1] = 2

    stones = [0, 2, 2]  # [ _ , 검은바둑돌, 흰바둑돌]

    for _ in range(M):  # M번의 횟수에 대하여 함수 돌리기
        j, i, color = map(int, input().split())
        backtracking(i, j, color)

    print(f'#{tc} {stones[1]} {stones[2]}')