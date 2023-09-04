if __name__ == '__main__':
    string_1 = input()
    string_2 = input()
    S1 = len(string_1)
    S2 = len(string_2)

    # make DP
    DP = [[''] * (S1 + 1) for _ in range(2)]

    # fill DP
    for i in range(S2):
        target_char = string_2[i]
        i %= 2
        for j in range(S1):
            if string_1[j] == target_char:
                DP[i][j + 1] = DP[1 - i][j] + target_char
            elif len(DP[i][j]) > len(DP[1 - i][j + 1]):
                DP[i][j + 1] = DP[i][j]
            else:
                DP[i][j + 1] = DP[1 - i][j + 1]

    mx = DP[1 - S2 % 2][-1]
    M = len(mx)
    print(M)
    if M:
        print(mx)
