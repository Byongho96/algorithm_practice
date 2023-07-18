from collections import defaultdict

# dfs로 모든 노드가 방문 가능하면, True 반환
def dfs(start, num_athletes):
    global adjLst
    
    visited = [False] * (num_athletes + 1)
    visited[start] = 1
    stack = [(start, 1), (start, -1)]   # 승리와 패배 모두 탐색
    
    num_visited = 1
    while stack:
        cur, direction = stack.pop()
            
        # 모든 노드를 방문할 수 있을 경우
        if num_visited == num_athletes:
            return True
        
        # 주변 노드 탐색
        for adj, adj_dir in adjLst[cur]:
            if not visited[adj] and direction == adj_dir:   # 방향성을 일치
                visited[adj] = True
                num_visited += 1
                stack.append((adj, adj_dir))
        
    return False

def solution(n, results):
    global adjLst
    
    # 인접 리스트 만들기
    adjLst = defaultdict(list)
    for i, j in results:
        adjLst[i].append((j, 1))    # 승리한 상대에 대해서 방향성 1
        adjLst[j].append((i, -1))   # 패배한 상대에 대해서 방향성 -1
        
    answer = 0
    for start in range(1, n + 1):
        if dfs(start, n):
            answer += 1
    
    return answer