import sys, heapq

input = sys.stdin.readline


def dijkstra(N, INF, adjLst, start):
    distance = [INF] * (N + 1)

    # Set the start point
    heap = [(0, start)]
    distance[start] = 0

    while heap:
        dist, cur = heapq.heappop(heap)

        if distance[cur] < dist:
            continue

        for w, adj in adjLst[cur]:
            new_dist = dist + w
            if new_dist < distance[adj]:
                distance[adj] = new_dist
                heapq.heappush(heap, (new_dist, adj))

    return distance


if __name__ == "__main__":
    for _ in range(int(input())):
        # Get input
        N, M = map(int, input().split())
        adjLst = [[] for _ in range(N + 1)]
        for _ in range(M):
            i, j, w = map(int, input().split())
            adjLst[i].append((w, j))
            adjLst[j].append((w, i))
        K = int(input())
        friends = list(map(int, input().split()))

        # Maximum value
        INF = 1000 * N * K

        # Run dijkstra
        distances = []
        for friend in friends:
            distances.append(dijkstra(N, INF, adjLst, friend))

        # Determine the room
        room = 0
        min_distance = INF
        for n in range(1, N + 1):
            case = 0
            for distance in distances:
                case += distance[n]
            if case < min_distance:
                min_distance = case
                room = n

        print(room)
