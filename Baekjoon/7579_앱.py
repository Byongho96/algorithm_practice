import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    memories = [0] + list(map(int, input().split()))
    costs = [0] + list(map(int, input().split()))
    C = sum(costs)

    # 1D DP
    DP = [0] * (C + 1)

    # Knapsack
    answer = C
    for i in range(1, N + 1):
        for j in range(C, costs[i] - 1, -1):
            DP[j] = max(DP[j], DP[j - costs[i]] + memories[i])
            if DP[j] > M - 1 and j < answer:
                answer = j

    print(answer)
