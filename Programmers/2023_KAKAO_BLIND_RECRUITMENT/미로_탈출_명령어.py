'''
n, m : 격자 크기
(si, sj) : 출발 지점
(ei, ej) : 끝 지점
K: 이동 횟수

d(아래), l(왼쪽), r(오른쪽), u(위쪽)
'''
from collections import deque

direction_ref = {
    'd': (1, 0), 
    'l': (0, -1), 
    'r': (0, 1),
    'u': (-1, 0),
}
    
def solution(n, m, si, sj, ei, ej, K):
    
    # 짝, 홀로 해결 가능성 판단
    if (abs(ei - si) + abs(ej - sj)) % 2 != K % 2:
        return 'impossible'
    
    # bfs
    q = deque([(si, sj, 0, '')])
    visited = [[''] * (m + 2)] + [[''] + ['z'] * m + [''] for _ in range(n)] + [[''] * (m + 2)]

    while q:
        i, j, k, history = q.popleft()
        
        # 종료조건
        if k == K:
            if i == ei and j == ej:
                return visited[i][j]
            continue
            
        # 가지치기
        if abs(i - ei) + abs(j - ej) + k > K:
            continue
        
        # 다음 상태: d -> l -> r -> u 순으로 탐색
        for direction in ('d', 'l', 'r', 'u'):
            di, dj = direction_ref[direction]
            ni = i + di
            nj = j + dj
            new_visited = history + direction
            length = len(visited[ni][nj])
            if visited[ni][nj] and new_visited[:length] <= visited[ni][nj]:
                visited[ni][nj] = new_visited
                q.append((ni, nj, k + 1, new_visited))
    
    return  'impossible'