from collections import deques

di = (0, 1, 0, -1, 1, 1, -1, -1)
dj = (1, 0, -1, 0, -1, 1, 1, -1)

def hollow(arr, i, j):
    visited = [[0] * 102 for _ in range(102)]
    visited[i][j] = 1
    
    stack = []
    stack.append((i, j))
    
    while stack:
        i, j = stack.pop()
        
        is_edge = False
        
        for idx in range(8):
            ni = i + di[idx]
            nj = j + dj[idx]
            if not arr[ni][nj]:
                is_edge = True
            elif arr[ni][nj] == 1 and not visited[ni][nj]:
                stack.append((ni, nj))
                visited[ni][nj] = 1
                
        if not is_edge:
            arr[i][j] = -1
    
def bfs(arr, si, sj, ei, ej):
    visited = [[0] * 102 for _ in range(102)]
    visited[si][sj] = 1
    
    q = deque()
    q.append((si, sj))
    
    while q:
        i ,j = q.popleft()
        
        # 종료조건
        if i == ei and j == ej:
            return visited[i][j] - 1
            
        for idx in range(4):
            ni = i + di[idx]
            nj = j + dj[idx]
            
            if arr[ni][nj] == 1 and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    arr = [[0] * 102 for _ in range(102)]
    
    # 2배 해서 채우기
    for rect in rectangle:
        i1, j1, i2, j2 = map(lambda x: 2 * x, rect)
        for i in range(i1, i2 + 1):
            for j in range(j1, j2 + 1):
                arr[i][j] = 1
    
    # 속 파내기
    hollow(arr, i1, j1)
    
    # 최단 경로 찾기
    answer = bfs(arr, 2 * characterX, 2 * characterY, 2 * itemX, 2 * itemY)
    
    return answer // 2