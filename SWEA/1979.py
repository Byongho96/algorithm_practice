T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    pzl = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)] # 오른쪽과 아래쪽 0으로 감싸기
    cnt = 0

    for _ in range(2):  # 행 탐색, 열탐색
        for i in range(N+1):
            ava = 0
            for j in range(N+1):
                if pzl[i][j]:   # 빈칸이 나오면 ava++
                    ava += 1
                    continue
                elif ava == K:  # 빈칸이 단어 길이와 딱 맞을 때
                    cnt += 1
                ava = 0
        pzl = list(zip(*pzl))   # Transpose

    print(f'#{t} {cnt}')