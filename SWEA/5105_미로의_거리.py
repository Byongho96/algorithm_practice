import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

def bfs(i, j, N):
    visited = [[0] * N for _ in range(N)]
    q = []

    q.append((i, j))
    visited[i][j] = 1

    while q:
        i, j = q.pop(0)
        # if maze[i][j] == 3:
        #     return visited[i][j] - 2
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                if maze[ni][nj] == 3:
                    return visited[ni][nj] - 2
    return 0


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    si, sj = -1, -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si = i
                sj = j
                break
        if si != -1:
            break

    result = bfs(si, sj, N)
    print(f'#{t} {result}')