def solution(m, n, puddles):
    arr = [0] * (m + 1) # 1차원 DP
    arr[1] = 1  # 초깃값 셋팅
    
    for i in range(1, n + 1):   # DP 행 갱신
        for j in range(1, m + 1):   # DP 열 갱신
            if [j,  i] in puddles:  # 현재 위치가 물에 잠겼을 경우
                arr[j] = 0
            else:                   # 현재 위치가 물에 잠기지 않았을 경우
                arr[j] = arr[j] + arr[j-1]
        print(arr)
    
    answer = arr[-1] % 1000000007
    return answer