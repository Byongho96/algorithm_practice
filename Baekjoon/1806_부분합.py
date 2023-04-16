if __name__=="__main__":
    N, S = map(int, input().split())
    nums = list(map(int, input().split()))

    start, end = 0, 0
    sum_ = nums[0]

    answer = N + 1
    while True:
        if sum_ < S:
            end += 1
            if end == N:
                break
            sum_ += nums[end]
        else:
            answer = min(answer, end - start + 1)
            sum_ -= nums[start]
            start += 1

    if answer == N + 1:
        print(0)
    else:
        print(answer)
