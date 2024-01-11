def solution(board, skill):
    N, M = len(board), len(board[0])
    diff = [[0] * (M + 1) for _ in range(N + 1)]

    # mark the skill range
    for t, si, sj, ei, ej, degree in skill:
        # if attack
        if t == 1:
            degree *= -1
        diff[si][sj] += degree
        diff[si][ej + 1] -= degree
        diff[ei + 1][sj] -= degree
        diff[ei + 1][ej + 1] += degree

    # row-direction culmulative sum
    for i in range(N):
        for j in range(1, M):
            diff[i][j] += diff[i][j - 1]

    # column-direction culmulative sum
    for j in range(M):
        for i in range(1, N):
            diff[i][j] += diff[i - 1][j]

    # result
    answer = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] + diff[i][j] > 0:
                answer += 1

    return answer
