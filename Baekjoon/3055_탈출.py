from collections import deque
import sys
input = sys.stdin.readline

def bfs(starts):
    visited = [[0] * (C + 2) for _ in range(R + 2)]
    q = deque()

    q.extend(starts)
    for start in starts:
        visited[start[0]][start[1]] = 1

    while q:
        i, j, type = q.popleft()
        if arr[i][j] == 'D':
            return visited[i][j] - 1
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if arr[ni][nj] != 'X' and not visited[ni][nj]:
                if not(arr[ni][nj] == 'D' and type == 'w'):     # 물은 비버의 굴로 침입 불가능
                    q.append((ni, nj, type))
                    visited[ni][nj] = visited[i][j] + 1
    return 'KAKTUS'

R, C = map(int, input().split())
arr = [['X'] * (C + 2)] + [['X'] + list(input().rstrip()) + ['X'] for _ in range(R)] + [['X'] * (C + 2)]

starts = []
for i in range(R+1):
    for j in range(C+1):
        if arr[i][j] == 'S':
            starts.append((i, j, 'h'))
        elif arr[i][j] == '*':              # WARNING: 물 시작지점이 없을 수도 있음
            starts.insert(0, (i, j, 'w'))       # 물 시작지점을, 고슴도치 시작지점보다 앞에 두기!!

result = bfs(starts)

print(result)
