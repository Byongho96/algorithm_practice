import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, R = map(int, input().rstrip().split())
    adjLst = [[] for _ in range(N + 1)]
    for _ in range(N-1):
        a, b, d = map(int, input().split())
        adjLst[a].append((b, d))
        adjLst[b].append((a, d))

    # 트리는 정의 상, 순환구조를 가지지 않기 때문에 dfs도 가능하다
    distance= [0] * (N + 1)
    stack = []

    distance[R] = 1 
    stack.append(R)

    G = 0
    found_G = False

    # Case 1: 기가노드가 루트노드인 경우
    if len(adjLst[R]) > 1:
        G = R
        found_G = True

    max_distance = 1
    while stack:
        node = stack.pop()

        if not found_G and len(adjLst[node]) > 2:
            G = node
            found_G = True

        for adj, weight in adjLst[node]:
            if not distance[adj]:
                distance[adj] = distance[node] + weight
                max_distance = max(distance[adj], max_distance)
                stack.append(adj)

    # Case 2: 기가노드가 리프노드인 경우
    if not found_G:
        print(max_distance - 1, 0)
    else:
        print(distance[G] - 1, max_distance - distance[G])




# # 912ms
# from collections import deque
# import sys
# input = sys.stdin.readline

# N, R = map(int, input().split())
# adjLst = [[] for _ in range(N + 1)]
# for _ in range(N-1):
#     a, b, d = map(int, input().split())
#     adjLst[a].append((b, d))
#     adjLst[b].append((a, d))

# def bfs(rt, dis):
#     distance = [-1] * (N + 1)
#     q = deque()

#     distance[rt] = dis
#     q.append(rt)

#     trunk, branch = 0, 0
#     flag = 0

#     if len(adjLst[rt]) > 1:
#         flag = 1

#     while q:
#         v = q.popleft()
#         if not flag and len(adjLst[v]) > 2:
#             trunk = distance[v]
#             flag = 1
#         for w in adjLst[v]:
#             if distance[w[0]] == -1:
#                 q.append(w[0])
#                 distance[w[0]] = distance[v] + w[1]

#     if not flag:
#         trunk = max(distance)
#     branch = max(distance) - trunk
#     return trunk, branch

# trunk, branch = bfs(R, 0)
# print(trunk, branch)