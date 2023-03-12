import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

from collections import deque

def bfs(i, j):
    q = deque()
    distance = [[-1] * N for _ in range(N)]

    q.append((i, j))
    distance[i][j] = 0

    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:
                tmp_dist = distance[i][j] + arr[ni][nj]
                if distance[ni][nj] == -1 or tmp_dist < distance[ni][nj]:
                    distance[ni][nj] = tmp_dist
                    q.append((ni, nj))

    return distance[-1][-1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    print(f'#{tc} {bfs(0, 0)}')