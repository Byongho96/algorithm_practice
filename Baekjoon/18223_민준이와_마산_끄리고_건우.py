import heapq
import sys
input = sys.stdin.readline

def solution(V, E, P, adjLst):
    INF = 10000 * V
    distance = [INF] * (V + 1)

    distance[1] = 0
    heap = [(0, 1, False)]
    mn_dis = INF
    while heap:
        dis, cur, is_picked = heapq.heappop(heap)

        if dis > mn_dis:
            return False

        if distance[cur] < dis:
            continue

        if cur == P:
            is_picked = True

        if cur == V:
            mn_dis = min(mn_dis, dis)
            if is_picked:
                return True

        for w, adj in adjLst[cur]:
            new_dis = dis + w
            if distance[adj] > new_dis - 1:
                distance[adj] = new_dis
                heapq.heappush(heap, (new_dis, adj, is_picked))
    
    return False


if __name__ == "__main__":
    V, E, P = map(int, input().split())
     
    adjLst = [[] for _ in range(V + 1)]
    for _ in range(E):
        i, j, w = map(int, input().split())
        adjLst[i].append((w, j))
        adjLst[j].append((w, i))

    answer = solution(V, E, P, adjLst)
    print('SAVE HIM' if answer else 'GOOD BYE')
