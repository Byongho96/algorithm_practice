from collections import defaultdict, deque
import sys

input = sys.stdin.readline


def topological_sort():
    # make data structure
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))

    indegree = defaultdict(int)
    adjLst = [[] for _ in range(N + 1)]
    for _ in range(K):
        i, j = map(int, input().split())
        adjLst[i].append(j)
        indegree[j] += 1

    W = int(input())

    # topological sort
    queue = deque()
    for i in range(1, N + 1):
        if not indegree[i]:
            queue.append(i)

    start_time = defaultdict(int)
    while queue:
        cur = queue.popleft()

        if cur == W:
            print(start_time[cur] + times[cur])
            return

        for adj in adjLst[cur]:
            start_time[adj] = max(start_time[adj], start_time[cur] + times[cur])
            indegree[adj] -= 1
            if not indegree[adj]:
                queue.append(adj)


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        topological_sort()
