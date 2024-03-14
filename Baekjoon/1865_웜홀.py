import sys, heapq

input = sys.stdin.readline


INF = 10001 * 500

def check_minus_cycle_with_dijkstra(N, adjLst):
    distance = [INF] * (N + 1)

    # check all the nodes
    for start in range(1, N + 1):
        # skip duplication
        if distance[start] != INF:
            continue

        """
        Dikjstra algorithm checking binary path
        """
        # set the start
        heap = [(0, start, 1 << start)]  # (distance, current node, visited_path)
        distance[start] = 0

        while heap:
            dist, cur, path = heapq.heappop(heap)

            # filter invalid
            if distance[cur] < dist:
                continue

            # check the adjacent nodes
            for weight, adj in adjLst[cur]:
                if dist + weight < distance[adj]:
                    
                    # check whether it's already visited node
                    if path >> adj & 1:
                        return True
                    
                    distance[adj] = dist + weight
                    heapq.heappush(heap, (dist + weight, adj, path | 1 << adj))

    return False




if __name__ == "__main__":
    for _ in range(int(input())):
        """
        N: the num of nodes <= 500
        M: the num of edges <= 2500
        W: the num of wormholes <= 200
        """
        N, M, W = map(int, input().split())
        adjLst = [[] for _ in range(N + 1)]

        # get roads info
        for _ in range(M):
            start, end, time = map(int, input().split())
            adjLst[start].append((time, end))
            adjLst[end].append((time, start))

        # get worholes info
        for _ in range(W):
            start, end, time = map(int, input().split())
            adjLst[start].append((-time, end))

        answer =  check_minus_cycle_with_dijkstra(N, adjLst)
        print('YES' if answer else 'NO')
        
        


        


# """
# 모든 지점이 연결되어있다는 조건이 없기 때문에

# (음의 경로를 추적하는) Dijkstra로 풀 경우, 모든 노드 군집에 대해서 실행해야함
# """

# import sys

# input = sys.stdin.readline

# import heapq


# # dijkstra which can handle minus cycle
# def dijkstra_detect_minus_cycle(N, adjLst, start, visited):
#     INF = 10001 * N
#     distance = [INF] * (N + 1)
#     heap = []

#     # set the start point
#     distance[start] = 0
#     path = 1  # bit data which record the nodes been visted
#     heapq.heappush(heap, (start, 0, path))

#     while heap:
#         cur, dis, path = heapq.heappop(heap)

#         # filter the invalid data
#         if distance[cur] < dis:
#             continue

#         visited[cur] = True

#         # check the adjacent nodes
#         for w, adj in adjLst[cur]:
#             new_dis = dis + w
#             if new_dis < distance[adj]:
#                 # Return the function, if there's minus cycle
#                 if path >> adj & 1:
#                     return True
#                 distance[adj] = new_dis
#                 new_path = path | 1 << adj
#                 heapq.heappush(heap, (adj, new_dis, new_path))

#     return False


# if __name__ == "__main__":
#     T = int(input())

#     for _ in range(T):
#         N, M, W = map(int, input().split())

#         # make adjacent node list
#         adjLst = [[] for _ in range(N + 1)]
#         for _ in range(M):
#             S, E, T = map(int, input().split())
#             adjLst[S].append((T, E))
#             adjLst[E].append((T, S))
#         for _ in range(W):
#             S, E, T = map(int, input().split())
#             adjLst[S].append((-T, E))

#         # run dijkstra for every node
#         visited = [False] * (N + 1)
#         for n in range(1, N + 1):
#             if visited[n]:
#                 continue
#             result = dijkstra_detect_minus_cycle(N, adjLst, n, visited)

#             # print the result
#             if result:
#                 print("YES")
#                 break
#         else:
#             print("NO")
