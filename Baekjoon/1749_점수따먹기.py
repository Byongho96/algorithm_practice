import sys

input = sys.stdin.readline


def find_the_sub_matrix(N, M, arr):
    sm = [[0] * (M + 1) for _ in range(N + 1)]

    # make cumulative sum array
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            sm[i][j] = arr[i][j] + sm[i][j - 1] + sm[i - 1][j] - sm[i - 1][j - 1]

    # brute-force
    answer = -10000 * N * M
    for i1 in range(1, N + 1):
        for j1 in range(1, M + 1):
            for i2 in range(i1):
                for j2 in range(j1):
                    answer = max(answer, sm[i1][j1] - sm[i1][j2] - sm[i2][j1] + sm[i2][j2])

    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    answer = find_the_sub_matrix(N, M, arr)
    print(answer)
