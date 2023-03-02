from collections import deque

def bfs(N, M, T):
    q = deque()
    visited = [[0] * M for _ in range(N)]

    q.append((0, 0))
    visited[0][0] = 1

    sword_time = N * M
    while q:
        i, j= q.popleft()
        t = visited[i][j]
        # 종료 조건
        if i == N - 1 and j == M - 1:
            return min(t - 1, sword_time)
        # 가지 치기
        if t > T:
            return t
        if t > sword_time:
            return sword_time
        # bfs
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                visited[ni][nj] = t + 1
                if arr[ni][nj] == 0:
                    q.append((ni, nj))
                    continue
                if arr[ni][nj] == 2:
                    sword_time = t + (N - 1 - ni) + (M - 1 - nj)
                    continue    

    return sword_time # 정석적인 방법으로 도착하지 못한 경우

if __name__ == '__main__':
    # 입력
    N, M, T = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # bfs 결과
    answer = bfs(N, M, T)

    if answer > T or answer >= N * M:
        print('Fail')
    else:
        print(answer)



# from collections import deque
# import sys
# input = sys.stdin.readline

# # 96ms
# def bfs(i, j):
#     visited = [[0] * M for _ in range(N)]
#     q = deque()

#     visited[i][j] = 1
#     q.append((i, j))

#     sword = N * M
#     princess = N * M
#     while q:
#         i, j = q.popleft()
#         if arr[i][j] == 2:
#             sword = visited[i][j]-1 + N-1-i + M-1-j
#         if i == N - 1 and j == M - 1:
#             princess = visited[i][j] - 1
#         for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
#             ni = i + di
#             nj = j + dj
#             if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] != 1:
#                 visited[ni][nj] = visited[i][j] + 1
#                 q.append((ni, nj))
#     # 검과 공주 둘다한테 못갈 수도 있음!!
#     return min(sword, princess)


# N, M, T = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# result = bfs(0, 0)
# if result == M*N:
#     print('Fail')
# elif result <= T:
#     print(result)
# else:
#     print('Fail')

