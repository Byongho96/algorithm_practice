# 112 ms
from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j, arr, lst):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    lst[i][j] = '.'

    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj]:
                if arr[ni][nj] == 'O':
                    q.append((ni, nj))
                visited[ni][nj] = 1
                lst[ni][nj] = '.'

R, C, N = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]

if N == 1:          # 자기 자신 return
    for row in arr:
        print(''.join(row))
elif N % 2:
    bomb1 = [['O'] * C for _ in range(R)]
    visited = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O' and not visited[i][j]:
                bfs(i, j, arr, bomb1)
    if (N // 2) % 2:
        for row in bomb1:
            print(''.join(row))
        exit()

    bomb2 = [['O'] * C for _ in range(R)]
    visited = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if bomb1[i][j] == 'O' and not visited[i][j]:
                bfs(i, j, bomb1, bomb2)
    for row in bomb2:
        print(''.join(row))

else:               # 짝수일 때는 꽉찬 것 리턴
    for _ in range(R):
        print('O' * C)