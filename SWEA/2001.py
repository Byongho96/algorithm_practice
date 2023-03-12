T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    brd = [list(map(int, input().split())) for _ in range(N)]
    max_fly = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0
            for di in range(M):
                for dj in range(M):
                    fly += brd[i+di][j+dj]

            if max_fly < fly:
                max_fly =fly

    print(f'#{t} {max_fly}')