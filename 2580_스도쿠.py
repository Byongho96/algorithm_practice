## Pypy 1896ms
import sys
input = sys.stdin.readline

def isPromising(i, j, num):
    if num in sdk[i]:
        return False
    for row in range(9):
        if sdk[row][j] == num:
            return False
    ii = i // 3 * 3
    jj = j // 3 * 3
    for di in range(3):
        for dj in range(3):
            if sdk[ii+di][jj+dj] == num:
                return False
    return True

def dfs_recursive(n):
    global found
    # 가지치기
    if found:
        return
    # 종료조건
    elif n == N:
        for row in sdk:
            print(' '.join(map(str, row)))
        found = True
        return
    # 후보군 출력
    else:
        i, j = spots[n]
        for num in range(1, 10):
            if isPromising(i, j, num):
                sdk[i][j] = num
                dfs_recursive(n+1)
        sdk[i][j] = 0
        return

sdk = [list(map(int, input().rstrip().split())) for _ in range(9)]
spots = []
for i in range(9):
    for j in range(9):
        if not sdk[i][j]:
            spots.append((i, j))
N = len(spots)

found = False
dfs_recursive(0)