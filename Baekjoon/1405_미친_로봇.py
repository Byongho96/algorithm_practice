import sys
input = sys.stdin.readline

DIRECTION = ((0, 1), (0, -1), (1, 0), (-1, 0))

sm_prob = 0
direction_prob = [0] * 4
visited = [[0] * (2 * 14 + 1) for _ in range(2 * 14 + 1)]

def backtracking(N, n, cur, cur_prob):
    global sm_prob

    if n == N:
        sm_prob += cur_prob
        return
    
    for i in range(4):
        di, dj  = DIRECTION[i]
        d = direction_prob[i]

        if not d:
            continue

        cur[0] += di
        cur[1] += dj

        if not visited[cur[0]][cur[1]]:
            visited[cur[0]][cur[1]] = 1
            backtracking(N, n + 1, cur, cur_prob * d)
            visited[cur[0]][cur[1]] = 0

        cur[0] -= di
        cur[1] -= dj

    return

def init(N, E, W, S, D):
    global sm_prob

    sm_prob = 0
    direction_prob[0] = E / 100
    direction_prob[1] = W / 100
    direction_prob[2] = S / 100
    direction_prob[3] = D / 100
    for i in range(2 * N + 1):
        for j in range(2 * N + 1):
            visited[i][j] = 0


def solution(N, E, W, S, D):
    init(N, E, W, S, D)

    visited[N][N] = 1
    cur = [N, N]

    backtracking(N, 0, cur, 1)
    return sm_prob

if __name__ == "__main__":
    N, E, W, S, D = map(int, input().split())

    answer = solution(N, E, W, S, D)
    print(answer)
