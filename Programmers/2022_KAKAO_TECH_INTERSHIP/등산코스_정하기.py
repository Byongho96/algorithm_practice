from collections import deque
import heapq

# 다익스트라 개선
from collections import defaultdict
import heapq

def dijkstra(N, adjLst, gates, summits):
    INF = 10000000 + 1  # 최댓값 설정 유의!
    intensity = [INF] * (N + 1)
    
    # 시작점 지정
    heap = []
    for gate in gates:
        intensity[gate] = 0
        heapq.heappush(heap, (0, gate))
    
    answers = []
    
    while heap:
        its, cur = heapq.heappop(heap)
        
        # 유효하지 않은 노드 삭제
        if its < intensity[cur]:
            continue
        
        # 종료조건 (최대조건을 초과했을 경우)
        if its > INF:
            return answers
            
        # 종료조건 (정상에 도달했을 경우)
        if cur in summits:
            answers.append([cur, its])
            INF = its
            continue
                 
        # 주변 노드 탐색 (출입구가 아닌)
        for w, adj in adjLst[cur]:
            new_its = max(its, w)
            if adj not in gates and new_its < intensity[adj]:
                intensity[adj] = new_its
                heapq.heappush(heap, (new_its, adj))
    
    return answers
    
def solution(n, paths, gates, summits):
    # 인접 노드 리스틑 생성
    adjLst = defaultdict(list)
    for i, j, w in paths:
        adjLst[i].append((w, j))
        adjLst[j].append((w, i))
    
    # 집합연산으로 바꾼 다음 in 연산 시, 유의미하게 빠름
    gates = set(gates)
    summits = set(summits)
    
    # Dijkstra
    answers = dijkstra(n, adjLst, gates, summits)
    
    answers.sort(key=lambda x: (x[1], x[0]))
    
    return answers[0]

# 다익스트라
def solution(n, paths, gates, summits):

    adjLst = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        adjLst[i].append((w, j))
        adjLst[j].append((w, i))

    intensity = [10000001] * (n+1)
    h = []

    summits_set = set(summits)      # 뭐야 이게...!? 집합으로 하면 in 사용시 선형탐색 대신 무엇을??
                                    # sort 후 이분탐색으로 구현할수도 있다고 한다...

    for gate in gates:
        intensity[gate] = 0
        heapq.heappush(h, (0, gate))

    while h:
        intense, now = heapq.heappop(h)

        if intensity[now] < intense:
            continue

        for intense2, next_node in adjLst[now]:
            tmp = max(intense, intense2)
            if tmp < intensity[next_node]:
                intensity[next_node] = tmp
                if next_node in summits_set:
                    continue
                heapq.heappush(h, (tmp, next_node))

    # print(intensity)
    mn_summit = 0
    mn = 10000001
    summits.sort()  # 문제 조건상 필요!
    for summit in summits:
        # print(summit, intensity[summit])
        if intensity[summit] < mn:
            mn = intensity[summit]
            mn_summit = summit
    
    return [mn_summit, mn]

# 변형된 bfs 2개 시간초과
def solution(n, paths, gates, summits):

    adjLst = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        adjLst[i].append((j, w))
        adjLst[j].append((i, w))
        
    mn_summit = 0
    mn = 10000001

    intensity = [10000001] * (n+1)
    q = deque()

    for gate in gates:
        intensity[gate] = 0
        q.append((gate, 0))

    while q:
        v, i = q.popleft()

        if intensity[v] < i:
            continue

        for w, intense in adjLst[v]:
            if w not in gates:
                tmp = max(intensity[v], intense)
                if intensity[w] > tmp:
                    intensity[w] = tmp
                    if w not in summits:
                        q.append((w, intensity[w]))

    summits.sort()  # 문제 조건상 필요!
    for summit in summits:
        # print(summit, intensity[summit])
        if intensity[summit] < mn:
            mn = intensity[summit]
            mn_summit = summit
    
    return [mn_summit, mn]


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))