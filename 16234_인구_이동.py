n, mn, mx = map(int, input().split())

population = [[0] * (n+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (n+2)]

di = (1, -1, 0, 0)
dj = (0, 0, 1, -1)

# from collections import deque

# def bfs(si, sj):
#     global isMoved
#     q = deque([(si, sj)])
#     visited[si][sj] = 1

#     sm = population[si][sj]
#     lst = [(si, sj)]

#     while q:
#         i, j = q.popleft()
#         for idx in range(4):
#             ni = i + di[idx]
#             nj = j + dj[idx]
#             if not visited[ni][nj] and mn <= abs(population[ni][nj] - population[i][j]) <= mx:
#                 visited[ni][nj] = 1
#                 q.append((ni, nj))

#                 lst.append((ni, nj))
#                 sm  += population[ni][nj]
    
#     if len(lst) > 1:
#         average = sm // len(lst)
#         for i, j in lst:
#             population[i][j] = average
#         isMoved = True

# def dfs(si, sj):
#     global isMoved
#     stk = [(si, sj)]
#     visited[si][sj] = 1

#     sm = population[si][sj]
#     lst = [(si, sj)]

#     while stk:
#         i, j = stk.pop()
#         for idx in range(4):
#             ni = i + di[idx]
#             nj = j + dj[idx]
#             if not visited[ni][nj] and mn <= abs(population[ni][nj] - population[i][j]) <= mx:
#                 visited[ni][nj] = 1
#                 stk.append((ni, nj))

#                 lst.append((ni, nj))
#                 sm  += population[ni][nj]
    
#     if len(lst) > 1:
#         average = sm // len(lst)
#         for i, j in lst:
#             population[i][j] = average
#         isMoved = True

def dfs2(si, sj):
    global isMoved
    visited[si][sj] = 1
    stk = []

    sm = population[si][sj]
    lst = [(si, sj)]

    i, j = si, sj
    while True:
        for idx in range(4):
            ni = i + di[idx]
            nj = j + dj[idx]
            if not visited[ni][nj] and mn <= abs(population[ni][nj] - population[i][j]) <= mx:
                stk.append((i, j))
                i, j = ni, nj
                visited[i][j] = 1

                sm += population[i][j]
                lst.append((i, j))
                break
        else:
            if stk:
                i, j = stk.pop()
            else:
                break
    
    if len(lst) > 1:
        average = sm // len(lst)
        for i, j in lst:
            population[i][j] = average
        isMoved = True

result = 0
for _ in range(2000):
    # visited 배열 초기화
    isMoved = False
    visited = [[1] * (n+2)] + [[1] + [0] * n + [1] for _ in range(n)] + [[1] * (n+2)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if not visited[i][j]:
                # 바로 함수에서 업데이트까지 진행. 어차피 visited=1처리 되면 별개의 국가
                dfs2(i, j)
    if not isMoved:
        break
    result += 1

print(result)
        

# from collections import deque
# import sys
# input = sys.stdin.readline

# def bfs(i, j):
#     global flag

#     q = deque()
#     tmp = []            # 연합국을 저장할 리스트
#     people = 0          # 연합국의 총사람수를 저장할 변수

#     q.append((i, j))
#     visited[i][j] = 1
#     tmp.append((i, j))
#     people += arr[i][j]
#     while q:
#         i, j = q.popleft()
#         for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
#             ni = i + di
#             nj = j + dj
#             if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and L <= abs(arr[ni][nj] - arr[i][j]) <= R:  # 조건에 맞을 때만, 연합국에 추가
#                 q.append((ni, nj))
#                 visited[ni][nj] = 1
#                 tmp.append((ni, nj))
#                 people += arr[ni][nj]

#     if len(tmp) > 1:                # 연합국의 수가 2개 이상일 때, 하나면 연합국이 아니라 그냥 하나의 국가이므로 인구이동 X
#         flag = 1                        # 인구이동이 있었다고, 외부 flag를 바꿔줌
#         avg = people // len(tmp)
#         for i, j in tmp:                # 인구이동 실시
#             arr[i][j] = avg

# N, L, R = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# cnt = 0
# while True:
#     flag = 0                                # 인구이동 방문여부를 표시하는 flag. bfs내부에서 바꿔줌
#     visited = [[0] * N for _ in range(N)]   # visited배열을 bfs 밖에 형성해줌. 밑에서 이중 for문을 도는 동안 유지되어야 하기 때문
#     for i in range(N):
#         for j in range(N):
#             if not visited[i][j]:                   # 방문하지 않은 노드에 대해서만 bfs 돌림
#                 bfs(i, j)
#     if not flag:                            # 아무런 인구이동이 없었을 경우, while문 탈출
#         break
#     cnt += 1                                # 날자 카운팅

# print(cnt)






















#
# def move(nations):
#     for nation in nations:
#         sm = sum(arr[i][j] for i, j in nation)
#         average = sm // len(nation)
#         for i, j in nation:
#             arr[i][j] = average
#
# def bfs():
#     visited = [[0] * N for _ in range(N)]
#     nations = []
#     for i in range(N):
#         for j in range(N):
#             if visited[i][j]:
#                continue
#             q = deque()
#             nation = []
#
#             visited[i][j] = 1
#             q.append((i, j))
#             nation.append((i, j))
#
#             while q:
#                 i, j = q.popleft()
#                 for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
#                     ni = i + di
#                     nj = j + dj
#                     if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
#                         if L <= abs(arr[i][j] - arr[ni][nj]) <= R:
#                             visited[ni][nj] = 1
#                             q.append((ni, nj))
#                             nation.append((ni, nj))
#
#             if len(nation) > 1:
#                 nations.append(nation)
#
#     if nations:
#         move(nations)
#         return True
#     else:
#         return False
#
# N, L, R = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# cnt = 0
# while True:
#     result = bfs()
#     if not result:
#         break
#     # pprint(arr)
#     cnt += 1
#
# print(cnt)
# #

