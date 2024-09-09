def solution(info, edges):
    N = len(info)
    visited = [0] * N 
    
    # adjacent list
    adjLst = tuple([] for _ in range(N))
    for i, j in edges:
        adjLst[i].append(j)
        adjLst[j].append(i)
    
    # DFS
    answer = 0
    stack = [(0, 0, 0)] # idx, sheep, wolf
    while stack:
        cur, sheep, wolf = stack.pop()
        if not visited[cur]:
            sheep += (1 - info[cur])
            wolf += info[cur]
            
        if sheep < visited[cur] + 1:
            continue
            
        visited[cur] = sheep
        answer = max(answer, visited[cur])
        print(cur, sheep, wolf)
        
        for adj in adjLst[cur]:
            if visited[adj] and visited[adj] < visited[cur]:    # a
                stack.append((adj, sheep, wolf))
            elif not visited[adj] and not info[adj]:
                stack.append((adj, sheep, wolf))
            elif not visited[adj] and info[adj] and sheep > wolf + 1:
                stack.append((adj, sheep, wolf))

    # print(visited)
            
    return answer


# print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])) # 5
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))