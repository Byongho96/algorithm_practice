# DFS로 십자 모양 갈라지는 탐색이 어렵다

from itertools import combinations


def is_som(arr, seats):
    som = 0

    for seat in seats:
        i, j = divmod(seat, 5)
        if arr[i][j] == "S":
            som += 1

    return som > 3


DIRECTION = ((1, 0), (0, 1), (-1, 0), (0, -1))


def is_connected(seats):
    visited = [False] * 25
    stack = [seats[0]]

    num = 0
    while stack:
        seat = stack.pop()

        # filter invalid
        if visited[seat]:
            continue

        # visited the node
        visited[seat] = True
        num += 1

        # traverse adjcents
        i, j = divmod(seat, 5)
        for di, dj in DIRECTION:
            ni = i + di
            nj = j + dj
            if ni < 0 or ni > 4 or nj < 0 or nj > 4:
                continue
            new_seat = 5 * ni + nj
            if new_seat in seats and not visited[new_seat]:
                stack.append(new_seat)

    return num == 7


if __name__ == "__main__":
    arr = [list(input()) for _ in range(5)]
    answer = 0

    for comb in combinations(range(25), 7):
        if not is_som(arr, comb):
            continue
        if not is_connected(comb):
            continue
        answer += 1

    print(answer)
