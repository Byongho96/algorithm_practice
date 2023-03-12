from itertools import accumulate

# 때로는 직관적으로
import sys
N = int(sys.stdin.readline())
total, cnt, minus = 0, 0, 1

for i in range(1, N+1):  # 1부터 N까지 반복한다. i = 1, 2, 3, 4, 5, 6...
    total += i           # total에 i를 더한다. total = 1, 3, 6, 10, 15, 21 ...
    while total > N:     # 만약 total이 N보다 커지면
        total -= minus   # 1부터 앞에서 더해진 숫자를 N보다 작거나 같을 때까지 뺀다.
        minus += 1       # total = 21이면 total = 20, 18, 15 (minus = 1, 2, 3 ...)
    if total == N:
        cnt += 1
print(cnt)

# # 메모리초과
# N = int(input())
#
# if N == 1 or N == 2:    # N==2 or 1일 경우, 아래코드로 돌릴시 2가 나옴
#     print(1)
#
# else:
#     cnt = 0
#     sum_lst = list(accumulate(range(1, N//2 + 2))) # 5 -> [1, 3, 6, 10]
#     for i in range(1, N//2 + 2):
#         for j in range(i-1, -1, -1):
#             sm = sum_lst[i] - sum_lst[j]
#             if sm == N:
#                 cnt += 1
#                 break
#             elif sm > N:
#                 break



# # Python3 시간초과, PyPy 348ms
# N = int(input())
#
# cnt = 0
#
# if N == 1 or N == 2:    # N==2 or 1일 경우, 아래코드로 돌릴시 2가 나옴
#     print(1)
#
# else:
#     for i in range(1, N//2 + 2):       # 1부터 N//2-1까지 자연수 시작지점 순회
#         sm = 0
#         for j in range(i, N//2 + 2):   # i부터 N//2-1까지 더하다가 N과 같하지면 cnt++
#             sm += j
#             if sm == N:
#                 cnt += 1
#                 break
#             elif sm > N:        # 합이 N보다 커질경우 break하고 다음 시작지점
#                 break
#
#     print(cnt + 1)  # N을 입력했을 때, N일 경우 출력