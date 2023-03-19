import heapq

def dijkstra(start, adjLst, distance, answer):

    # 시작점 지정
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    # 시작점을 기준으로 첫번재 이웃 노드 들에 대해서 answer 리스트 업데이트
    # because) 결국 모든 답은 시작노드의 이웃 노드들이 될 수밖에 없음
    for weight, first_node in adjLst[start]:
        distance[first_node] = weight
        answer[first_node] = str(first_node)
        heapq.heappush(heap, (weight, first_node))

    while heap:
        # 힙에서 가장 낮은 가중치를 가진 노드를 heap에서 pop
        dist, nearest = heapq.heappop(heap)

        # 이미 거리 계산이 완료된 노드 무시하기: Basic Dijkstra에서 visited 배열을 기능을 담당
        if distance[nearest] < dist:
            continue

        # 인접 노드들의 거리 재계산하여 heap에 push
        for weight, adj in adjLst[nearest]:
            new_dist = dist + weight
            if new_dist < distance[adj]:
                distance[adj] = new_dist
                answer[adj] = answer[nearest]   # 이웃 노드들의 answer를 현재 노드의 answer로 업데이트
                heapq.heappush(heap, (new_dist, adj))

    return distance

if __name__ == "__main__":
    N, E = map(int, input().split())

    adjLst = [[] for _ in range(N + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adjLst[n1].append((w, n2))
        adjLst[n2].append((w, n1))

    # 다익스트라
    distance = [[2000000] * (N + 1) for _ in range(N + 1)]
    answer = [['-'] * (N + 1) for _ in range(N + 1)]
    for n in range(1, N + 1):
        dijkstra(n, adjLst, distance[n], answer[n])

    # 출력
    for node in range(1, N + 1):
        print(' '.join(answer[node][1:]))