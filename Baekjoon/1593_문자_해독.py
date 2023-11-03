if __name__ == "__main__":
    LW, LS = map(int, input().split())
    W, S = input(), input()

    # make counter list
    offset = ord("A")
    TOTAL = ord("z") - offset + 1
    counter = [0] * TOTAL
    for w in W:
        counter[ord(w) - offset] += 1

    # set initial sliding window
    for i in range(LW - 1):
        counter[ord(S[i]) - offset] -= 1

    # sliding window
    answer = 0
    l, r = 0, LW - 1
    for _ in range(LS - LW + 1):
        counter[ord(S[r]) - offset] -= 1

        if counter.count(0) == TOTAL:
            answer += 1

        counter[ord(S[l]) - offset] += 1
        l += 1
        r += 1

    print(answer)
