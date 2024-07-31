if __name__ =="__main__":
    N = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    answer = 0
    for i in range(N):
        answer += nums[i] * (N - i)

    print(answer)