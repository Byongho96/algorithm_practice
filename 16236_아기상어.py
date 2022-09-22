from pprint import pprint
from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    visited = [[0] * N for _ in range(N)]
    q = deque()

    visited[i][j] = 1
    q.append((i, j))

    d = N*N
    fish = []
    while q:
        # print(q)
        i, j = q.popleft()
        # 2-1. d보다 더 멀어진 것일 때, 1번 처리 되기 전에 넘어간 d+1거리의 요소
        if visited[i][j] > d:
            continue
        # 2-2. d 만큼 떨어진 거리일 때, 1번 처리된 곳이랑 같은 거리 요소
        if visited[i][j] == d:
            if 1 <= arr[i][j] < size:    # 물고기가 있으면
                fish.append((i, j))
            continue
        # 1. 처음 먹을 물고기를 만났을 때 d 저장
        if 1 <= arr[i][j] < size:
            d = visited[i][j]
            fish.append((i, j))
            continue
        # 최소거리 d보다 커진 경우에는 밑에 실행 안함
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] <= size and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    # pprint(visited)
    # print('fish', fish)
    if not len(fish):
        return 0, 0, 0
    fish.sort()
    # print('size', size, 'd', d, fish)
    return d - 1, fish[0][0], fish[0][1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

si, sj = -1, -1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            si = i
            sj = j
            break
    if si != -1:
        break

total_time = 0
fish = 0
size = 2
while True:
    time, i, j = bfs(si, sj)
    if not time:
        break
    # size처리
    fish += 1
    if fish == size:
        size += 1
        fish = 0
    # time처리
    total_time += time
    # arr수정
    arr[si][sj] = 0
    arr[i][j] = size + 1
    # si sj 업데이트
    si, sj = i, j

print(total_time)