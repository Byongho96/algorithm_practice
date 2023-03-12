import sys
sys.stdin = open('input.txt','r',encoding='UTF-8')

T = int(input())
for t in range(1, T + 1):

    string = input()
    card_lst = [[] for _ in range(4)]

    N = len(string)
    for i in range(N//3):
        T = string[3 * i]
        num = int(string[3 * i + 1: 3 * i + 3])

        if T == 'S':
            T = 0
        elif T == 'D':
            T = 1
        elif T == 'H':
            T = 2
        else:
            T = 3

        if num in card_lst[T]:
            lst = 'ERROR'
            break
        else:
            card_lst[T].append(num)

        lst = ' '.join(map(str, [13-len(card_lst[0]), 13-len(card_lst[1]), 13-len(card_lst[2]), 13-len(card_lst[3])]))

    print(f'#{t} {lst}')
