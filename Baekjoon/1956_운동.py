import sys, heapq

input = sys.stdin.readline


def find_min_cycle(V, adjLst):
    INF = 10000 * V * 2
    distance = tuple([INF] * (V + 1) for _ in range(V + 1))

    # set the start
    heap = []
    for start in range(1, V + 1):
        for w, next in adjLst[start]:
            heapq.heappush(heap, (w, next, start))
            distance[start][next] = w

    while heap:
        w, cur, start = heapq.heappop(heap)

        # filter invalid
        if distance[start][cur] < w:
            continue

        # find the answer
        if cur == start:
            return w

        # traverse adjacent
        for adj_w, adj in adjLst[cur]:
            new_weight = w + adj_w
            if new_weight < distance[start][adj]:
                distance[start][adj] = new_weight
                heapq.heappush(heap, (new_weight, adj, start))

    return False


if __name__ == "__main__":
    V, E = map(int, input().split())

    # make adjacent nodes
    adjLst = tuple([] for _ in range(V + 1))
    for _ in range(E):
        i, j, w = map(int, input().split())
        adjLst[i].append((w, j))

    # find the minimum answer
    answer = find_min_cycle(V, adjLst)
    print(answer if answer else -1)
