import sys

input = sys.stdin.readline

DIRECTIION = ((1, 0), (0, 1), (-1, 0), (0, -1))


# melt cheese with dfs
def melt_cheese(N, M, arr, visited, stack):
    melted_cheese = 0
    melted_points = []
    while stack:
        i, j = stack.pop()
        for di, dj in DIRECTIION:
            ni = i + di
            nj = j + dj
            if -1 < ni < N and -1 < nj < M and not visited[ni][nj]:
                visited[ni][nj] = True
                # melted cheese
                if arr[ni][nj]:
                    arr[ni][nj] = 0
                    melted_cheese += 1
                    melted_points.append((ni, nj))
                # empty area
                else:
                    stack.append((ni, nj))

    return melted_cheese, melted_points


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # count cheese
    cheese = 0
    for row in arr:
        cheese += sum(row)

    # simulate
    time = 0
    melted_cheese = 0
    start_points = [(0, 0)]
    visited = [[False] * M for _ in range(N)]
    while cheese:
        time += 1
        melted_cheese, start_points = melt_cheese(N, M, arr, visited, start_points)
        cheese -= melted_cheese

    print(time, melted_cheese, sep="\n")
