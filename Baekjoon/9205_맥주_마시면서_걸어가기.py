def dfs(N, nodes):
    ex, ey = nodes[-1]  # 도착지점 기억

    stack = []
    visited = [0] * N 

    stack.append(nodes[0])  # 시작지점 설정
    visited[0] = 1

    while stack:
        x, y = stack.pop()
        if x == ex and y == ey: # 도착했을 경우
            return 'happy'
        for i in range(N):
            nx, ny = nodes[i]
            if not visited[i] and (abs(x - nx) + abs(y - ny)) <= 1000:
                visited[i] = 1
                stack.append((nx, ny))

    return  'sad'   # 도착할수 없을 경우

if __name__ == "__main__":
    T = int(input())  # 테스트 케이스 수

    for _ in range(T):
        N = int(input())    # 편의점 갯수

        nodes = []          # 모든 지점을 (x, y)형태로 리스트에 모은다
        for _ in range(N + 2):
            nodes.append(tuple(map(int, input().split())))

        result = dfs(N + 2, nodes)  # dfs로 결과값을 추출
        print(result)

