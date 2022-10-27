import sys
input = sys.stdin.readline

# 1. 배열복사는 하지 않기!!
# 2. in 탐색을 할 경우, set으로 하기(프로그래머스)
# 3. for문은 최대한 줄이기

ref = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4:(-1, 1), 5:(0, 1), 6:(1, 1), 7:(1, 0), 8:(1, -1)}

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
d = [0] * M
s = [0] * M
for i in range(M):
    d[i], s[i] = map(int, input().split())

# 구름 생성
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for m in range(M):
    # 이동 후 비내리기
    moved_clouds = set()
    for i, j in clouds:
        mi = (i + s[m] * ref[d[m]][0]) % N
        mj = (j + s[m] * ref[d[m]][1]) % N
        arr[mi][mj] += 1
        moved_clouds.add((mi, mj))

    # 물복사 버그
    for ci, cj in moved_clouds:
        for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]:
                arr[ci][cj] += 1

    # 구름 생성
    clouds = []
    for i in range(N):
        for j in range(N):
            if (i, j) not in moved_clouds and arr[i][j] >= 2:
                arr[i][j] -= 2
                clouds.append((i, j))

    # print(arr)
    # print(next_clouds)

result = 0
for row in arr:
    result += sum(row)
print(result)

# import sys
# input = sys.stdin.readline
#
# ref = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4:(-1, 1), 5:(0, 1), 6:(1, 1), 7:(1, 0), 8:(1, -1)}
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# d = [0] * M
# s = [0] * M
# for i in range(M):
#     d[i], s[i] = map(int, input().split())
#
# # 구름 생성
# clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
# for m in range(M):
#     # 이동
#     for cloud in clouds:
#         cloud[0] = (cloud[0] + s[m] * ref[d[m]][0]) % N
#         cloud[1] = (cloud[1] + s[m] * ref[d[m]][1]) % N
#
#     # 비 내리기
#     for ci, cj in clouds:
#         arr[ci][cj] += 1
#
#     # 물복사 버그
#     for ci, cj in clouds:
#         for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
#             ni = ci + di
#             nj = cj + dj
#             if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]:
#                 arr[ci][cj] += 1
#
#     # 구름 생성
#     next_clouds = []
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] >= 2 and [i, j] not in clouds:
#                 arr[i][j] -= 2
#                 next_clouds.append([i, j])
#
#     # print(arr)
#     # print(next_clouds)
#     clouds = next_clouds
#
# result = 0
# for row in arr:
#     result += sum(row)
# print(result)