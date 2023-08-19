import heapq
from collections import defaultdict

# dijkstra which can handle minus cycle
def dijkstra_with_minus_cycle(N, adjLst, start):
    distance = [INF] * (N + 1)
    heap = []

    # set the start point
    distance[start] = 0
    heapq.heappush(heap, (start, 0, [0])) # path is for the tracking minus cycle

    while heap:
        cur, dis, path = heapq.heappop(heap)

        # filter the invalid data
        if distance[cur] < dis:
            continue

        # check the adjacent nodes
        for w, adj in adjLst[cur]:
            new_dis = dis + w
            if new_dis < distance[adj]:
                # Return the function, if there's minus cycle
                if adj in path:
                    return False
                distance[adj] = new_dis
                new_path = path[:]
                new_path.append(adj)
                heapq.heappush(heap, (adj, new_dis, new_path))

    return distance

if __name__ == '__main__':
    N, M = map(int, input().split())
    INF = N * 10000

    # make adjacent node list dictionary
    adjLst = defaultdict(list)
    for _ in range(M):
        i, j, w = map(int, input().split())
        adjLst[i].append((w, j))

    # run dijkstra
    distance = dijkstra_with_minus_cycle(N, adjLst, 1)

    # print the result
    if distance:
        for dis in distance[2:]:
            print(dis if dis != INF else -1)
    else:
        print(-1)