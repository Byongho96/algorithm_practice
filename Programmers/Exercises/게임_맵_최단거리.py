from collections import deque

def solution(maps):
    # maps 크기 구하기
    N = len(maps)
    M = len(maps[0])
    
    # maps 테두리에 벽 세우기
    for i in range(N):
        maps[i] = [0] + maps[i] + [0]
    maps = [[0] * (M + 2)] + maps + [[0] * (M + 2)]
    
    # bfs
    visited = [[0] * (M + 2) for _ in range(N + 2)]
    queue = deque()
    
    visited[1][1] = 1
    queue.append((1, 1))
    
    while queue:
        i, j = queue.popleft()
        
        if i == N and j == M :
            return visited[i][j]
        
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni = i + di
            nj = j + dj
            if maps[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                queue.append((ni, nj))

    return -1