import sys
from collections import deque
input = sys.stdin.readline

dir_ref = {0: (0, 1), 1: (0, -1), 2: (1, 0), 3: (-1, 0)}        # { 현재방향: (i증가 방향, j증가 방향)}
turn_ref = {0: (2, 3), 1: (2, 3), 2: (0, 1), 3: (0, 1)}         # { 현재방향: (회전 시 방향1, 회전 시 방향2)}

def bfs2():
    INF= 20002
    visited = [[[0] * 4 for _ in range(M)] for _ in range(N)]
    q = deque()

    visited[si-1][sj-1][sd-1] = 1
    q.append((si-1, sj-1, sd-1))

    while q:
        i, j, d = q.popleft()
        if i == ei-1 and j == ej-1 and d == ed-1:   # 종료조건
            return visited[ei-1][ej-1][ed-1] - 1

        # 무조건 1씩 증가하도록 설계
        # 1. 거리증가
        for dist in range(1, 4):        # 1~3까지 한번에 이동할 수 있음
            ni = i + dir_ref[d][0] * dist
            nj = j + dir_ref[d][1] * dist
            if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj]: # 해당 위치로 직진이 가능한 경우
                if not visited[ni][nj][d]:                          # 해당 위치와 방향을 방문하지 않았을 경우에만 append
                    q.append((ni, nj, d))
                    visited[ni][nj][d] = visited[i][j][d] + 1
            else:                                               # 직진이 불가능한 경우 break하여 for문을 탈출해야 함, 안그러면 예외케이스 발생
                break
        # 2. 방향변환
        for nd in turn_ref[d]:          # turn_ref 딕셔너리를 미리 정의하여 값을 읽어옴
            if not visited[i][j][nd]:       # 해당 위치와 방향을 방문하지 않았을 경우에만 append
                q.append((i, j, nd))
                visited[i][j][nd] = visited[i][j][d] + 1

N, M = map(int, input().split())
# arr = [[1]*(M+2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + [[1]*(M+2)]
arr = [list(map(int, input().split())) for _ in range(N)]
si, sj, sd = map(int, input().split())
ei, ej, ed = map(int, input().split())

# bfs()
print(bfs2())
# mn = 20002
# dfs(si, sj, sd, 0, 3)
# print(mn)


#
# import sys
# from pprint import pprint
# from collections import deque
# input = sys.stdin.readline
#
# ref = {1: (0, 0, 2, 1, 1), 2: (0, 2, 0, 1, 1), 3: (0, 1, 1, 0, 2), 4: (0, 1, 1, 2, 0)}
#
# def bfs():
#     INF= 20002
#     visited = [[INF] * (M + 2) for _ in range(N + 2)]
#     q = deque()
#
#     visited[si][sj] = 0
#     q.append((si, sj, sd, 0, 3))
#
#     mn = INF
#     while q:
#         i, j, d, cost, dist = q.popleft()
#         if i == ei and j == ej:
#             mn = min(mn, cost + ref[d][ed])
#         for di, dj, nd in ((0, 1, 1), (0, -1, 2), (1, 0, 3), (-1, 0, 4)):
#             ni = i + di
#             nj = j + dj
#             if not arr[ni][nj]:
#                 if d != nd:
#                     new_cost = cost + ref[d][nd] + 1
#                     new_dist = 1
#                 elif dist != 3:
#                     new_cost = cost
#                     new_dist = dist + 1
#                 else:
#                     new_cost = cost + 1
#                     new_dist = 1
#                 if new_cost <= visited[ni][nj]:
#                     visited[ni][nj] = new_cost
#                     q.append((ni, nj, nd, new_cost, new_dist))
#                 elif new_cost == visited[ni][nj] + 1:
#                     q.append((ni, nj, nd, new_cost, new_dist))
#     # pprint(visited)
#     print(mn)
#
# def dfs(i, j, d, cnt, m):
#     global mn
#     if i == ei and j == ej:
#         mn = min(mn, cnt + ref[d][ed])
#         return
#     if cnt >= mn:
#         return
#     for di, dj, nd in ((0, 1, 1), (0, -1, 2), (1, 0, 3), (-1, 0, 4)):
#         ni = i + dj
#         nj = j + dj
#         if not arr[ni][nj]:
#             if d != nd:
#                 new_cnt = cnt + ref[d][nd]
#                 nm = 1
#             elif m != 3:
#                 new_cnt = cnt
#                 nm = m + 1
#             else:
#                 new_cnt = cnt + 1
#                 nm = 1
#             dfs(ni, nj, nd, new_cnt, nm)
#
#
# N, M = map(int, input().split())
# arr = [[1]*(M+2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + [[1]*(M+2)]
# si, sj, sd = map(int, input().split())
# ei, ej, ed = map(int, input().split())
#
# bfs()
# # mn = 20002
# # dfs(si, sj, sd, 0, 3)
# # print(mn)



