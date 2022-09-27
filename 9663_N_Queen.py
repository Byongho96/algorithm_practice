## Pypy 30320
N = int(input())

def isPromising(i, j):
    for ii in range(i):
        if row[ii] == j or abs(row[ii] - j) == i - ii:
            return False
    return True

def nQueen(i):
    global ans
    # 종료조건
    if i == N:
        # print(row)
        ans += 1
        return
    # 가지치기
    # 후고분 출력
    else:
        for j in range(N):
            row[i] = j
            if isPromising(i, j):
                nQueen(i + 1)


ans = 0
row = [0] * N
nQueen(0)
print(ans)


#######################################################
# Look_Up table
def dfs_tbl(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        if j not in v1 and (n + j) not in v2 and (n - j) not in v3:
            v1.append(j), v2.append(n + j), v3.append(n - j)
            dfs_tbl(n + 1)
            v1.pop(), v2.pop(), v3.pop()


N = int(input())
arr = [[0] * N for _ in range(N)]
ans = 0

# dfs(0)

v1 = []
v2 = []
v3 = []
dfs_tbl(0)
print(ans)