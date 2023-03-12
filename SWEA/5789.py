T = int(input())

for t in range(1, T+1):

    N, Q = map(int, input().split())
    box = [0] * N   # N개의 박스 형성

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        box[L-1:R] = [i] * (R - L + 1)  # L ~ R 번 박스, 단 -1씩하여 인덱스 값을 맞춤

    print(f'#{t}', *box)