if __name__ == "__main__":
    weight = {'*': 2, '/': 2, '+': 1, '-':1, '(':0} # 스택에서 각 피연산자의 가중치(우선순위?)딕셔너리. 
    inorder = '(' + input() + ')'

    postorder = ''  # 후위표기식 정답
    stack = []      # 연산자를 담을 리스트

    for s in inorder:
        if s.isalpha(): # 피연산자는 바로 postorder에 추가
            postorder += s
            continue
        if s == '(':    # '('는 stack에 append
            stack.append(s)
            continue
        if s == ')':    # ')'가 나올 경우, '('전에 있는 모든 피연산자를 pop하여 postorder에 추가
            while stack[-1] != '(':
                postorder += stack.pop()
            stack.pop()
            continue
        while weight[s] <= weight[stack[-1]]:   # 그 외의 피연산자는 자신보다 낮은 피연산자가 stack의 최상단에 있을 때까지 pop한 이후 postorder에 추가
            postorder += stack.pop()
        stack.append(s)

    print(postorder)




# string = input()

# result = []
# stk = []
# ref = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

# for s in string:
#     if s.isalpha():                                                 # 피연산자: push
#         result.append(s)      

#     else:                                                           # 연산자일 경우:
#         if s == '(':                                                    # '(': push
#             stk.append(s)

#         elif s == ')':                                                  # ')': '('만날때까지 stk.pop()
#             while stk[-1] != '(':
#                 result.append(stk.pop())
#             stk.pop()                                                       # '('은 버림

#         else:                                                           # 그 외 연산자일 경우:
#             while stk and ref[s] <= ref[stk[-1]] and stk[-1] != '(':        # 자기보다 우선순위가 낮은 연산자를 만나거나, '('를 만날 때가지 stk.pop()
#                 result.append(stk.pop())
#             stk.append(s)                                                   # 그 다음에 연산자 push

#     # print(stk)

# while stk:                      # 연산이 끝난 후, 남은 연산자들도 모두 결과값으로 stk.pop()
#     result.append(stk.pop())

# print(''.join(result))