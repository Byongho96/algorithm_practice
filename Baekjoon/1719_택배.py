import heapq

def dijkstra(start, adjLst):
    distance = [2000000] * (N + 1)
    answer = ['-'] * (N + 1)

    # 시작점 지정
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    # 시작점의 이웃 인접 집하장들로 answer 업데이트
    for weight, first_node in adjLst[start]:
        distance[first_node] = weight
        answer[first_node] = str(first_node)
        heapq.heappush(heap, (weight, first_node))

    while heap:
        dist, nearest = heapq.heappop(heap)

        # 유효하지 않은 값 무시
        if distance[nearest] < dist:
            continue

        for weight, adj in adjLst[nearest]:
            new_dist = dist + weight
            if new_dist < distance[adj]:
                distance[adj] = new_dist
                answer[adj] = answer[nearest]   # 시작점의 이웃 인접 집하장들로 answer 업데이트
                heapq.heappush(heap, (new_dist, adj))

    print(' '.join(answer[1:]))

if __name__ == "__main__":
    N, E = map(int, input().split())

    # 인접 리스트 생성
    adjLst = [[] for _ in range(N + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adjLst[n1].append((w, n2))
        adjLst[n2].append((w, n1))

    # 다익스트라
    for n in range(1, N + 1):
        dijkstra(n, adjLst)