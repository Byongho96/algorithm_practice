# 경로를 찾는 dfs 
def find_loop(N, start, adjLst):
    visited = [False] * (N + 1)
    stack = []

    # 시작점 셋팅
    node = start
    visited[node] = True

    while True:
        # 자식 상태노드 탐색
        for adj in adjLst[node]:
            if not visited[adj]:
                stack.append(node)
                node = adj
                visited[node] = True
                break
            if stack and adj != stack[-1] and adj in stack:   # 반복지점을 찾는 순간
                idx = stack.index(adj)
                return stack[idx:] + [node] # 순환 경로
        # 부모 상태노드로 회귀
        else:
            if stack:
                node = stack.pop()
            else:
                break
    
    return False    # 무조건 순환고리가 존재하기 때문에 False가 반환 될 일은 없음

# 순환역으로 거리를 계산하는 bfs
def cal_distance(N, loop, adjLst):
    visited = [-1] * (N + 1)
    stack = []

    s = loop[0] # 시작점으로 순환역 중 하나로 설정
    stack.append(s)
    visited[s] = 0

    while stack:
        node = stack.pop()
        for adj in adjLst[node]:
            if visited[adj] == - 1:
                if adj in loop: # 순환역일 경우
                    visited[adj] = 0
                else:           # 순환역이 아닐 경우
                    visited[adj]  = visited[node] + 1
                stack.append(adj)
    
    return visited[1:]

if __name__ == "__main__":
    N = int(input())

    # 인접리스트 생성
    adjLst = [[] for _ in range(N + 1)]
    for _ in range(N):
        n1, n2 = map(int, input().split())
        adjLst[n1].append(n2)
        adjLst[n2].append(n1)

    loop = find_loop(N, 1, adjLst)  # 순환역 찾기
    answer = cal_distance(N, loop, adjLst)  # 거리 정보 계산하기

    print(' '.join(list(map(str, answer))))