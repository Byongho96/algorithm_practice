from collections import deque

# bfs
def count_the_farthest_nodes(n, adjLst, start):
    queue = deque()
    visited = [0] * (n + 1)
    
    # set the start
    queue.append((1, start))
    visited[start] = 1
    
    max_dis = 0
    num_max_nodes = 0
    while queue:
        dis, cur = queue.popleft()
        
        # visit the node
        if dis < max_dis:
            pass
        elif dis > max_dis:
            max_dis = dis
            num_max_nodes = 1
        else:
            num_max_nodes += 1
        
        # traverse the adjacent nodes
        for adj in adjLst[cur]:
            if visited[adj]:
                continue
            visited[adj] = dis + 1
            queue.append((dis + 1, adj))
        
    return num_max_nodes

def solution(n, edge):
    # make adjacent nodes lists
    adjLst = [[] for _ in range(n + 1)]
    for [i, j] in edge:
        adjLst[i].append(j)
        adjLst[j].append(i)
        
    answer = count_the_farthest_nodes(n, adjLst, 1)
    return answer