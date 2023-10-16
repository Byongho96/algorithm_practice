import sys

input = sys.stdin.readline


def DP(N, pages):
    DP = [[0] * N for _ in range(N)]

    # init prefix sum array
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + pages[i - 1]

    # fill DP from the low size(diff from start to end)
    for size in range(1, N):
        for start in range(N - size):
            end = start + size
            mn = float("inf")
            for mid in range(start, end):
                result = DP[start][mid] + DP[mid + 1][end]
                if result < mn:
                    mn = result
            DP[start][end] = mn + prefix_sum[end + 1] - prefix_sum[start]

    return DP[0][N - 1]


if __name__ == "__main__":
    T = int(input())
    answers = [0] * T

    for t in range(T):
        N = int(input())
        pages = [*map(int, input().split())]
        answers[t] = DP(N, pages)

    print(*answers, sep="\n")


# import sys

# input = sys.stdin.readline


# def calculate_the_min_cost(start, end) -> int:
#     """calculate the minimum merging cost with Top-down memoization"""
#     # use memoization
#     if memo[start][end] != -1:
#         return memo[start][end]

#     # fill the DP
#     min_cost = sys.maxsize
#     for mid in range(start, end):
#         result = calculate_the_min_cost(start, mid) + calculate_the_min_cost(mid + 1, end)
#         if result < min_cost:
#             min_cost = result

#     # save DP
#     memo[start][end] = min_cost + prefix_sum[end + 1] - prefix_sum[start]
#     return memo[start][end]


# if __name__ == "__main__":
#     T = int(input())
#     answers = [0] * T

#     for t in range(T):
#         N = int(input())
#         pages = list(map(int, input().split()))

#         # make prefix sum array for time efficiency
#         prefix_sum = [0] * (N + 1)
#         for i in range(1, N + 1):
#             prefix_sum[i] = prefix_sum[i - 1] + pages[i - 1]

#         # make memoization
#         memo = [[-1] * N for _ in range(N)]
#         for n in range(N):
#             memo[n][n] = 0

#         answers[t] = calculate_the_min_cost(0, N - 1)

#     print(*answers, sep="\n")
