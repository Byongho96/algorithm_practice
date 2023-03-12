bingo = [list(map(int, input().split())) for _ in range(5)]

announce = []
for _ in range(5):
    announce += list(map(int, input().split()))

cnt = 0
B = 0
for num in announce:
    cnt += 1
    # 빙고 숫자 0 으로 지우기
    flag = 0    # 한번에 2개의 for문을 탈출하기 위한 변수
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == num:
                bingo[i][j] = 0
                flag = 1
                break
        if flag:
            break
    # 빙고 검사
    if cnt >= 12: # 최소 12회 이후부터 빙고 가능
        B = 0
        for _ in range(2):  # 행, 열 빙고검사
            for row in bingo:
                if sum(row) == 0:
                    B += 1
            bingo = list(zip(*bingo))
            for i in range(len(bingo)): # zip사용 시 튜플 인 리스트 -> 리스트 인 리스트
                bingo[i] = list(bingo[i])
        lrCross = 0
        rlCross = 0
        for i in range(5):  # 대각선 빙고검사
            lrCross += bingo[i][i]
            rlCross += bingo[4-i][i]
        if not lrCross:
            B += 1
        if not rlCross:
            B += 1

    # 빙고 여부
    if B >= 3:
        print(cnt)
        break