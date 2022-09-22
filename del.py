T = int(input())

for tc in range(1, T+1):
    binary_digit = int(input(), 2)
    # print(binary_digit)
    trit = list(map(int, input()))

    flag = 0
    for i in range(len(trit)):
        # 한자리만 바뀐 3진수
        for j in (0, 1, 2):
            if trit[i] == j:
                continue
            trit_copy = trit[:]
            trit_copy[i] = j
            # print(trit_copy)

            # 3진수 -> 10진수
            digit = 0
            for t in trit_copy:
                digit = digit*3 + t
            # print(digit)

            # xor연산 다를 경우에만 1
            # 따라서 1이 하나만 존재한다면 정답
            result = bin(binary_digit ^ digit)[2:].count('1')
            if result == 1:
                print(f'#{tc} {digit}')
                flag = 1
                break
        if flag:
            break





