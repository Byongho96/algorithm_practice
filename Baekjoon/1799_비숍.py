def backtracking(N, step, board, occupied_plus, occupied_minus, num_bishops):
    # 1. 종료 조건
    if step > N**2 - 1:
        return num_bishops
    
    # 2. 상태 공간 자식 노드 검색

    # 2.1. 다음 발판의 위치 탐색 (항상 +2가 아니기 때문에)
    i, j = divmod(step, N)
    next_step = step
    for _ in range(3):
        next_step += 1
        ni, nj = divmod(next_step, N)
        if (i + j) % 2 == (ni + nj) % 2:
            break
    # 2.2. 상태공간 탐색
    mx_1 = backtracking(N, next_step, board, occupied_plus, occupied_minus, num_bishops)    # 비숍을 놓지 않는 경우
    mx_2 = 0
    if board[i][j] and not((i + j) in occupied_plus or (i - j) in occupied_minus):
        occupied_plus.add(i + j)
        occupied_minus.add(i - j)
        mx_2 = backtracking(N, next_step, board, occupied_plus, occupied_minus, num_bishops + 1)    # 비숍을 놓는 경우
        occupied_plus.remove(i + j)     # 다음 자식 노드가 없더라도
        occupied_minus.remove(i - j)    # return 후 부모 노드에 영향주기 때문에 초기화 필요!

    return max(mx_1, mx_2)  # 최댓값을 반환

if __name__ == "__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 흰색발판과 검은색발판은 독립적인 사건으로 처리 가능
    # 시간복잡도: N^2 -> 2*(N/2)^2
    mx_1 = backtracking(N, 0, board, set(), set(), 0)   # 흰색 발판
    mx_2 = backtracking(N, 1, board, set(), set(), 0)   # 검은색 발판

    print(mx_1 + mx_2)































# # Python 612ms, Pypy 380ms
# import sys
# input = sys.stdin.readline

# def backtracking_black(n, cnt):
#     global mx_black
#     # 종료조건
#     if n == B:
#         mx_black = max(mx_black, cnt)
#         return
#     # 가지치기
#     if B - n + cnt <= mx_black: # 나머지 칸에 모두 비숍을 놓아도 최댓값을 못 넘는 경우
#         return
#     # 후보군 출력
#     i, j = black[n]
#     if not B1[i - j + N] and not B2[i + j]:
#         B1[i - j + N] = 1
#         B2[i + j] = 1
#         backtracking_black(n + 1, cnt + 1)
#         B1[i - j + N] = 0
#         B2[i + j] = 0
#     backtracking_black(n + 1, cnt)

# def backtracking_white(n, cnt):
#     global mx_white
#     # 종료조건
#     if n == W:
#         mx_white = max(mx_white, cnt)
#         return
#     # 가지치기
#     if W - n + cnt <= mx_white: # 나머지 칸에 모두 비숍을 놓아도 최댓값을 못 넘는 경우
#         return
#     # 후보군 출력
#     i, j = white[n]
#     if not B1[i - j + N] and not B2[i + j]:
#         B1[i - j + N] = 1
#         B2[i + j] = 1
#         backtracking_white(n + 1, cnt + 1)
#         B1[i - j + N] = 0
#         B2[i + j] = 0
#     backtracking_white(n + 1, cnt)


# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]

# white = []          # 비숍을 놓을 수 있는 흰색 좌표를 저장할 리스트
# black = []          # 비숍을 놓을 수 있는 검은색 좌표를 저장할 리스트
# for i in range(N):
#     for j in range(N):
#         if arr[i][j]:
#             if (i + j) % 2:
#                 black.append((i, j))
#             else:
#                 white.append((i, j))

# B1 = [0] * (2 * N + 1)  # 대각 방향 (i - j + N) 비숍을 체크할 리스트: -(N-1) ~ (N-1)
# B2 = [0] * (2 * N + 1)  # 대각 방향 (i + j) 비숍을 체크할 리스트: 0 ~ 2(N-1)

# # 흰색 좌표 백트래킹
# W = len(white)
# mx_white = 0
# backtracking_white(0, 0)

# # 검은색 좌표 백트래킹
# B = len(black)
# mx_black = 0
# backtracking_black(0, 0)

# # 흰색 좌표 최대 비숍 갯수 + 검은색 좌표 최대 비숍 갯수
# print(mx_white + mx_black)


# import time
# start = time.time()
# import sys
# input = sys.stdin.readline
#
# def backtracking(n, cnt):
#     # print(n, cnt)
#     global mx
#     # 종료조건
#     if n == 2 * N:
#         mx = max(mx, cnt)
#         return
#     # 가지치기
#     if 2 * N - n + cnt <= mx:
#         return
#     # 후보군 출력
#     if n < N:       # 좌측 상단
#         for i in range(n + 1):
#             for j in range(n, -1, -1):
#                 if arr[i][j] and not B1[i - j + N - 1] and not B2[i + j]:
#                     B1[i - j + N - 1] = 1
#                     B2[i + j] = 1
#                     backtracking(n + 1, cnt + 1)
#                     B1[i - j + N - 1] = 0
#                     B2[i + j] = 0
#         backtracking(n + 1, cnt)
#
#     else:           # 우측 하단
#         for i in range(n - N + 1, N):
#             for j in range(N - 1, n - N, -1):
#                 if arr[i][j] and not B1[i - j + N - 1] and not B2[i + j]:
#                     B1[i - j + N - 1] = 1
#                     B2[i + j] = 1
#                     backtracking(n + 1, cnt + 1)
#                     B1[i - j + N - 1] = 0
#                     B2[i + j] = 0
#         backtracking(n + 1, cnt)
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# mx = 0
# B1 = [0] * (2 * N - 1)
# B2 = [0] * (2 * N - 1)
# backtracking(0, 0)
# print(mx)
# print("time: ", time.time()-start)
#
