def calculate_score(arr):
    global apeach_arr
    global answer
    global max_score_diff
    
    apeach_score = 0
    lion_score = 0
    
    for idx, lion_num in enumerate(arr):
        apeach_num = apeach_arr[idx]
        if lion_num > apeach_num:
            lion_score += (10 - idx)
        elif apeach_num:
            apeach_score += (10 - idx)
       
    if lion_score - apeach_score > max_score_diff:
        max_score_diff = lion_score - apeach_score
        answer = arr[:]    # arr is call by reference


def backtracking(n, N, idx, arr):
    if n == N:
        calculate_score(arr)
        return
                             
    for i in range(idx, -1, -1):
        arr[i] += 1
        backtracking(n + 1, N, i, arr)
        arr[i] -= 1
    

def solution(N, info):
    global apeach_arr
    global max_score_diff
    global answer
    
    apeach_arr = info
     
    answer = [-1]
    max_score_diff = 0
    backtracking(0, N, 10, [0] * 11)
                             
    return answer