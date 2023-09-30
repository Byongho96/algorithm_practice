if __name__ == "__main__":
    N = int(input())
    ns = list(map(int, input().split()))

    # c[0]: left counter
    # c[1]: right counter
    c = [[0] * 30001 for _ in range(2)]

    # fill the right counter
    for n in ns:
        c[1][n] += 1

    # count the number of sequence
    ans = 0
    for m in ns:
        c[1][m] -= 1
        M = m if m < 15001 else 30001 - m
        for d in range(-M + 1, M):
            ans += c[0][m - d] * c[1][m + d]
        c[0][m] += 1

    print(ans)
