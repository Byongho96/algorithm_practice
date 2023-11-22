import sys

input = sys.stdin.readline


def calculate_the_max(N, M, K, money):
    # Edge case
    if N == M:
        return 1 if sum(money) < K else 0

    # Double the list for considering a cylce
    money += money

    # Run two pointer
    s, e = 0, M - 1
    cases = 0
    stolen = sum(money[:M])
    for _ in range(N):
        # Satisfied
        if stolen < K:
            cases += 1

        # Move the pointer
        stolen -= money[s]
        s += 1
        e += 1
        stolen += money[e]

    return cases


if __name__ == "__main__":
    for _ in range(int(input())):
        N, M, K = map(int, input().split())
        money = list(map(int, input().split()))

        print(calculate_the_max(N, M, K, money))
