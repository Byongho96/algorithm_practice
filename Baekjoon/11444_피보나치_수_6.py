import sys
sys.setrecursionlimit(10**9)

def two_by_two_matrix_multi(M1 :list, M2 :list):
    result =[[0] * 2 for _ in range(2)]
    result[0][0] = (M1[0][0] * M2[0][0] + M1[0][1] * M2[1][0]) % 1000000007
    result[0][1] = (M1[0][0] * M2[0][1] + M1[0][1] * M2[1][1]) % 1000000007
    result[1][0] = (M1[1][0] * M2[0][0] + M1[1][1] * M2[1][0]) % 1000000007
    result[1][1] = (M1[1][0] * M2[0][1] + M1[1][1] * M2[1][1]) % 1000000007
    return result

def matrx_power_divide_conquer(N):
    # end condition
    if N == 0:
        return [[1, 0], [0, 1]] # identity matrix
    if N == 1:
        return [[1, 1], [1, 0]]
    
    # divide and conquer
    if N % 2:
        M = matrx_power_divide_conquer(N // 2)
        return two_by_two_matrix_multi(two_by_two_matrix_multi(M, M), [[1, 1], [1, 0]])
    else:
        M = matrx_power_divide_conquer(N // 2)
        return two_by_two_matrix_multi(M, M)

# calculate fibonacci based on matrix multiplication
# [fn+1, fn] = [[1, 1], [1, 0]]^n X [1, 0]
def fibonacci(N):
    MATRIX = matrx_power_divide_conquer(N - 1)
    return MATRIX[0][0]

if __name__ == '__main__':
    N = int(input())
    answer = fibonacci(N)
    print(answer)