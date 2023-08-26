"""
모든 지점이 연결되어있다는 조건이 없기 때문에

(음의 경로를 추적하는) Dijkstra로 풀 경우, 모든 노드 군집에 대해서 실행해야함
"""

import sys
input = sys.stdin.readline

import heapq

# dijkstra which can handle minus cycle
def dijkstra_detect_minus_cycle(N, adjLst, start, visited):
    INF = 10001 * N
    distance = [INF] * (N + 1)
    heap = []

    # set the start point
    distance[start] = 0
    heapq.heappush(heap, (start, 0, [0])) # path being used for the tracking minus cycle

    while heap:
        cur, dis, path = heapq.heappop(heap)

        # filter the invalid data
        if distance[cur] < dis:
            continue

        visited[cur] = True

        # check the adjacent nodes
        for w, adj in adjLst[cur]:
            new_dis = dis + w
            if new_dis < distance[adj]:
                # Return the function, if there's minus cycle
                if adj in path:
                    return True
                distance[adj] = new_dis
                new_path = path[:]
                new_path.append(adj)
                heapq.heappush(heap, (adj, new_dis, new_path))

    return False

if __name__ == '__main__':
    T  = int(input())

    for _ in range(T):
        N, M, W = map(int, input().split())

        # make adjacent node list
        adjLst = [[] for _ in range(N +1)]
        for _ in range(M):
            S, E, T = map(int, input().split())
            adjLst[S].append((T, E))
            adjLst[E].append((T, S))
        for _ in range(W):
            S, E, T = map(int, input().split())
            adjLst[S].append((-T, E))

        # run dijkstra for every node
        visited = [False] * (N + 1)
        for n in range(1, N + 1):
            if visited[n]:
                continue
            result = dijkstra_detect_minus_cycle(N, adjLst, n, visited)

            # print the result
            if result:
                print('YES')
                break
        else:
            print('NO')
