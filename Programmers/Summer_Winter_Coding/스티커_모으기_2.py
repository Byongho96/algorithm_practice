def solution(sticker):
    N = len(sticker)
    
    # 스티커가 2개 이하일 경우
    if N < 3:
        return max(sticker)
    
    dp0 = [0] * N   # 첫번째 스티커 찢지 않음
    dp1 = [0] * N   # 첫번째 스티커 찢음
    
    # dp 채우기
    dp0[0], dp0[1] = 0, sticker[1]
    dp1[0], dp1[1] = sticker[0], sticker[0]
    for i in range(2, N - 1):
        dp0[i] = max(dp0[i - 1], dp0[i - 2] + sticker[i])
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])
    
    # 마지막 값
    dp0[-1] = max(dp0[-2], dp0[-3] + sticker[-1])
    dp1[-1] = dp1[-2]
    
    return max(dp0[-1], dp1[-1])