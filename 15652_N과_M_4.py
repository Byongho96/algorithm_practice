N, M = map(int, input().split())

def backtracking(n, m):
    if m == M:
        print(' '.join(map(str, lst)))
        return
    for num in range(n, N + 1):
        lst[m] = num
        backtracking(num, m+1)
    return

lst = [0] * M
backtracking(1, 0)