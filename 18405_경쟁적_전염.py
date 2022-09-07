# 284ms
from collections import deque
import sys
input = sys.stdin.readline

def bfs(starts):
    visited = [[0] * (N+2) for _ in range(N + 2)]
    q = deque()

    for i in range(len(starts)):
        q.append((starts[i][1], starts[i][2]))  # 시작점 여러개
        visited[starts[i][1]][starts[i][2]] = (1, starts[i][0]) # visited[i][j] = (거리, 바이러스종류)

    while q:
        i, j = q.popleft()
        if visited[i][j][0] == S + 1:   # bfs이므로 S초까지의 전염이 완료되었다는 의미!
            return (visited[X][Y][1] if visited[X][Y] else 0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = i + di
            nj = j + dj
            if arr[ni][nj] != -1 and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = (visited[i][j][0] + 1, visited[i][j][1])  # 거리(시간)은 1 증가, 바이러스 종류는 그대로
    return visited[X][Y][1]     # 제한시간이 전염이 완료되는 시간보다 클 경우 고려!!!!

N, K = map(int, input().split())
arr = [[-1] * (N + 2)] + [[-1] + list(map(int, input().rstrip().split())) + [-1] for _ in range(N)] + [[-1] * (N + 2)]
S, X, Y = map(int, input().split())

starts = []
for i in range(1, N+1):                 # 바이러스가 위치하는 지점 모두 찾ㄱ;
    for j in range(1, N+1):
        if arr[i][j]:
            starts.append((arr[i][j], i, j))    # (바이러스 종류, 행, 렬)

starts.sort()   # 바이러스 종류 오름차순으로 정렬
result = bfs(starts)

print(result)
