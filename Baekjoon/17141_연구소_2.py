from itertools import combinations
from collections import deque

di = (1, 0, 0, -1)
dj = (0, 1, -1, 0)

def bfs(starts):
    visited = [[0] * (N + 2) for _ in range(N + 2)]
    queue = deque()
    for si, sj in starts:
        visited[si][sj] = 1
        queue.append((si, sj))

    num_diffused = len(starts)
    mx_seconds = 0

    while queue:
        i, j = queue.popleft()
        for idx in range(4):
            ni = i + di[idx]
            nj = j + dj[idx]
            
            # 모두 확산된 경우
            if num_diffused > num_empty - 1:
                return mx_seconds
            
            # 이미 최소조건을 넘은 경우
            if mx_seconds > mn_seconds - 1:
                return N * M

            if arr[ni][nj] != 1 and not visited[ni][nj]:    # 확산 가능하고, 아지 확산되지 않은 곳일 경우
                visited[ni][nj] = visited[i][j] + 1
                mx_seconds = max(mx_seconds, visited[i][j])
                num_diffused += 1
                queue.append((ni, nj))
                
    return N * M

if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = [[1] * (N + 2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + [[1] * (N + 2)]

    spots = []
    num_empty = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if not arr[i][j]:
                num_empty += 1
            elif arr[i][j] == 2:
                spots.append((i ,j))
                num_empty += 1

    mn_seconds = N * M
    for comb in combinations(spots, M):
        mn_seconds = min(mn_seconds, bfs(comb))

    print(-1) if mn_seconds == N*M else print(mn_seconds)