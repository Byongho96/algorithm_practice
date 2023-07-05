from collections import deque

dir_i = (1, 0, 0, -1)
dir_j = (0, 1, -1, 0)

def bfs():
    INF = N * M + 1
    distance= [[[INF] * 2 for _ in range(M + 2)] for _ in range(N + 2)] # 벽을 부순 경우와 안 부순 경우, 높이 2차원
    queue = deque()

    distance[1][1][0] = 1   # 초깃값 설정
    queue.append((1, 1, 0)) # 초기노드 주입

    while queue:
        i, j, isBroken = queue.popleft()

        # 종료조건
        if i == N and j == M:
            return distance[i][j][isBroken]

        # 인접 노드 탐색
        new_distance = distance[i][j][isBroken] + 1
        for idx in range(4):
            ni = i + dir_i[idx]
            nj = j + dir_j[idx]
            if arr[ni][nj] == 0 and distance[ni][nj][isBroken] > new_distance:  # 벽이 없을 때
                distance[ni][nj][isBroken] = new_distance
                queue.append((ni, nj, isBroken))
            if not isBroken and arr[ni][nj] == 1 and distance[ni][nj][1] > new_distance:    # 벽이 있고, 부술 수 있을 때
                distance[ni][nj][1] = new_distance
                queue.append((ni, nj, 1))
    return -1

if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = [[2] * (M + 2)] + [[2] + list(map(int, input())) + [2] for _ in range(N)] + [[2] * (M + 2)]   # 둘레로 2로 감쌈

    answer = bfs()
    print(answer)




# from pprint import pprint
# from collections import deque
# import sys
# input = sys.stdin.readline

# def bfs(k, i, j):
#     visited = [[[0] * M for _ in range(N)] for _ in range(2)]
#     q = deque()

#     visited[k][i][j] = 1
#     q.append((k, i, j))

#     while q:
#         k, i, j = q.popleft()
#         if i == N-1 and j == M-1:
#             return visited[k][i][j]
#         for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
#             ni = i + di
#             nj = j + dj
#             if 0 <= ni < N and 0 <= nj < M:
#                 if not arr[ni][nj] and not visited[k][ni][nj]:         # 벽이 없다면
#                     q.append((k, ni, nj))
#                     visited[k][ni][nj] = visited[k][i][j] + 1
#                 if not k and arr[ni][nj] and not visited[k+1][ni][nj]:   # 벽이 있고, 부술 수 있다면
#                     q.append((k+1, ni, nj))
#                     visited[k+1][ni][nj] = visited[k][i][j] + 1
#     return -1

# N, M = map(int, input().split())
# arr = [list(map(int, input().rstrip())) for _ in range(N)]

# print(bfs(0, 0, 0))