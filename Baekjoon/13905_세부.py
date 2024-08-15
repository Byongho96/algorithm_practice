import sys
input = sys.stdin.readline

import heapq

INF = 10 ** 6 + 1

def solution(N, M, s, e, adjLst):
    max_visited = [0] * (N + 1)
    
    max_visited[s] = -INF
    heap = [(-INF, s)]

    while heap:
        w, cur = heapq.heappop(heap)

        if max_visited[cur] < w: # 이미 더 큰(절댓값) 가중치로 방문할 수 있는 경우
            continue

        if cur == e:
            return -w

        for nxt, nw in adjLst[cur]:
            nw = max(w, -nw)    # 더 작은(절댓값) 경우로 갱신
            if nw < max_visited[nxt]:   # 더 큰(절댓값) 가중치로 방문할 수 있는 경우
                max_visited[nxt] = nw
                heapq.heappush(heap, (nw, nxt))
    
    return 0

if __name__ == "__main__":
    N, M = map(int, input().split())
    s, e = map(int, input().split())

    adjLst = tuple([] for _ in range(N + 1))
    for _ in range(M):
        a, b, w= map(int, input().split())
        adjLst[a].append((b, w))
        adjLst[b].append((a, w))

    answer = solution(N, M, s, e, adjLst)
    print(answer)