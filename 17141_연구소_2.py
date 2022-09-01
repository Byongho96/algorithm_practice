from pprint import pprint
## 684ms
from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

def bfs():
    # visited = [[0] * (N + 2)for _ in range(N + 2)]    # 나중에 visited배열을 함수 밖에서 사용하기 위해, 상위함수에 정의했음
    q = deque()

    for sp in comb:
        q.append(sp)
        visited[sp[0]][sp[1]] = 1

    i, j = 0, 0
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if arr[ni][nj] != 1 and not visited[ni][nj]:    # [1]로 감싸서, 범위 안 조건식 생략
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

    # pprint(visited)
    return visited[i][j] - 1


N, M = map(int, input().split())
# arr를 1로 감싸서 입력 받음
arr = [[1] * (N + 2)] + [[1] + list(map(int, input().rstrip().split())) + [1] for _ in range(N)] + [[1] * (N + 2)]

# start 포인트 찾기
start = []
for i in range(N + 2):
    for j in range(N + 2):
        if arr[i][j] == 2:
            start.append((i, j))

mn = N * N
for comb in combinations(start, M):  # 백트래킹으로 구현 가능
    visited = [[0] * (N + 2) for _ in range(N + 2)]
    result = bfs()
    if result < mn:
        flag = False                # 이중 for문을 탈출하기 위한 변수
        for i in range(1, N + 1):   # arr에서 0인 부분을 visited로 모두 방문하지 않았을 경우, 결과값에서 제외
            for j in range(1, N + 1):
                if not arr[i][j] and not visited[i][j]:
                    flag = True
                    break
            if flag:
                break
        else:
            mn = result

if mn == N * N: # 모든 경우의 수에서 방을 다 채울 수 없을 경우, -1 프린트
    print(-1)
else:
    print(mn)