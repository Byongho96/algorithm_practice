import sys

input = sys.stdin.readline


def main():
    N, M, K = map(int, input().split())

    # Always true
    if M < 2:
        print("YES")
        return

    stones = [0] + list(map(int, input().split()))

    # Connect all the buildings
    nxt = [i + 1 for i in range(N + 1)]
    nxt[N] = 1  # last -> first

    # Disconnect buildings
    n1, n2 = 0, 0
    for _ in range(M):
        x, y = map(int, input().split())
        n1, n2 = min(x, y), max(x, y)
        if n1 == 1 and n2 == N:
            nxt[n2] = n2
        else:
            nxt[n1] = n1

    # Solution
    required = 0
    visited = 0
    cur = n1 if n1 == 1 and n2 == N else n2

    group_min = 1000000
    while visited < N:
        # visit building
        group_min = min(group_min, stones[cur])
        visited += 1
        # next building
        if nxt[cur] != cur:
            cur = nxt[cur]
            continue
        # end of a group
        required += group_min
        group_min = 1000000
        if cur == N:
            cur = 1
        else:
            cur += 1

    print("YES" if required < K + 1 else "NO")


if __name__ == "__main__":
    main()
