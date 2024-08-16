import heapq

DIRECTION = ((0, 1), (1, 0), (0, -1), (-1, 0))

def solution(land, height):
    N = len(land)
    visited = [[0] * N for _ in range(N)]
    
    answer = 0
    ladder_heap = []
    stack = [(0, 0)]
    
    while True:  
        # DFS
        while stack:
            i, j = stack.pop()
            cur = land[i][j]
            
            visited[i][j] = 1

            for di , dj in DIRECTION:
                ni = i + di
                nj = j + dj
                
                if ni < 0 or ni > N - 1 or nj < 0 or nj > N - 1:
                    continue

                if visited[ni][nj] == 1:
                    continue

                diff = abs(cur - land[ni][nj])
                if diff > height:
                    heapq.heappush(ladder_heap, (diff, ni, nj))
                    continue

                visited[ni][nj] = 1
                stack.append((ni, nj))
        
        # heap으로 최소 사다리 설치 위치
        while ladder_heap:
            cost, li, lj = heapq.heappop(ladder_heap)
            
            if visited[li][lj] == 1:
                continue
                
            answer += cost
            stack.append((li, lj))
            break
        
        # 없으면 끝
        else:
            break
        
        
    return answer