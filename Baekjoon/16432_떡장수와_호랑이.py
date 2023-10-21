import sys

sys.setrecursionlimit(10**4)  # 1000 * 9
input = sys.stdin.readline


def backtracking(N, n, adjLst, visited, yesterday, path):
    global answer, is_end
    # pruning
    if is_end:
        return

    # end condition
    if n == N:
        answer = path[:]
        is_end = True
        return

    # traverse adjacent
    for adj in adjLst[n][1:]:
        if adj == yesterday:
            continue
        if visited[n][adj]:
            continue
        path.append(adj)
        visited[n][adj] = True
        backtracking(N, n + 1, adjLst, visited, adj, path)
        path.pop()


def main():
    global answer, is_end

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * 10 for _ in range(N)]

    answer = None
    is_end = False
    backtracking(N, 0, arr, visited, 0, [])

    if answer:
        print(*answer, sep="\n")
    else:
        print(-1)


if __name__ == "__main__":
    main()
