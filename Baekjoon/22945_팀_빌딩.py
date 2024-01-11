if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    # two pointer
    s, e = 0, N - 1
    middle_num = N - 2
    answer = 0
    while s < e:
        answer = max(min(arr[s], arr[e]) * middle_num, answer)
        if arr[s] < arr[e]:
            s += 1
        else:
            e -= 1
        middle_num -= 1

    print(answer)
