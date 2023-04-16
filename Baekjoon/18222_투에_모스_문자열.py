if __name__ == "__main__":
    K = int(input())

    num_flip = 0    # 문제의 2번 과정에서 뒤바뀐 횟수
    while K != 1:   # K 분할하며 줄이는 과정에서 모든 K는 1로 귀결된다.
        # K를 K 미만의 2의 제곱수로 뺀다.
        two_square = 1 
        while two_square < K:
            two_square *= 2
        K -= two_square // 2
        num_flip += 1

    print(1 if num_flip % 2 else 0) # num_flip에 따라 정답이 결정된다.