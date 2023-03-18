def dfs(N, si, sj, ei, ej):
    stack = []
    visited = [[[0] * N for _ in range(N)] for _ in range(N ** 2 + N)]

    # 시작점 지정
    visited[0][0][0] = 1
    stack.append((0, si, sj, 0))

    while stack:
        t, i, j, stayed = stack.pop()

        # 종료조건
        if i == ei and j == ej:
            return 1
        
        # 필요이상으로 멈춰있던 경우 가지 치기 -> > 연산이 >= 연산보다 빠름!! 
        if stayed > N - 1:
            continue
        
        # 9개 방향 탐색
        for di ,dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)):
            ni = i + di
            nj = j + dj
            # 행 범위 이내 and 열 범위 이내 and 같은 시간에 방문한 적이 없는 노드 and 벽이 없는 곳 and 움직인 다음에 벽이 오지 않는 곳
            if 0 <= ni < N and 0 <= nj < N and not visited[t + 1][ni][nj] and (ni < t or arr[ni - t][nj] == '.') and (ni < t + 1 or arr[ni - t - 1][nj] == '.'):
                if di == 0 and dj == 0:
                    stayed += 1
                visited[t + 1][ni][nj] = 1
                stack.append((t + 1, ni, nj, stayed))

    # 도착 불가능한 경우
    return 0

if __name__ == "__main__":

    arr = [ list(input()) for _ in range(8) ]
    answer = dfs(8, 7, 0, 0, 7)

    print(answer)