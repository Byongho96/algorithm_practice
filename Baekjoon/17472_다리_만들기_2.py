from pprint import pprint
from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

def numbering(i, j):
    global number
    q = deque()

    arr[i][j] = number
    visited[i][j] = 1
    q.append((i, j))

    while q:
        i, j = q.popleft()
        for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] and not visited[ni][nj]:
                arr[ni][nj] = number
                visited[ni][nj] = 1
                q.append((ni, nj))

    number += 1

def bfs(v):
    global result
    visited = [0] * (number + 1)
    q = deque()

    cnt = 1                 # 방문한 섬의 갯수 카운팅
    visited[v] = 1
    q.append(v)

    while q:
        v = q.popleft()
        for w in adjLst[v]:
            if not visited[w]:
                visited[w] = 1
                cnt += 1    # 방문한 섬의 갯수 카운팅
                q.append(w)

    if cnt == number:       # bfs가 끝났을 대, 방문한 섬의 갯수가 모든 섬의 갯수이면
        result = min(result, total_distance)    # result를 최솟값으로 업데이트


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 섬마다 번호 매기기. bfs를 약간 활용
# 첫번째 섬의 모든 땅을 1로, 두번재 섬의 모든 땅을 2로, ...
visited = [[0] * M for _ in range(N)]
number = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] and not visited[i][j]:
            numbering(i, j)
number -= 1     # 모든 섬의 갯수
# pprint(arr)

# 건설 가능한 모든 다리의 집합 구하기
# bridges = {(시작 섬 번호, 도착 섬 번호, 다리 길이), }
bridges = set()
for _ in range(2):          # 행과 열 뒤집어서 한 번 더, 가로 세로 방향 탐색
    for row in arr:             # 행 단위로 탐색
        j = 0
        while j < M-2:          # 다리길이가 최소 2 는 되야하므로, 시작 지점을 M-3 까지만 탐색하면 됨
            if row[j] and not row[j+1] and not row[j+2]:    # 시작지점으로부터 2개의 당이 바다일 경우
                br = row[j]
                bridge = 2
                j += 3
                while j < M and not row[j]:                     # 끝지점을 만나거나, 다른 섬을 만날 때까지 탐색
                    bridge += 1
                    j += 1
                if j < M:                                       # 다른 섬을 만난 경우
                    bridges.add((br, row[j], bridge))               # 다리 집합에 정보 추가
                    j -= 1                                          # 밑에 j += 1이 무조건 실행되서, 상쇄하고자 추가
            j += 1
    arr = list(zip(*arr))       # 행, 렬 뒤집기
    N, M = M, N
# print(bridges)

result = N*M
# 다리의 갯수가 n-1개일 때, 중복 없이 모든 섬을 연결가능
# n개 이상일 때부터는 불필요한 다리가 있다는 것
for comb in combinations(bridges, number - 1):  # 다리 집합에서 n-1개의 다리 조합을 추출
    adjLst = [[] for _ in range(number + 1)]
    total_distance = 0
    for bridge in comb:                             # 그래프처럼 인접리스트 형성
        island1, island2, distance = bridge
        adjLst[island1].append(island2)
        adjLst[island2].append(island1)
        total_distance += distance
    bfs(1)                                          # bfs로 모든 섬이 연결되어 있는지 탐색하고, 연결되어있을 경우 result 업데이트

if result == N*M:
    print(-1)
else:
    print(result)