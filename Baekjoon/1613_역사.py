from collections import defaultdict
import heapq

memoization = {}    # 각 노드(사건)의 dijkstra의 결과를 저장할 딕셔너리

# 가중치가 1인 djikstra
# BFS로도 같은 기능을 수행할 수 있지만, heap을 사용한 dijkstra의 O()이 더 작음
def dijkstra(N, start, adjLst):
    visited = [0] * (N + 1)
    following_accidents = []    # 반환값: start노드로부터 방문할 수 있는 모든 노드들 저장할 리스트

    visited[start] = 1
    heap = [start]

    while heap:
        node = heapq.heappop(heap)

        for adj in adjLst[node]:
            if not visited[adj]:
                visited[adj] = 1
                following_accidents.append(adj)
                heapq.heappush(heap, adj)

    return following_accidents

# accident_1과 accident_2의 선후 관계를 파악하여 반환
def isEarlier(N, accident_1, accident_2, adjLst):

    # accident_1의 memoization값 확인하여 없으면 dijkstra 적용
    accident_1_memo = memoization.get(accident_1)
    if not accident_1_memo:
        accident_1_memo = dijkstra(N, accident_1, adjLst)
        memoization[accident_1] = accident_1_memo

    # accident_2의 memoization값 확인하여 없으면 dijkstra 적용
    accident_2_memo = memoization.get(accident_2)
    if not accident_2_memo:
        accident_2_memo = dijkstra(N, accident_2, adjLst)
        memoization[accident_2] = accident_2_memo

    # 문제 조건에 따라 결과값 분기처리하여 반환
    if accident_2 in accident_1_memo:
        return '-1'
    if accident_1 in accident_2_memo:
        return '1'
    return '0'

if  __name__ == "__main__":
    N, K = map(int, input().split())
    
    adjLst = defaultdict(list)  # 인접리스트(단방향) 자료구조 형성
    for _ in range(K):
        history_1, history_2 = map(int, input().split())
        adjLst[history_1].append(history_2)

    S = int(input())
    answers = []    # 출력을 한 번에 하고자 리스트로 각 Case의 결과 임시 저장
    for _ in range(S):
        accident_1, accident_2 = map(int, input().split())
        answers.append(isEarlier(N, accident_1, accident_2, adjLst))

    print('\n'.join(answers))
