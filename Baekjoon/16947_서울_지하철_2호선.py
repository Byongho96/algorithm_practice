def find_loop(N, start, adjLst):
    visited = [False] * (N + 1)
    stack = []

    node = start
    visited[node] = True

    while True:

        for adj in adjLst[node]:
            if not visited[adj]:
                stack.append(node)
                node = adj
                visited[node] = True
                break
            if stack and adj != stack[-1] and adj in stack:   # 반복지점을 찾는 순간
                idx = stack.index(adj)
                return stack[idx:] + [node]

        else:
            if stack:
                node = stack.pop()
            else:
                break
    
    return False

def cal_distance(N, loop, adjLst):
    visited = [-1] * (N + 1)
    stack = []

    s = loop[0]
    stack.append(s)
    visited[s] = 0

    while stack:
        node = stack.pop()

        for adj in adjLst[node]:
            if visited[adj] == - 1:
                if adj in loop:
                    visited[adj] = 0
                else:
                    visited[adj]  = visited[node] + 1
                stack.append(adj)
    
    return visited[1:]

if __name__ == "__main__":
    N = int(input())

    adjLst = [[] for _ in range(N + 1)]
    for _ in range(N):
        n1, n2 = map(int, input().split())
        adjLst[n1].append(n2)
        adjLst[n2].append(n1)

    loop = find_loop(N, 1, adjLst)
    answer = cal_distance(N, loop, adjLst)

    print(' '.join(list(map(str, answer))))