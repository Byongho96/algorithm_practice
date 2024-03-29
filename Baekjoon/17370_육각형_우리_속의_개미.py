def backtracking(N, step, i, j):
    # 종료 조건
    if N + 2 == step:
        if visited[i][j]:   # 조건에 맞을 경우
            return 1
        return 0
    
    # 가지치기
    if visited[i][j]:
        return 0
    
    # 자식 상태노드 탐색
    nums = 0
    visited[i][j] = step
    for (ni, nj) in ((i, j - 1), (i, j + 1), (i + 2 * ((i + j) % 2) - 1, j)):
        if visited[ni][nj] == step - 1: # 바로 이전에 지나온 경로는 탐색 X
            continue
        nums += backtracking(N, step + 1, ni, nj)
    visited[i][j] = 0
    return nums

if __name__ == "__main__":
    N = int(input())
    visited = [[0] * (2 * (N + 2)) for _ in range(2 * (N + 2))] # 유한한 범위의 2차원 visited 배열 생성

    s = N + 1 if (N % 2) else N + 2 # 짝수 인덱스를 가진 visited 배열 중앙 선정
    visited[s][s] = 1

    answer = backtracking(N, 2, s-1, s)
    print(answer)