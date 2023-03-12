import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

def backtracking(idx, cost):
    # print(idx, cost)
    global mn
    if idx >= 12:
        mn = min(mn, cost)
        return
    if cost > mn:
        return
    if uses[idx]:
        backtracking(idx + 1, cost + min(d * uses[idx], m))
        backtracking(idx + 3, cost + t)
        backtracking(idx + 12, cost + y)
    else:
        backtracking(idx + 1, cost)


T = int(input())
for tc in range(1, T + 1):
    d, m, t, y = map(int, input().split())
    uses = list(map(int, input().split()))

    must = set()
    for i in range(12):
        if uses[i]:
            must.add(i)

    mn = 3000 * 12
    backtracking(0, 0)

    print(f'#{tc} {mn}')