def solution(triangle):
    
    for i in range(len(triangle)):
        row = []
        for j, num in range(len(tri)):
            if j == 0:
                triangle[i][j] = triangle[i-1][j] + num
            elif j == len(row) - 1:
                triangle[i][j] = triangle[i-1][j-1] + num
            else:
                triangle[i][j] = max(triangle[i-1][j-1], triangle[i-1][j]) + num
        i += 1
        
        
    return max(triangle[-1])