if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))

    stk = []    # 스택
    answer = [0] * N    # 정답 배열

    for idx, num in enumerate(nums):
        if not stk or stk[-1][1] >= num:    # 현재 스택이 비었거나, 스택의 최상단이 현재 숫자보다 작을경우
            stk.append((idx, num))
            continue

        while stk and stk[-1][1] < num:     # 현재 스택이 비었거나, 스택의 최상단이 현재 숫자보다 작을 때까지
            pop_idx, pop_num = stk.pop()    
            answer[pop_idx] = num           # 오큰수 할당
        stk.append((idx, num))

    while stk:                              # 스택의 남은 값에 대해서 -1 할당
        pop_idx, pop_num = stk.pop()
        answer[pop_idx] = -1

    print(*answer)
