import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)

    # Set initail data
    for _ in range(M):
        i, j = map(int, input().split())
        graph[i].append(j)
        in_degree[j] += 1

    # Set starts
    starts = [n for n, degree in enumerate(in_degree) if degree == 0]

    # Topological sort
    idx = 1
    answer = []
    while idx < N + 1:
        answer.append(starts[idx])
        for adj in graph[starts[idx]]:
            in_degree[adj] -= 1
            if in_degree[adj] == 0:
                starts.append(adj)
        idx += 1

    print(*answer)
