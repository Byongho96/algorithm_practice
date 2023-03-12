stk = []
alphas = []
N = int(input())
words = input()

for _ in range(N):
    alphas.append(int(input()))

for w in words:
    if w.isalpha():
        stk.append(alphas[ord(w)-ord('A')])
    else:
        a2 = stk.pop()
        a1 = stk.pop()
        if w == '*':
            a3 = a1 * a2
        elif w == '/':
            a3 = a1 / a2
        elif w == '+':
            a3 = a1 + a2
        else:
            a3 = a1 - a2
        stk.append(a3)

print('%.2f' % stk[0])