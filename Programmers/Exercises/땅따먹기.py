def solution(land):
    answer = 0

    N = len(land)
    
    DP = [[0] * 4 for _ in range(N)]
    DP[0] = land[0]
    
    for i in range(1, N):
        for j in range(4):
            for k in range(4):
                if j == k:
                    continue
                DP[i][j] = max(DP[i][j], land[i][j] + DP[i - 1][k])
    
    answer = max(DP[-1])
    return answer