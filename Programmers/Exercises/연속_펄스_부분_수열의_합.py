def solution(sequence):
    N = len(sequence)
    dp = [ [0] *2 for _ in range(N) ]
    
    dp[0][0] = sequence[0]
    dp[0][1] = -sequence[0]
    mx = max(dp[0])
    
    for i in range(1, N):
        dp[i][0] = max(dp[i-1][1], 0) + sequence[i]
        dp[i][1] = max(dp[i-1][0], 0) - sequence[i]
        mx = max(mx, *dp[i])
        
    return mx