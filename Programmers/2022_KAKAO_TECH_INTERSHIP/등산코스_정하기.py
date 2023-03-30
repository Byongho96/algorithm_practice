from collections import deque
import heapq

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