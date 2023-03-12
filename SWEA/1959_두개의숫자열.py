import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    Alst = list(map(int, input().split()))
    Blst = list(map(int, input().split()))

    # 초깃값
    max = 0
    for i in range(min(N, M)):
        max += Alst[i] * Blst[i]

    if N > M:   # A리스트가 더 긴 경우
        for i in range(1, (N - M) + 1):
            mulsum = 0
            for j in range(min(N, M)):
                mulsum += Alst[j+i] * Blst[j]
            if mulsum > max:
                max = mulsum
    else:       # B리스트가 더 긴 경우
        for i in range(1, (M - N) + 1):
            mulsum = 0
            for j in range(min(N, M)):
                mulsum += Alst[j] * Blst[j+i]
            if mulsum > max:
                max = mulsum

    print(f'#{t} {max}')