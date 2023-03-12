N, M = map(int, input().split())

num_lst = list(map(int, input().split()))
num_lst.sort()

def backtracking(m, idx):
    if m == M:
        print(' '.join(map(str, lst)))
        return

    if M - m > N - idx:
        return 
    
    for i in range(idx, N):
        lst[m] = num_lst[i]
        backtracking(m + 1, i + 1)
    return


lst = [0] * M
backtracking(0, 0)