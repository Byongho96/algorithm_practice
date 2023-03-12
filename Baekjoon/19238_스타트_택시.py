from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline

# 손님 선택하는 bfs
# 탐색순서 위->왼->오->아래로는 충분하지 않음!! 직접 2step까지 그려보기
def bfs_find_customer(ti, tj):
    q = deque()
    visited = [[0] * (N+2) for _ in range(N + 2)]

    q.append((ti, tj))
    visited[ti][tj] = 1

    customer_lst = []
    while q:
        i, j = q.popleft()
        if (i, j) in customer:
            customer_lst.append((visited[i][j] - 1, i, j))
        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ni = i + di
            nj = j + dj
            if arr[ni][nj] != 1 and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

    # 탐색을 위->왼->오->아래로 하면, 반례발생
    # 예를 들어, "왼->아래" 가 "오->오"보다 먼저 탐색
    # (거리, 행, 렬) 오름차순 정렬
    if customer_lst:
        customer_lst.sort()
        return customer_lst[0]
    return -1, 0, 0

# 손님을 목적지까지 bfs
def bfs_to_destination(ci, cj, ei, ej):
    q = deque()
    visited = [[0] * (N + 2) for _ in range(N + 2)]

    q.append((ci, cj))
    visited[ci][cj] = 1

    while q:
        i, j = q.popleft()
        if i == ei and j == ej:
            return visited[i][j] - 1
        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ni = i + di
            nj = j + dj
            if arr[ni][nj] != 1 and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return -1

N, M, oil  = map(int, input().rstrip().split())

# 1로 둘러싸서 받으면, 이후 택시랑 손님의 좌표 모두 그대로 쓸 수 있고, bfs에서 조건문도 줄어듬
arr = [[1] * (N + 2)] + [[1] + list(map(int, input().rstrip().split())) + [1] for _ in range(N)] + [[1] * (N + 2)]

ti, tj = map(int, input().rstrip().split())

customer = {}               # 딕셔너리 형성 { 손님 좌표 튜플 : 목적지 좌표 튜플 }
for _ in range(M):
    ci, cj, di, dj = map(int, input().rstrip().split())
    customer[(ci, cj)] = (di, dj)

for _ in range(M):          # M명의 손님을 바래다 줌
    dis_customer, ci, cj = bfs_find_customer(ti, tj)
    if dis_customer < 0:        # 손님에게 접근할 수 없는 경우
        print(-1)
        break
    elif dis_customer > oil:    # 손님이 연료량보다 멀리 있을 경우
        print(-1)
        break

    oil -= dis_customer         # 손님 태운 뒤의 연료량 업데이트
    di, dj = customer[ci, cj]   # 목적지 설정
    del customer[ci, cj]        # 태운 손님은 태울 손님 목록에서 삭제

    dis_destination = bfs_to_destination(ci, cj, di, dj)
    if dis_destination < 0:     # 목적지에 갈 수 없을 경우
        print(-1)
        break
    elif dis_destination > oil: # 목적지가 연료량보다 멀리 있을 경우
        print(-1)
        break

    oil += dis_destination      # 손님 바래다주고 연료량 업데이트
    ti, tj = di, dj             # 다음 for문을 위해 택시위치 업데이트

else:                       # 모든 손님을 무사히 바래다 준 경우에만, 연료량 출력
    print(oil)



