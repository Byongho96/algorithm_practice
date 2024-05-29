import sys
import heapq
input = sys.stdin.readline

INF = 1000 * 100000 + 1

def solution(N, M, adjLst, S, E):
    distance = [INF] * (N + 1)
    par = [0] * (N + 1)

    # set the start
    distance[S] = 0
    heap = [(0, S)]
    par[S] = 0

    # dijkstra
    while heap:
        dis, cur = heapq.heappop(heap)

        if distance[cur] < dis:
            continue
    
        if cur == E:
            break

        for weight, adj in adjLst[cur]:
            if dis + weight < distance[adj]:
                distance[adj] = dis + weight
                heapq.heappush(heap, [distance[adj], adj])
                par[adj] = cur


    path = []
    point = E
    while point:
        path.append(point)
        point = par[point]

    return (distance[E], len(path), ' '.join(map(str, path[::-1])))




if __name__ == "__main__":
    N = int(input())
    M = int(input())
    adjLst = [[]for _ in range(N + 1)]
    for _ in range(M):
        i, j, w = map(int, input().split())
        adjLst[i].append([w, j])
    S, E = map(int, input().split())

    answer = solution(N, M, adjLst, S, E)
    print(*answer, sep='\n')