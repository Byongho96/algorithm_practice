
import sys
sys.stdin = open('input.txt','r',encoding='UTF-8')

def postorder_ope(cur):                  # 후위순위로 돌면서 결과값을 연산하는 함수
    if ch1[cur]:                            # 자식노드가 있으면
        left = postorder_ope(ch1[cur])          # 왼쪽 자식에 대해 재귀
        right = postorder_ope(ch2[cur])         # 오른쪽 자식에 대해 재귀
        if item[cur] == '+':                    # 받은값을 연산자에 따라 연산
            return left + right
        elif item[cur] == '-':
            return left - right
        elif item[cur] == '*':
            return left * right
        else:
            return left // right
    return item[cur]                        # 리프노드이면, 자기 숫자 반환

for tc in range(1, 11):
    N = int(input())

    item = [0] * (N + 1)                    # 노드의 값을 저장할 리스트
    ch1 = [0] * (N + 1)                     # 왼쪽 자식노드 인덱스를 저장할 리스트
    ch2 = [0] * (N + 1)                     # 오른쪽 자식노드 인덱스를 저장할 리스트
    for _ in range(N):
        tmp = input().split()                   # 입력받은 값의 길이에 따라, 적절하게 저장
        if len(tmp) == 4:
            i, ope, c1, c2 = tuple(tmp)
            i, c1, c2 = map(int, (i, c1, c2))
            ch1[i] = c1
            ch2[i] = c2
            item[i] = ope
        else:
            i, it = map(int, tmp)
            item[i] = it

    result = postorder_ope(1)               # 함수 돌리기

    print(f'#{tc} {result}')