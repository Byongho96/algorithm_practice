import sys
input = sys.stdin.readline

def floyd_warshall(N, arr):
    
    for m in range(1, N + 1):
        for s in range(1, N + 1):
            for e in range(1, N + 1):
                if arr[s][e] > arr[s][m] + arr[m][e]:
                    arr[s][e] = arr[s][m] + arr[m][e]

    return arr


if __name__ == '__main__':
    N = int(input())
    M = int(input())

    # the maximum distance
    INF = N * 100000

    # make floyd_warshall
    arr = [[INF] * (N + 1) for _ in range(N + 1)]

    # set the distance
    for _ in range(M):
        i, j, w = map(int, input().split())
        # filter the invalid data
        if w < arr[i][j]:
            arr[i][j]  = w

    for i in range(1, N + 1):
        arr[i][i] = 0

    # run floyd_warshall for every node
    floyd_warshall(N, arr)

    # print the result
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(0 if arr[i][j] == INF else arr[i][j], end= ' ')
        print()


# import heapq
# from collections import defaultdict

# import sys
# input = sys.stdin.readline

# def dijkstra(N, adjLst, start):
#     distance = [INF] * (N + 1)
#     heap = []
#     visited = 0

#     # set the start
#     distance[start] = 0
#     heapq.heappush(heap, (0, start))

#     # dijktra with heap
#     while heap:
#         dis, cur = heapq.heappop(heap)

#         # filter the invalid data
#         if distance[cur] < dis:
#             continue

#         # end condition
#         visited += 1
#         if visited == N:
#             return distance
        
#         # traverse the adjacent nodes
#         for w, adj in adjLst[cur]:
#             new_dis = dis + w
#             if new_dis < distance[adj]:
#                 distance[adj] = new_dis
#                 heapq.heappush(heap, (new_dis, adj))

#     return distance


# if __name__ == '__main__':
#     N = int(input())
#     M = int(input())

#     # the maximum distance
#     INF = N * 100000

#     # make adjacent list dictionary
#     adjLst = defaultdict(list)
#     for _ in range(M):
#         i, j, w = map(int, input().split())
#         adjLst[i].append((w, j))

#     # run dikjstra for every node
#     for start in range(1, N + 1):
#         answer = dijkstra(N, adjLst, start)
#         for i in range(1, N + 1):
#             if answer[i] == INF:
#                 answer[i] = 0
#         print(*answer[1:])