import sys
sys.stdin= open('input.txt', 'r', encoding='UTF-8')

def bfs(i, j):
    visited = [[0]*16 for _ in range(16)]
    q = []

    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if maze[ni][nj] != 1 and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                if maze[ni][nj] == 3:
                    return 1
    return 0


for _ in range(10):

    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    result = bfs(1, 1)

    print(f'#{T} {result}')