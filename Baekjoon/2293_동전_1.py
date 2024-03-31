import sys
from typing import List

input = sys.stdin.readline

def solution(N: int, K: int, coins: List[int]) -> int:
    DP = [0] * (K + 1)
    DP[0] = 1

    for value in coins:
        for k in range(value, K + 1):
            DP[k] += DP[k - value]

    return DP[K]


if __name__== "__main__":
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]

    answer = solution(N, K, coins)
    print(answer)