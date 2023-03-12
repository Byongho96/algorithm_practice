stk = []
rlt = []
N = int(input())

cur = 1
for _ in range(N):
    num = int(input())
    while cur <= num:
        stk.append(cur)
        rlt.append('+')
        cur += 1
    if stk[-1] == num:
        stk.pop()
        rlt.append('-')
    else:
        print('NO')
        break
else:
    for i in rlt:
        print(i)