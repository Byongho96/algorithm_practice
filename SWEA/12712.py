T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    brd = [[0] * (N + 2*(M-1)) for _ in range(M-1)] + [[0] * (M-1) + list(map(int, input().split())) + [0] * (M-1)
                                   for _ in range(N)] + [[0] * (N + 2*(M-1)) for _ in range(M-1)]   # 스프레이 범위만큼 0으로 감싸는 보드
    max = 0

    for i in range(M, N + M-1):
        for j in range(M, N + M-1):
            fly1 = brd[i][j]    # + 모양
            fly2 = brd[i][j]    # x 모양
            for m in range(1, M):   # 스프레이 범위까지 키우기
                fly1 += (brd[i][j + m] + brd[i + m][j] + brd[i][j - m] + brd[i - m][j])
                fly2 += (brd[i - m][j + m] + brd[i + m][j + m] + brd[i + m][j - m] + brd[i - m][j - m])
            if max < fly1:
                max = fly1
            if max < fly2:
                max = fly2

    print(f'#{t} {max}')
