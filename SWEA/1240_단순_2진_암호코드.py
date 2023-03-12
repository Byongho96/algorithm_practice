from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

T = int(input())
ref = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,
       '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 뒷열부터 탐색하면서 1이 되는 부분 찾기
    i, j = -1, -1
    flag = 0
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                flag = 1
                break
        if flag:
            break

    # ref 딕셔너리를 참조하면서 대응하는 암호찾기
    code = []
    for _ in range(8):
        num = ref.get(''.join(arr[i][j-6:j+1]))
        code.append(num)
        j -= 7

    # 유효성 검사
    print(f'#{tc}', end=' ')
    if not ((code[1] + code[3] + code[5] + code[7]) * 3 + code[0] + code[2] + code[4] + code[6]) % 10:
        print(sum(code))
    else:
        print(0)
