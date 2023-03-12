import sys
input = sys.stdin.readline

N, M = map(int, input().split())
aLst = list(map(int, input().split()))
bLst = list(map(int, input().split()))

result = []
a, b = 0, 0
while a < N and b < M:
    if aLst[a] < bLst[b]:
        result.append(aLst[a])
        a += 1
    else:
        result.append(bLst[b])
        b += 1
result += aLst[a:] + bLst[b:]

print(*result)
