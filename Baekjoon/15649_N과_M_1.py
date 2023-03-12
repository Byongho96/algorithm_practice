N, M = map(int,  input().split())

lst = [0] * M
visited = [0] * (N + 1)

def backtracking(n):
    # 후보 조건
    if n == M:
        print(*lst)
        return
    # 가지치기

    # 후보군
    for num in range(1, N + 1):
        if not visited[num]:
            lst[n] = num
            visited[num] = 1
            backtracking(n + 1)
            visited[num] = 0

backtracking(0)


# import sys
# input = sys.stdin.readline

# N, M = map(int, input().rstrip().split())

# ## Backracking_recursive
# def Backtracking_recursive(m, in_perm):
#     global result
#     # 종료조건
#     if m == M + 1:
#         result.append(in_perm)
#         return
#     # 가지치기
#     # 후보군 선택
#     for i in range(1, N+1):
#         if i not in in_perm:
#             Backtracking_recursive(m+1, in_perm + [i])

# in_perm = []
# result = []
# Backtracking_recursive(1, in_perm)

# for ele in result:
#     print(*ele)

############################################################
