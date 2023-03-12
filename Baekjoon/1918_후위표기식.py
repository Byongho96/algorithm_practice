string = input()

result = []
stk = []
ref = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

for s in string:
    if s.isalpha():                                                 # 피연산자: push
        result.append(s)

    else:                                                           # 연산자일 경우:
        if s == '(':                                                    # '(': push
            stk.append(s)

        elif s == ')':                                                  # ')': '('만날때까지 stk.pop()
            while stk[-1] != '(':
                result.append(stk.pop())
            stk.pop()                                                       # '('은 버림

        else:                                                           # 그 외 연산자일 경우:
            while stk and ref[s] <= ref[stk[-1]] and stk[-1] != '(':        # 자기보다 우선순위가 낮은 연산자를 만나거나, '('를 만날 때가지 stk.pop()
                result.append(stk.pop())
            stk.append(s)                                                   # 그 다음에 연산자 push

    # print(stk)

while stk:                      # 연산이 끝난 후, 남은 연산자들도 모두 결과값으로 stk.pop()
    result.append(stk.pop())

print(''.join(result))