import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

def brute_forth(k):
    global m
    for i in range(N):
        for j in range(N):
            num = arr[i][j]
            for dk in range(k):
                for ddk in range(dk):
                    # house의 배열을 만들고, i, j 지점마다 house가 해당 지점 안에 들어가는지
                    # abs(i - hi) + abs(j - hj) <= K-1:
                    for ni, nj in ((i - dk + ddk, j + ddk), (i + ddk, j + dk - ddk), (i + dk - ddk, j - ddk), (i - ddk, j - dk + ddk)):
                        if  0 <= ni < N and 0<= nj < N:
                            num += arr[ni][nj]

            if num * M - cost >= 0 and num > m:
                # print (i, j, k, num)
                m = num

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 집의 갯수 count
    houses = 0
    for row in arr:
        houses += row.count(1)

    # 운영 영역 K의 최댓값 설정
    K = 0
    cost = 0
    while cost >= 0:
        K += 1
        cost = houses * M - (2*K**2 - 2*K + 1)
    K = min(K, N + 1)

    # mx = M - 1
    m = 1
    for k in range(2, K + 1):
        cost = 2*k**2 - 2*k + 1
        brute_forth(k)

    print(f'#{tc} {m}')