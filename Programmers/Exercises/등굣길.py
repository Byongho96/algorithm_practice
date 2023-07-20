def solution(m, n, puddles):
    dp = [0] * (m + 1)  # 1차원 DP
    
    dp[1] = 1   # 초기조건 셋팅
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if [j, i] in puddles:
                dp[j] = 0
            else:
                dp[j] += dp[j-1]
    
    answer = dp[m] % 1000000007
    return answer