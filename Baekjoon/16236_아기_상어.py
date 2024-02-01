import sys
from typing import List, Tuple
from collections import deque

input = sys.stdin.readline

DIRECTION = ((1, 0), (0, 1), (-1, 0), (0, -1))


# BFS
def eat_fish(N, arr, size, si, sj) -> Tuple[int, int] | bool:
    queue = deque()
    visited = [[False] * N for _ in range(N)]

    # set the start
    queue.append((si, sj))
    visited[si][sj] = 1
    arr[si][sj] = 0

    # run bfs
    shortest = N**2 + 1
    fi, fj = N, N
    while queue:
        i, j = queue.popleft()

        # early end condition
        if visited[i][j] > shortest:
            break

        # eat fish
        if arr[i][j] and arr[i][j] < size:
            # find the same minimum distance fish
            if visited[i][j] == shortest:
                if i < fi:
                    fi, fj = i, j
                elif i == fi and j < fj:
                    fi, fj = i, j

            # find the minimum distance fish
            else:
                shortest = visited[i][j]
                fi, fj = i, j

        # traverse adjacent nodes
        for di, dj in DIRECTION:
            ni = i + di
            nj = j + dj
            if (
                -1 < ni < N
                and -1 < nj < N
                and not visited[ni][nj]
                and arr[ni][nj] < size + 1
            ):
                visited[ni][nj] = visited[i][j] + 1
                queue.append((ni, nj))

    # can't eat fish
    if shortest == N**2 + 1:
        return False

    # move shark
    arr[fi][fj] = 9

    # return moved position
    return (shortest - 1, fi, fj)


def main(N: int, arr: List[List[int]]) -> int:
    # find the start point
    si, sj = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                si, sj = i, j
                break
        else:
            continue
        break

    # simulate
    time = 0
    size, hp = 2, 0
    while True:
        result = eat_fish(N, arr, size, si, sj)

        # call mom
        if not result:
            break

        t, si, sj = result

        # grow up
        hp += 1
        if hp == size:
            size += 1
            hp = 0

        # update data
        time += t

    # return the answer
    return time


if __name__ == "__main__":
    # get inputs
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # run function
    answer = main(N, arr)
    print(answer)
