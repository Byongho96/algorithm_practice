from copy import deepcopy

def consturct(i, j):
    candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sdk_r = list(zip(*sdk))
    for ele in candidates[::-1]:
        if ele in sdk[i]:
            candidates.remove(ele)
    for ele in candidates[::-1]:
        if ele in sdk_r[j]:
            candidates.remove(ele)
    ii = i//3*3
    jj = j//3*3
    for ele in candidates[::-1]:
        if ele in sdk[ii][jj:jj+3]:
            candidates.remove(ele)
    for ele in candidates[::-1]:
        if ele in sdk[ii+1][jj:jj+3]:
            candidates.remove(ele)
    for ele in candidates[::-1]:
        if ele in sdk[ii+2][jj:jj+3]:
            candidates.remove(ele)

    return candidates

def backtracking(n):
    if result:  # 한개만 있으면 됨
        return
    # 종료조건
    elif n == N:
        result.append(deepcopy(sdk))
    # 가지치기
    # 후보군 출력
    else:
        i, j = nodes[n][0], nodes[n][1]
        for num in consturct(i, j):
            sdk[i][j] = num
            backtracking(n+1)
            sdk[i][j] = 0

def backtracking2(v):
    visited = [[0] * 10 for _ in range(N)]
    stk = []

    while True:
        for ele in consturct(nodes[v][0], nodes[v][1]):
            if not visited[v][ele]:
                sdk[nodes[v][0]][nodes[v][1]] = ele
                visited[v][ele] = 1
                stk.append((v, ele))
                v += 1
                if v == N:
                    result.append(sdk)
                    return
                break
        else:
            if stk:
                sdk[nodes[v][0]][nodes[v][1]] = 0
                stk.pop()
                v -= 1
            else:
                break

sdk = [list(map(int, input().split())) for _ in range(9)]

nodes = []
for i in range(9):
    for j in range(9):
        if not sdk[i][j]:
            nodes.append((i, j))
N = len(nodes)

result = []
backtracking2(0)

for row in result[0]:
    print(*row)