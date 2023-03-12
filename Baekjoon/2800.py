# 구글링

from itertools import combinations
import sys

input = sys.stdin.readline

fml = input().rstrip()
stk = [] # ['('의 idx]
lst = [] # [( '('의 idx, ')'의 idx )]
ans = set()

for i, f in enumerate(fml):
    if f == '(':
        stk.append(i)
    elif f == ')':
        start = stk.pop()
        end = i
        lst.append((start, end))

for num in range(1, len(lst)+1):
    com = combinations(lst, num)
    for pair in com:
        tmp = list(fml)
        for s, e in pair:
            tmp[s] = ''
            tmp[e] = ''
        ans.add(''.join(tmp))

for i in sorted(list(ans)):
    print(i)