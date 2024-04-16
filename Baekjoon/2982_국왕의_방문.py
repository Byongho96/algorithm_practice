import sys
import heapq
from typing import List, Tuple

input = sys.stdin.readline

def get_current_occupied(occupied: List[int], order:Tuple[int], time: int) -> Tuple[int, int, int]:
    for i in range(len(occupied)):
        if time < occupied[i]:
            return order[i - 1], order[i], occupied[i] - time
        
    return -1, -1, 0

def solution(N: int, M: int, start: int, dest: int, offset: int, K: int, occupied: List[int], order: Tuple[int], adjLst: List[Tuple[int, int]] ): 
    INF = 1000 * N
    distance = [INF] * (N + 1)
    distance[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, cur = heapq.heappop(heap)

        # filter invalid
        if distance[cur] < dist:
            continue

        # end condition
        if cur == dest:
            return dist

        # current occupied road
        v1, v2, waiting_itme = get_current_occupied(occupied, order, dist + offset)

        for w, nxt in adjLst[cur]:
            if (cur == v1 and nxt == v2) or (nxt == v1 and cur == v2):
                w += waiting_itme
            if distance[nxt] > w + dist:
                distance[nxt] = w + dist
                heapq.heappush(heap, (w + dist, nxt))

    answer = distance[dest]
    return answer

if __name__ == "__main__":
    N, M = map(int, input().split())
    start, dest, offset, K = map(int, input().split())

    order = tuple(map(int, input().split()))
    occupied = [0] * (K)
    adjLst = [[] for _ in range(N + 1)]
    for _ in range(M):
        i, j, w = map(int, input().split())
        adjLst[i].append((w, j))
        adjLst[j].append((w, i))

        if i in order and j in order and abs(order.index(i) - order.index(j)) == 1:
            idx = max(order.index(i), order.index(j))
            occupied[idx] = w

    for i in range(1, K):
        occupied[i] += occupied[i - 1]
   
    answer = solution(N, M, start, dest, offset, K, occupied, order, adjLst)
    print(answer)