import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    memories = [0] + list(map(int, input().split()))
    costs = [0] + list(map(int, input().split()))
    C = sum(costs)

    # DP[i][j] : j번째 앱까지 i의 cost로 만들 수 있는 최대 바이트
    DP = [[0] * (N + 1) for _ in range(C + 1)]
    for i in range(1, C + 1):
        for j in range(1, N + 1):
            DP[i][j] = max(DP[i][j - 1], 0 if i - costs[j] < 0 else DP[i - costs[j]][j - 1] + memories[j])
            if DP[i][j] > M - 1:
                print(i)
                exit()
