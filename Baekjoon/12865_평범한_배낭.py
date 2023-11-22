import sys

input = sys.stdin.readline


def DP(N, MAX_WEIGHT, weights, values):
    # 행 : 가방의 최대 무게 / 열: i번째 물건
    # DP[i][j] : 무게가 i인 가방에 j번째 물건가지 고려했을 때, 최대로 넣을 수 있는 가치
    DP = [[0] * (N + 1) for _ in range(MAX_WEIGHT + 1)]

    for max_weight in range(1, MAX_WEIGHT + 1):
        for n in range(1, N + 1):
            weight = weights[n]
            value = values[n]

            if max_weight < weight:
                DP[max_weight][n] = DP[max_weight][n - 1]
            else:
                DP[max_weight][n] = max(
                    DP[max_weight - weight][n - 1] + value, DP[max_weight][n - 1]
                )

    return DP[-1][-1]


if __name__ == "__main__":
    N, MAX_WEIGHT = map(int, input().split())

    weights = [0] * (N + 1)
    values = [0] * (N + 1)
    for i in range(1, N + 1):
        weights[i], values[i] = map(int, input().split())

    answer = DP(N, MAX_WEIGHT, weights, values)
    print(answer)
