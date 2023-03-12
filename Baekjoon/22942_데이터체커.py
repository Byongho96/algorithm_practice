# 구글링
import sys
input = sys.stdin.readline

N = int(input())
lst = []
stk = [0] * 400000
top = -1

for i in range(N):
    cen, rad = map(int, input().rstrip().split())
    lst.append(((cen-rad), i, 0))
    lst.append(((cen+rad), i, 1))

lst.sort()

for point in lst:
    if not point[2]:
        top += 1
        stk[top] = point
    else:
        stk_point = stk[top]
        if stk_point[1] == point[1]:
            top -= 1
        else:
            print('NO')
            break
else:
    print('YES')
