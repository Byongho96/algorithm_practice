N, M = map(int, input().split())

def backtracking(i, start_idx):
    # 종료조건
    if i == M:
        print(*lst)
        return
    for num in range(start_idx, N + 1):
        if not visited[num]:
            lst[i] = num
            visited[num] = 1
            backtracking(i + 1, num + 1)
            visited[num] = 0


lst = [0] * M
visited = [0] * (N + 1)
backtracking(0, 1)
