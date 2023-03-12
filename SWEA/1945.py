T = int(input())

for t in range(1, T+1):

    N = int(input()) # 숫자를 입력 받음
    index = [0] * 5 # [a, b, c, d, e]

    i = 0  # index리스트의 인덱스 값
    for n in (2, 3, 5, 7, 11):
        
        while True:
            r = N % n 
            if r:       # 나눠 떨어지지 않았을 경우, 다음 숫자
                break
            N = N // n  # 나눠 떨어질 경우, N을 나누고 해당하는 알파벳 +1
            index[i] += 1

        i += 1  # 다음 알파벳의 인덱스를 가리킴

    print(f'#{t}', *index)