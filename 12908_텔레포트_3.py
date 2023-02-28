from collections import defaultdict
import heapq

def bfs_backtracking(x, y):
    global mn

    visited = defaultdict(int)
    q = [(1, x, y)]
    visited[(x, y)] = 1

    while q:
        n, x, y = heapq.heappop(q)
        # 종료조건
        if x == xe and y == ye:
            mn = min(mn, n)
            continue
        # 가지치기
        if n >= mn:
            break
        # 후보군 출력
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx <= 1000000000 and 0 <= ny <= 1000000000 and (not visited[(nx, ny)] or visited[(nx, ny)] > n + 1):
                heapq.heappush(q, (n+1, nx, ny))
                visited[(nx, ny)] = n + 1

        if (x, y) in teleport1:
            index = teleport1.index((x ,y))
            nx, ny = teleport2[index]
            if (not visited[(nx, ny)] or visited[(nx, ny)] > n + 10):
                heapq.heappush(q, (n+10, nx, ny))
                visited[(nx, ny)] = n + 10

        elif (x, y) in teleport2:
            index = teleport2.index((x ,y))
            nx, ny = teleport1[index]
            if (not visited[(nx, ny)] or visited[(nx, ny)] > n + 10):
                heapq.heappush(q, (n+10, nx, ny))
                visited[(nx, ny)] = n + 10

xs, ys = map(int, input().split())
xe, ye = map(int, input().split())

teleport1 = []
teleport2 = []

for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    teleport1.append((x1, y1))
    teleport2.append((x2, y2))

mn = 2000000000
bfs_backtracking(xs, ys)
print(mn-1)




# from collections import defaultdict
# import heapq

# def bfs_backtracking(x, y):
#     global mn

#     q = []
#     q.append((x, y))

#     visited = defaultdict(int)
#     visited[(x, y)] = 1

#     while q:
#         n, x, y = heapq.heappop()
#         n = visited[(x, y)]
#         # 종료조건
#         if x == xe and y == ye:
#             mn = min(mn, n)
#             continue
#         # 가지치기
#         if n >= mn - 1:
#             continue
#         # 후보군 출력
#         for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
#             nx = x + dx
#             ny = y + dy
#             if 0 <= nx <= 1000000000 and 0 <= ny <= 1000000000 and (not visited[(nx, ny)] or visited[(nx, ny)] > n + 1):
#                 q.append((nx, ny))
#                 visited[(nx, ny)] = n + 1

#         if (x, y) in teleport1:
#             index = teleport1.index((x ,y))
#             nx, ny = teleport2[index]
#             if (not visited[(nx, ny)] or visited[(nx, ny)] > n + 10):
#                 q.append((nx, ny))
#                 visited[(nx, ny)] = n + 10

#         elif (x, y) in teleport2:
#             index = teleport2.index((x ,y))
#             nx, ny = teleport1[index]
#             if (not visited[(nx, ny)] or visited[(nx, ny)] > n + 10):
#                 q.append((nx, ny))
#                 visited[(nx, ny)] = n + 10

#     return visited[(xe, ye)] - 1

# xs, ys = map(int, input().split())
# xe, ye = map(int, input().split())

# teleport1 = []
# teleport2 = []

# for _ in range(3):
#     x1, y1, x2, y2 = map(int, input().split())
#     teleport1.append((x1, y1))
#     teleport2.append((x2, y2))

# mn = 2000000000
# print(bfs_backtracking(xs, ys))