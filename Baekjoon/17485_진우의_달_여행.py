import sys
input = sys.stdin.readline

if __name__ == '__main__':
    INF = 100000
    N, M = map(int, input().split())
    cost_arr = [list(map(int, input().split())) for _ in range(N)] 
    cul_cost_arr = [[[INF, INF, INF] for _ in range(M)] for _ in range(2)]  # DP 배열. 바로 이전 내역만 기억

    # DP 배열 처음 행(i == 0) 초기화
    for j in range(M):
        cul_cost_arr[0][j][0] = cost_arr[0][j]
        cul_cost_arr[0][j][1] = cost_arr[0][j]
        cul_cost_arr[0][j][2] = cost_arr[0][j]
    
    # DP 배열 채우기
    for i in range(1, N):
        cul_i = i % 2   # 현재 업데이트할 행
        prev_cul_i = abs(1 - cul_i) # 이전 행
        for j in range(M):
            cur_cost = cost_arr[i][j]
            for k in range(3):  # 0: 왼쪽 위에서 오는 경우, 1: 위에서 오는 경우, 2: 오른쪽 위에서 오는 경우
                direction = k -1
                if (j == 0 and direction == -1) or (j == M - 1 and direction == 1): # 불가능한 경우, 왼쪽 끝행인데 왼쪽 위에서 오거나, 오른쪽 끝행인데 오른쪽 위에서 오는 경우
                    cul_cost_arr[cul_i][j][k] = INF
                # 각각의 경우에 대해, 이전 행에서 지금과 동일한 방향값을 제외하고 최솟값을 넛택
                elif k == 0:    # 왼쪽 위에서 오는 경우
                    cul_cost_arr[cul_i][j][k] = cur_cost + min(cul_cost_arr[prev_cul_i][j+direction][1], cul_cost_arr[prev_cul_i][j+direction][2]) 
                elif k == 1:    # 위에서 오는 경우
                    cul_cost_arr[cul_i][j][k] = cur_cost + min(cul_cost_arr[prev_cul_i][j+direction][0], cul_cost_arr[prev_cul_i][j+direction][2]) 
                else:           # 오른쪽 위에서 오는 경우
                    cul_cost_arr[cul_i][j][k] = cur_cost + min(cul_cost_arr[prev_cul_i][j+direction][0], cul_cost_arr[prev_cul_i][j+direction][1]) 

    answer = INF
    last_cul_i = (N - 1) % 2    # 마지막 행의 위치 파악
    # 최솟값 계산
    for j in range(M):
        answer = min(answer, min(cul_cost_arr[last_cul_i][j]))
    
    print(answer)