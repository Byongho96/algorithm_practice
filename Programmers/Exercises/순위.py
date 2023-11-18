def dfs(N, start, adjLst):
    visited = [False] * (N + 1)
    stack = []

    # set the start
    visited[start] = True
    stack.extend([(1, start), (-1, start)])

    # dfs
    cnt = 1
    while stack:
        d, cur = stack.pop()

        # traverse the adjacents
        for adj_d, adj in adjLst[cur]:
            if visited[adj]:
                continue
            if adj_d != d:
                continue
            visited[adj] = True
            stack.append((adj_d, adj))

            # check the end condition
            cnt += 1
            if cnt == N:
                return True

    return False


def solution(n, results):
    adjLst = [[] for _ in range(n + 1)]
    for win, loose in results:
        adjLst[win].append((1, loose))  # plus weight for winning
        adjLst[loose].append((-1, win))  # minus weight for loosing

    # dfs for every node: O(N**2)
    answer = 0
    for i in range(1, n + 1):
        answer += 1 if dfs(n, i, adjLst) else 0

    return answer
