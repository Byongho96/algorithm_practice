# 해설 참조: https://school.programmers.co.kr/questions/35224

def solution(arr):
    N = len(arr) // 2 + 1
    DP_max = [[0] * N for _ in range(N)]
    DP_min = [[0] * N for _ in range(N)]
    
    # DP 초깃값 셋팅
    for i in range(N):
        DP_max[i][i] = int(arr[2 * i])
        DP_min[i][i] = int(arr[2 * i])
    
    for diff in range(1, N):    # 숫자의 범위 크기를 2부터 N까지 증가시키며 채워나감
        for start in range(N - diff):   # 숫자 범위를 슬라이드 크기로 삼아 스캔
            mx = -1000 * 101
            mn = 1000 * 101
            for mid in range(start, start + diff):  # 모든 가능한 중간값을 고려
                if arr[2 * mid + 1] == '+':
                    mx_tmp = DP_max[start][mid] + DP_max[mid+1][start+diff]
                    mn_tmp = DP_min[start][mid] + DP_min[mid+1][start+diff]
                else:
                    mx_tmp = DP_max[start][mid] - DP_min[mid+1][start+diff]
                    mn_tmp = DP_min[start][mid] - DP_max[mid+1][start+diff]
                mx = max(mx, mx_tmp)
                mn = min(mn, mn_tmp)
            DP_max[start][start+diff] = mx
            DP_min[start][start+diff] = mn
        
    answer = DP_max[0][N-1] # 원하는 답: 0부터 N-1까지 N개의 숫자범위 중 최댓값
    return answer