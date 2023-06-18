from typing import List, Tuple
from collections import defaultdict
import heapq

# dijkstra(노드 갯수, 시작점, 인접노드리스트) -> 각 노드까지의 최단 거리
def dijkstra(V: int, start: int, adjLst: List[Tuple[int, int]]) -> List[int]:
    # 초깃값 셋팅
    INF = 200 * 100000
    distance = [INF] * (V + 1)    # 시작점부터 다른 노드까지의 거리

    # 시작점 지정
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        # 힙에서 가장 낮은 가중치를 가진 노드를 heap에서 pop
        dist, nearest = heapq.heappop(heap)

        # 이미 거리 계산이 완료된 노드 무시하기: Basic Dijkstra에서 visited 배열을 기능을 담당
        if distance[nearest] < dist:
            continue

        # 인접 노드들의 거리 재계산하여 heap에 push
        for adj, weight in adjLst[nearest]:
            new_dist = dist + weight
            if new_dist < distance[adj]:
                distance[adj] = new_dist
                heapq.heappush(heap, (new_dist, adj))
                
    return distance

def solution(n, s, a, b, fares):
    
    # 인접 노드 리스트 만들기
    adjLst = defaultdict(list)
    for i, j, fare in fares:
        adjLst[i].append((j, fare))
        adjLst[j].append((i, fare))
        
    # 모든 지점에 대해 dijkstra 실행 (플로이드-와샬과 동일한 효과)
    dijkstra_lst = [[]]
    for start in range(1, n + 1):
        dijkstra_lst.append(dijkstra(n, start, adjLst))
    
    # 모든 경우의 수 탐색
    answer = 200 * 100000 * 2
    for common_end in range(1, n + 1):
        case = dijkstra_lst[s][common_end] + dijkstra_lst[common_end][a] + dijkstra_lst[common_end][b]
        answer = min(answer, case)
    
    return answer