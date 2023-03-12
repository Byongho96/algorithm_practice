W, H = map(int, input().split())

overview = [[0] * (W+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(H)] + [[0] * (W+2)]

def dfs():
    di = (-1, -1, 0, 0, 1, 1)
    dj = [(-1, 0, -1, 1, -1, 0), (0, 1, -1, 1, 0, 1)]
    visited = [[0] * (W+2) for _ in range(H+2)]
    stk = [(0, 0)]
    visited[0][0] = 1

    result = 0
    while stk:
        i, j = stk.pop()
        for idx in range(6):
            ni = i + di[idx]
            nj = j + dj[i % 2][idx]
            if 0 <= ni < H + 2 and 0 <= nj < W + 2 and not visited[ni][nj]:
                if not overview[ni][nj]:
                    visited[ni][nj] = 1
                    stk.append((ni, nj))
                else:
                    result += 1

    return result

from collections import deque

def bfs():
    di = (-1, -1, 0, 0, 1, 1)
    dj = [(-1, 0, -1, 1, -1, 0), (0, 1, -1, 1, 0, 1)]
    visited = [[0] * (W+2) for _ in range(H+2)]
    q = deque([(0, 0)])
    visited[0][0] = 1

    result = 0
    while q:
        i, j = q.popleft()
        for idx in range(6):
            ni = i + di[idx]
            nj = j + dj[i % 2][idx]
            if 0 <= ni < H + 2 and 0 <= nj < W + 2 and not visited[ni][nj]:
                if not overview[ni][nj]:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                else:
                    result += 1

    return result

# print(dfs())
print(bfs())