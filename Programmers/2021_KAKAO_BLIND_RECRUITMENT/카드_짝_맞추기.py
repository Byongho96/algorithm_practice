from itertools import permutations
from collections import deque


DIRECTION = ((-1, 0), (0, 1), (1, 0), (0, -1))


def bfs(board, si, sj, ei, ej):
    visited = [[0] * 4 for _ in range(4)]
    queue = deque()

    visited[si][sj] = 1
    queue.append((si, sj))

    while queue:
        i, j = queue.popleft()

        # visit the node
        cnt = visited[i][j]
        if i == ei and j == ej:
            return cnt - 1

        # traverse
        for d in range(4):
            di, dj = DIRECTION[d]

            # without ctrl
            ni, nj = i + di, j + dj
            if -1 < ni < 4 and -1 < nj < 4 and not visited[ni][nj]:
                visited[ni][nj] = cnt + 1
                queue.append((ni, nj))

            # with ctrl
            ni, nj = i + di, j + dj
            while -1 < ni < 4 and -1 < nj < 4 and not board[ni][nj]:
                ni, nj = ni + di, nj + dj
            if ni < 0 or ni > 3 or nj < 0 or nj > 3:
                ni, nj = ni - di, nj - dj
            if not visited[ni][nj]:
                visited[ni][nj] = cnt + 1
                queue.append((ni, nj))


def cal_total_min_dis(board, N, n, order, weight, isEven):
    global answer
    global card_type

    # pruning
    if weight > answer - 1:
        return

    # find pair card
    cur_card_type = order[n]
    ci, cj = card_type[2 * cur_card_type - 2 + isEven]
    pi, pj = card_type[2 * cur_card_type - 2 + 1 - isEven]
    new_weight = weight + bfs(board, ci, cj, pi, pj)

    # pruning
    if new_weight > answer - 1:
        return

    # end condition
    if n == N - 1:
        answer = min(answer, new_weight)
        return

    board[ci][cj] = 0
    board[pi][pj] = 0

    # next card
    next_card = card_type[2 * order[n + 1] - 2]
    cal_total_min_dis(board, N, n + 1, order, new_weight + bfs(board, pi, pj, *next_card), 0)
    next_card = card_type[2 * order[n + 1] - 1]
    cal_total_min_dis(board, N, n + 1, order, new_weight + bfs(board, pi, pj, *next_card), 1)

    # return the board
    board[ci][cj] = cur_card_type
    board[pi][pj] = cur_card_type


def solution(board, r, c):
    global answer
    global card_type

    # make card_type array
    card_type = [None] * 12
    cards = set()
    for i in range(4):
        for j in range(4):
            card = board[i][j]
            if not card:
                continue
            if not card_type[2 * card - 2]:
                card_type[2 * card - 2] = (i, j)
            else:
                card_type[2 * card - 1] = (i, j)
            cards.add(card)

    answer = 8 * 6
    N = len(cards)
    for perm in permutations(cards):
        first_card_type = perm[0]

        fi, fj = card_type[2 * first_card_type - 2]
        weight = bfs(board, r, c, fi, fj)
        cal_total_min_dis(board, N, 0, perm, weight, 0)

        fi, fj = card_type[2 * first_card_type - 1]
        weight = bfs(board, r, c, fi, fj)
        cal_total_min_dis(board, N, 0, perm, weight, 1)

    answer = answer + 2 * N
    return answer
