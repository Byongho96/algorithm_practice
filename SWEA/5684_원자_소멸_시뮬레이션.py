import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

ref = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    time = [0]
    atoms = [[] for _ in range(N)]
    for _ in range(N):
        j, i, d, e = map(int, input().split())
        di, dj = ref[d]
        atoms.extend([i + time[0] * di, j + time * dj])
        atoms.extend([i, j , d, e])

    atoms.sort()
    # 0.5초 체크
    for i in range(N):
        if atoms[i]

    # 1초 체크
    for i in range(N):
        if atoms[i]
    energy = 0

    print(f'#{tc} {energy}')