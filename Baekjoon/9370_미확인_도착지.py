import sys
import heapq

INF = 2000 * 1000

# 힙을 사용한 다익스트라 알고리즘
def dijkstra(start, n):
    distance = [INF] * (n + 1)

    # 시작점 셋팅
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        dis, cur = heapq.heappop(heap)

        if dis > distance[cur]: # 유효하지 않은 값 버리기
            continue
        
        # 확정
        
        for weight, adj in adjLst[cur]:
            new_dis = dis + weight
            if distance[adj] > new_dis:
                distance[adj] = new_dis
                heapq.heappush(heap, (new_dis, adj))

    return distance

if __name__ == '__main__':
    input = sys.stdin.readline

    NUM_TEST = int(input())

    for _ in range(NUM_TEST):
        N, M, T = map(int, input().split())
        S, G, H = map(int, input().split())

        adjLst = [[] for _ in range(N + 1)]
        for _ in range(M):
            i, j, w = map(int, input().split())
            adjLst[i].append((w, j))
            adjLst[j].append((w, i))

        destinations = []
        for _ in range(T):
            destinations.append(int(input()))

        from_S_distance = dijkstra(S, N)   
        from_G_distance = dijkstra(G, N)   
        from_H_distance = dijkstra(H, N)   

        # 조건에 맞는 목적지 탐색
        answer = []
        target_distance = from_G_distance[H]
        for dest in destinations:
            if from_S_distance[dest] - from_S_distance[G] - from_H_distance[dest] == target_distance:
                answer.append(dest)
                continue
            if from_S_distance[dest] - from_S_distance[H] - from_G_distance[dest] == target_distance:
                answer.append(dest)
                continue

        answer.sort()
        print(*answer)