import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    n = int(N ** (1 / 3))

    for num in (n, n+1, n-1, ):
        if num ** 3 == N:
            print(f'#{tc} {num}')
            break
    else:
        print(f'#{tc} {-1}')