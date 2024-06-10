

def solution(N, nums):
    DP = [1] * N    # DP[i] : i번째 수를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이

    for i in range(1, N):
        for j in range(i):
            if nums[i] < nums[j]:   
                DP[i] = max(DP[i], DP[j] + 1)

    return max(DP)

if __name__ == "__main__":
    N = int(input())
    nums= list(map(int, input().split()))

    answer = solution(N, nums)
    print(answer)