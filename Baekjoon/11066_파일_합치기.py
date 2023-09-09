from typing import List

import sys

input = sys.stdin.readline


def calculate_the_min_cost(memo: List[List[int]], pages: List[int], start: int, end: int) -> int:
    """calculate the minimum merging cost with Top-down memoization"""
    # use memoization
    if memo[start][end] != -1:
        return memo[start][end]

    # base condition
    if start == end:
        return 0

    # fill the DP
    min_cost = 0
    for division in range(start, end):
        result = calculate_the_min_cost(memo, pages, start, division) + calculate_the_min_cost(
            memo, pages, division + 1, end
        )
        if result < min_cost or not min_cost:
            min_cost = result

    # save DP
    memo[start][end] = min_cost + sum(pages[start : end + 1])
    return memo[start][end]


def main():
    """main function"""
    N = int(input())
    pages = list(map(int, input().split()))

    # make memoization
    memo = [[-1] * N for _ in range(N)]

    answer = calculate_the_min_cost(memo, pages, 0, N - 1)
    return answer


if __name__ == "__main__":
    T = int(input())

    answers = []
    for _ in range(T):
        answers.append(main())

    print(*answers, sep="\n")
