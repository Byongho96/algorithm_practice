import sys

input = sys.stdin.readline
INF = sys.maxsize


def floyd(V, arr):
    for m in range(1, V + 1):
        for i in range(1, V + 1):
            if arr[i][m] == INF:
                continue
            for j in range(1, V + 1):
                if arr[i][j] > arr[i][m] + arr[m][j]:
                    arr[i][j] = arr[i][m] + arr[m][j]


if __name__ == "__main__":
    V, E = map(int, input().split())
    arr = [[INF] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        i, j, w = map(int, input().split())
        arr[i][j] = w

    # Run Floyd
    floyd(V, arr)

    # Get the answer
    ans = INF
    for i in range(1, V + 1):
        ans = min(ans, arr[i][i])

    print(-1 if ans == INF else ans)
