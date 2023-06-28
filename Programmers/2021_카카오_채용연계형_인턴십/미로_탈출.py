from collections import defaultdict
import heapq

# 비트마스크를 기반으로, 활성화된 트랩에 대한 key 생성
def calculate_key(activated_traps, new_trap):
    global traps_idx
    
    if new_trap in traps_idx:
        return activated_traps ^ (1 << traps_idx[new_trap])
    
    return activated_traps

# 인접노드 간의 관계가, 순관계인지 역관계인지 판단
def check_reverse(cur, adj, activated_traps):
    global traps_idx
    
    cur_trap, adj_trap = 0, 0
    if cur in traps_idx:
        cur_trap = (activated_traps >> traps_idx[cur]) & 1
    if adj in traps_idx:
        adj_trap = (activated_traps >> traps_idx[adj]) & 1
        
    return cur_trap ^ adj_trap


# 비용과 활성화된 트랩을 같이 비교하는 다익스트라
def dijkstra(n, start, end, adjLst, traps):
    global traps_idx
    
    INF = 3000 * 3000 * 3
    distance = [{} for _ in range(n + 1)]   # 초깃값을 비워서 생성 (경우의 수가 너무 많음)

    heap = [] 
    heapq.heappush(heap, (0, start, 0))    # (비용, 노드, 활성화된 트랩에 대한 비트마스크)
    distance[start][0] = 0

    while heap:
        cost, cur, activated_traps = heapq.heappop(heap)
        
        # 이미 처리된 노드 패스
        cost_record = distance[cur].get(activated_traps, INF)
        if cost_record < cost:
            continue
        
        # 종료조건
        if cur == end:
            return cost
        
        # 인접 노드 탐색
        for adj, weight in adjLst[cur]:
            reversed_path = (weight < 0)    # 역경로 여부
            is_reverse = check_reverse(cur, adj, activated_traps)   # 두 노드의 역관계 여부
            
            if reversed_path ^ is_reverse:  # 역경로 여부와 역관계 여부가 일치하지 않으면, 해당 경로 패스
                continue
            
            # 비용과 활성화 트랩 업데이트
            new_cost = cost + abs(weight)
            new_activated_traps = calculate_key(activated_traps, adj)
                    
            # 조건 충족하면 heap에 push
            adj_cost_record = distance[adj].get(new_activated_traps, INF)
            if new_cost < adj_cost_record:
                distance[adj][new_activated_traps] = new_cost
                heapq.heappush(heap, (new_cost, adj, new_activated_traps))
                
def solution(n, start, end, roads, traps):
    global traps_idx
    
    adjLst = defaultdict(list)
    for i, j, cost in roads:
        adjLst[i].append((j, cost))
        adjLst[j].append((i, -cost))    # 음수로 역경로도 추가 
            
    # 노드의 최대갯수는 1000개인 반면, 트랩의 최대갯수는 10개이므로
    # 시간복잠도를 줄이고자 딕셔너리 생성
    traps_idx = {}
    for idx, trap in enumerate(traps):
        traps_idx[trap] = idx
    
    # 다익스트라 알고리즘
    answer = dijkstra(n, start, end, adjLst, traps)
        
    return answer