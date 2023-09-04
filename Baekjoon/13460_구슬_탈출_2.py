def tilt_board(arr, d, ri, rj, bi, bj):
    R, B = False, False
    r_move, b_move = 0, 0

    # decide the direction
    di, dj = 0, 0
    if d == 0:      # left
        di, dj = 0, -1
    elif d == 1:    # right
        di, dj = 0, 1
    elif d == 2:    # up
        di, dj = -1, 0
    else:           # down
        di, dj = 1, 0

    # tilt the board
    while arr[ri][rj] != '#':
        if arr[ri][rj] == 'O':
            R = True
        ri += di
        rj += dj
        r_move += 1
    while arr[bi][bj] != '#':
        if arr[bi][bj] == 'O':
            B = True
        bi += di
        bj += dj
        b_move += 1

    # adjust the position
    ri -= di
    rj -= dj
    bi -= di
    bj -= dj
    if ri == bi and rj == bj:
        if r_move > b_move:
            ri -= di
            rj -= dj
        else:
            bi -= di
            bj -= dj

    return ri, rj, bi, bj, R, B

def brute_force(N, n, arr, ri, rj, bi, bj, R, B):
    global answer

    # pruning
    if answer < n:
        return

    # end conditions
    if R and not B:
        answer = min(answer, n)
        return
    
    if B:
        return

    if N == n:
        return
    
    # traverse candidates
    for di in range(4):
        nri, nrj, nbi, nbj, R, B = tilt_board(arr, di, ri, rj, bi, bj)
        brute_force(N, n + 1, arr, nri, nrj, nbi, nbj, R, B)

if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # find the marbles' position
    ri, rj, bi, bj = 0, 0, 0, 0
    flag = 3
    for i in range(1, N):
        for j in range(1, M):
            if arr[i][j] == 'R':
                arr[i][j] = '.'
                ri, rj = i, j
                flag -= 1
                continue
            if arr[i][j] == 'B':
                arr[i][j] = '.'
                bi, bj = i, j
                flag -= 1
                continue
        if not flag:
            break

    # brute force
    answer = 11
    brute_force(10, 0, arr, ri, rj, bi, bj, False, False)

    # print answer
    print(answer if answer < 11 else -1)