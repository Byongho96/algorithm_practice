MOD = 10 ** 9 + 7
DIRECTION = ((-1, 0), (1, 0), (0, 1), (0, -1))

# 4 x 3 * 3 X 4 = 4 X 4
def matrix_multiply(A, B):
    R1, C1 = len(A), len(A[0])
    R2, C2 = len(B), len(B[0])

    result = [[0 for _ in range(C2)] for _ in range(R1)]

    # 행렬 곱셈 수행
    for i in range(R1):
        for j in range(C2):
            for k in range(C1):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= MOD

    return result

# 분할 정복 방식으로 제곱 계산하여 연산 최소화
def matrix_power(mat, cnt) :
    if cnt == 1 :
        return mat
    
    sub_result = matrix_power(mat, cnt // 2)
    temp_result = matrix_multiply(sub_result, sub_result)
    
    if cnt % 2 :
        return matrix_multiply(temp_result, mat)
    else :
        return temp_result


def solution(grid, d, k):
    N, M = len(grid), len(grid[0])
    L = N * M
    D = len(d)
    
    # DP[hop][i][j] : i에서 hop번 거쳐 j까지 가는 경우의 수
    # 가장 마지막에 DP[D] 만을 가지고, 행렬 제곱 연산을 통해 답을 추출
    DP = [[[0] * (L) for _ in range(L)] for _ in range(D + 1)]
    
    # DP 초기화
    for point in range(L):
        DP[0][point][point] = 1
    
    # DP 채우기
    for hop in range(1, D + 1):
        for i in range(N):
            for j in range(M):
                for di, dj in DIRECTION:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni > N - 1 or nj < 0 or nj > M - 1:
                        continue
                    if grid[ni][nj] - grid[i][j] != d[hop - 1]:
                        continue
                    for start in range(L):
                        DP[hop][start][ni * M + nj] += DP[hop - 1][start][i * M + j]
            
    # 최종 행렬 제곱
    one_cycle_mat = DP[D]
    kth_cycle_mat = matrix_power(one_cycle_mat, k)
    
    # 답안 계산
    answer = 0
    for i in range(L) :
        for j in range(L) :
            answer += kth_cycle_mat[i][j]
            answer %= MOD
            
    return answer