from collections import deque

DIRECTION = ((1, 0, "D"), (0, 1, "R"), (-1, 0, "U"), (0, -1, "L"))


def move_marbles(d, arr, red, blue, hole):
    di, dj, _ = DIRECTION[d]
    ri, rj = red
    bi, bj = blue
    hi, hj = hole

    # move marbles
    r_move = -1
    r_escaped = False
    while arr[ri][rj] != "#":
        ri += di
        rj += dj
        r_move += 1
        if ri == hi and rj == hj:
            r_escaped = True
    ri -= di
    rj -= dj

    b_move = -1
    b_escaped = False
    while arr[bi][bj] != "#":
        bi += di
        bj += dj
        b_move += 1
        if bi == hi and bj == hj:
            b_escaped = True
    bi -= di
    bj -= dj

    # adjust poistion
    if ri == bi and rj == bj:
        if r_move > b_move:
            ri -= di
            rj -= dj
        else:
            bi -= di
            bj -= dj

    # is escaped
    is_escaped = False
    if r_escaped and not b_escaped:
        is_escaped = True

    # is posible
    is_possible = True
    if b_escaped or not (r_move or b_move):
        is_possible = False

    return (ri, rj), (bi, bj), is_escaped, is_possible


def bfs(arr, red, blue, hole):
    queue = deque()
    queue.append((0, red, blue, False, ""))

    while queue:
        n, red, blue, is_escaped, path = queue.popleft()

        # end condition
        if is_escaped:
            return n, path

        # end condition
        if n == 11:
            return (-1,)

        # traverse candidates:
        for d in range(4):
            new_red, new_blue, is_escaped, is_possible = move_marbles(d, arr, red, blue, hole)
            if not is_possible:
                continue
            queue.append((n + 1, new_red, new_blue, is_escaped, path + DIRECTION[d][2]))


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # find the positions
    red = blue = hole = None
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            var = arr[i][j]
            if var == "." or var == "#":
                pass
            elif var == "R":
                red = (i, j)
            elif var == "B":
                blue = (i, j)
            else:
                hole = (i, j)

    # run bfs
    answer = bfs(arr, red, blue, hole)
    print(*answer, sep="\n")
