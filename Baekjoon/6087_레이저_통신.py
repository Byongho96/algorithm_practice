from collections import deque

direction = ((0, 1), (1, 0), (0, -1),  (-1, 0))

def count_the_minimum_mirrors(arr, start, end):
    si, sj  = start
    ei, ej = end
    queue = deque()
    visited = [[0] * (N + 2) for _ in range(M +2)]

    # set the start point
    queue.append((si, sj))
    visited[si][sj] = 1

    # bfs
    while queue:
        i, j = queue.popleft()

        # end condition
        cur_mirror = visited[i][j]
        if i == ei and j == ej:
            return  cur_mirror - 2
        
        # insert every nodes in one line
        new_mirror =  cur_mirror + 1
        for idx in range(4):
            ni, nj = i, j
            di, dj  = direction[idx]
            while (arr[ni][nj] == '.' or arr[ni][nj] == 'C'):
                ni += di
                nj += dj
                if visited[ni][nj]:
                    continue
                visited[ni][nj] = new_mirror
                queue.append((ni,  nj))


if __name__ == '__main__':
    # N: columns, M: row
    N, M = map(int, input().split())
    arr = [[0] * (N + 2)] + [[0] + list(input()) + [0] for _ in range(M)] + [[0] * (N + 2)]

    # find the laser points
    C = []
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if arr[i][j] == 'C':
                C.append((i, j))

    # bfs based on the turning points
    answer = count_the_minimum_mirrors(arr, C[0], C[1])
    print(answer)