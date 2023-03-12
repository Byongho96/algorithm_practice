T = int(input())

for t in range(1, T+1):

    N = int(input())
    board = [[0] * N for _ in range(N)] # 달팽이 보드 형성

    i, j = 0, -1 # 초기 위치 설정, [0][0]의 가상의 왼쪽 공간에서 시작
    num = 1 # 처음 집어 넣을 값
    distnc = N # 움직여야 할 거리

    while num <= N**2: # N**2개의 수를 모두 집어 넣을 때까지
        # range(-int): 아무 요소 없음
        for _ in range(distnc): # 오른쪽 움직임
            j += 1
            board[i][j] = num
            num += 1
        distnc -= 1             # 움직일 거리가 줄어드는 방향전환

        for _ in range(distnc): # 아래쪽 움직임
            i += 1
            board[i][j] = num
            num += 1
        for _ in range(distnc): # 왼쪽 움직임
            j -= 1
            board[i][j] = num
            num += 1
        distnc -= 1             # 움직일 거리가 줄어드는 방향전환

        for _ in range(distnc): # 위쪽 움직임
            i -= 1
            board[i][j] = num
            num += 1

    print(f'#{t}')
    for i in range(N):
        print(*board[i])