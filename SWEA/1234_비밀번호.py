import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

for T in range(1, 11):
    N, string = input().split()
    stk = [0] * int(N)
    top = -1

    top += 1
    stk[top] = string[0]
    for num in string[1:]:
        if num != stk[top]:
            top += 1
            stk[top] = num
            continue
        top -= 1

    password = ''.join(stk[:top+1])

    print(f'#{T} {password}')