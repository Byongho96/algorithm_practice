import sys
input = sys.stdin.readline


def solution(n, paths, gates, summits):

    def backtracking(v):
        nonlocal mx_intensity
        nonlocal the_summit
        # 종료조건
        if v in gates:
            if visited[v] < mx_intensity:
                mx_intensity = visited[v]
                the_summit = summit
            return
        # 가지치기
        if visited[v] > mx_intensity:
            return
        elif mx_intensity == mn_intensity:
            return
        # 후보군 출력
        for w in adjLst[v]:
            if not (visited[w[0]] or w[0] in summits) :
                visited[w[0]] = max(visited[v], w[1])
                backtracking(w[0])
                visited[w[0]] = 0

    adjLst = [[] for _ in range(n + 1)]
    mn_intensity = 10000001
    for path in paths:
        a, b, d = path[0], path[1], path[2]
        adjLst[a].append((b, d))
        adjLst[b].append((a, d))
        if d < mn_intensity:
            mn_intensity = d

    mx_intensity = 10000001
    the_summit = 0
    for summit in summits:
        visited = [0] * (n + 1)
        visited[summit] = 1
        backtracking(summit)
        if mx_intensity == mn_intensity:
            break

    answer = [the_summit, mx_intensity]
    return answer

print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))