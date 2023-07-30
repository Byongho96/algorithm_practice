if __name__ == '__main__':
    string_1 = input()
    string_2 = input()

    # 1차원 DP
    DP = [0] * len(string_1)

    for i in range(len(string_2)):
        target_str = string_2[i]
        cur_mx = 0
        for j in range(len(string_1)):
            if cur_mx < DP[j]:  # 중복 증가를 방지
                cur_mx = DP[j]
                continue
            if string_1[j] == target_str:
                DP[j] = cur_mx + 1
        print(DP)

    print(max(DP))
