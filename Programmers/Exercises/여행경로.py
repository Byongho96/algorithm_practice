from collections import defaultdict

def backtracking(N, tickets, cur_port, path, visited):
    # 종료조건
    if len(path) == N:
        return path + [cur_port]
    
    # 후보군 출력
    path.append(cur_port)
    for i in range(N):
        if not visited[i] and tickets[i][0] == cur_port:
            visited[i] = True
            next_port = tickets[i][1]
            answer = backtracking(N, tickets, next_port, path, visited)
            if answer:
                return answer
            visited[i] = False
    path.pop()
    
    return False

def solution(tickets):
    # adjLst 정렬
    tickets.sort()
    
    N = len(tickets)
    cur_port = "ICN" 
    path = []
    visited = [False] * N
    answer = backtracking(N, tickets, cur_port, path, visited)
    
    return answer