import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    # 길고 짧은 배열을 구분해서 입력받음, 또한 N이 M보다 작게 유지
    if N > M:
        long = list(map(int, input().split()))
        short = list(map(int, input().split()))
        N, M = M, N
    else:
        short = list(map(int, input().split()))
        long = list(map(int, input().split()))

    # 초깃값 설정
    mx = 0
    for i in range(N):  # 첫번째 곱셈 결과를 초기값으로 설정, 수의 범위가 문제에 안나와있음
        mx += short[i] * long[i]

    # 탐색
    for i in range(1, M - N + 1):  # 길이 차이 +1 만큼 곱셈의 가짓수가 나오는데, 첫번째 가짓수는 초깃값 설정으로 이미 사용
        mul = 0
        for j in range(N):
            mul +=  short[j] * long[i+j]
        if mul > mx:
            mx = mul

    print(f'#{t} {mx}')