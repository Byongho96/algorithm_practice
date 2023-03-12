N, M = map(int, input().split())

num_lst = list(map(int, input().split()))
num_lst.sort()

def backtracking(m):
    if m == M:
        print(' '.join(map(str, lst)))
        return
    
    for i in range(N):
        if not visited[i]:
            lst[m] = num_lst[i]
            visited[i] = 1
            backtracking(m + 1)
            visited[i] = 0
    return


lst = [0] * M
visited = [0] * N
backtracking(0)