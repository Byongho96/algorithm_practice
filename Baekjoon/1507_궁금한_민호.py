import sys

input = sys.stdin.readline


def reverse_floyd_warshall(N, dist):
    # set to record the rodas to be deleted_roads
    # too prevent empty set
    deleted_roads = set([1])
    for m in range(N):
        for s in range(N):
            for e in range(s + 1, N):  # half the arr
                # case1: impossible case
                if dist[s][e] > dist[s][m] + dist[m][e]:
                    return False
                # case2: delete meaningless road, should not be delete right away to avoid error in case1
                if s != m != e and dist[s][e] == dist[s][m] + dist[m][e]:
                    deleted_roads.add((s, e))
    return deleted_roads


if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    deleted_roads = reverse_floyd_warshall(N, arr)

    if deleted_roads:
        answer = 0
        for i in range(N):
            for j in range(i + 1, N):  # half the arr
                if (i, j) in deleted_roads:
                    continue
                answer += arr[i][j]
        print(answer)
    else:
        print(-1)
