# PyPy3 502420KB, 2208 ms
from collections import deque
import sys
input = sys.stdin.readline

def bfs(froms, ends):
    visited = [0] * (B + 1)
    q = deque()

    for v in froms:
        visited[v] = 1
        q.append(v)

    while q:
        v = q.popleft()
        if v in ends:           # for문 안에 넣으려면 시작지랑 목적지랑 같은 버스 노선 안에 있을 때를 고려해서 처리해야 한다
            return visited[v]
        for w in adjLst[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                q.append(w)

N, M = map(int, input().split())
B = int(input())

# 버스노선 입력받기
d = [0] * (B + 1)                       # 방향(가로:0, 세로:1)
starts = [[] for _ in range(B + 1)]     # 버스의 시작점
ends = [[] for _ in range(B + 1)]       # 버스의 종점
for _ in range(B):
    i, j1, i1, j2, i2 = map(int, input().split())
    if i1 == i2:                            # 가로 방향
        if j1 > j2:                             # 열 번호가 큰게 종점
            j1, j2 = j2, j1
    else:                                   # 세로 방향
        d[i] = 1
        if i1 > i2:                             # 행 번호가 큰게 종점
            i1, i2 = i2, i1
    starts[i] = [i1, j1]
    ends[i] = [i2, j2]
sj, si, ej, ei = map(int, input().split())

# 그래프 만들기
adjLst = [[] for _ in range(B + 1)] # 인접리스트 정보
froms = []                          # 출발지를 포함하는 버스 노선 리스트
destinations = []                   # 도착지를 포함하는 버스 노선 리스트
for i in range(1, B + 1):           # 이중 for문으로 2개의 버스 노선 조합을 모두 탐색
    d1 = d[i]
    i1, j1 = starts[i]
    i2, j2 = ends[i]
    for j in range(i + 1, B + 1):
        d3 = d[j]
        i3, j3 = starts[j]
        i4, j4 = ends[j]
        if not d1:                  # 가로
            if not d3 and i1 == i3:     # 가로 - 가로
                if j4 < j1 or j2 < j3:      # 겹치지 않을 경우,
                    pass
                else:                       # 겹칠 경우
                    adjLst[i].append(j)
                    adjLst[j].append(i)
            else:                       # 가로 - 세로
                if i3 <= i1 <= i4 and j1 <= j3 <= j2:   # 겹칠 경우
                    adjLst[i].append(j)
                    adjLst[j].append(i)
        else:                       # 세로
            if not d3:                  # 세로 - 가로
                if i1 <= i3 <= i2 and j3 <= j1 <= j4:   # 겹칠 경우
                    adjLst[i].append(j)
                    adjLst[j].append(i)
            elif j1 == j3:              # 세로 - 세로
                if i4 < i1 or i2 < i3:      # 겹치지 않을 경우,
                    pass
                else:                       # 겹칠 경우
                    adjLst[i].append(j)
                    adjLst[j].append(i)

    # 버스 노선이 출발지와 목적지를 포함하는지 여부 체크
    if not d1:                      # 현재 버스 노선이 가로 방향일 때,
        if i1 == si and j1 <= sj <= j2:
            froms.append(i)
        if i1 == ei and j1 <= ej <= j2:
            destinations.append(i)
    else:                           # 현재 버스 노선이 새로 방향일 때,
        if j1 == sj and i1 <= si <= i2:
            froms.append(i)
        if j1 == ej and i1 <= ei <= i2:
            destinations.append(i)

# print(adjLst)
# print(froms, destinations)
print(bfs(froms, destinations))

