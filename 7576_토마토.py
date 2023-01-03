from collections import deque

def bfs(starts, box, N, M, cnt_0):
    q = deque(starts)

    i, j = 0, 0
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and not box[ni][nj]:
                box[ni][nj] = box[i][j] + 1
                cnt_0 -= 1
                q.append((ni, nj))
    
    return cnt_0, box[i][j] - 1

M, N = map(int, input().split())

box =  [list(map(int, input().split())) for _ in range(N)]

cnt_0 = 0
starts = []
for i in range(N):
    for j in range(M):
        if not box[i][j]:
            cnt_0 += 1
        elif box[i][j] == 1:
            starts.append((i, j))

cnt_0, result = bfs(starts, box, N, M, cnt_0)


if cnt_0:
    print('-1')
else:
    print(result)

