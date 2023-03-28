from collections import deque

def shortest_round_path(N, adjLst, start, end):
    going_path = [] # 가는 길 저장

    distance = 0    # 총 거리

    for _ in range(2):  # 2번의 bfs
        visited = [[] for _ in range(N + 1)] 
        queue = deque()

        visited[start] = []
        queue.append(start)

        while queue:
            node = queue.popleft()

            if node == end: # 도착하면 거리 더해서 끝내기
                going_path = visited[node]
                distance += len(going_path)
                break

            for adj in adjLst[node]:    # 사전순으로 정렬되어 있는 adjLst 탐색
                if not visited[adj] and not (adj in going_path):
                    visited[adj] = visited[node] + [adj]
                    queue.append(adj)

        start, end = end, start # 시작점, 끝지점 바꾸기
    
    return  distance

if __name__ == "__main__":
    N, E = map(int, input().split())    # 노드 갯수, 간선 갯수
    
    adjLst=[[] for _ in range(N + 1)]    # 인접 리스트 딕셔너리 만들기
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adjLst[n1].append(n2)
        adjLst[n2].append(n1)
    for lst in adjLst:          # 인접 리스트 정렬
        lst.sort()

    start, end = map(int, input().split())  # 시작점, 마지막점

    answer = shortest_round_path(N, adjLst, start, end)
    print(answer)

# from collections import deque
# import sys
# input = sys.stdin.readline

# # 156ms
# def bfs(s, e, path):
#     visited = [0] * (N + 1)
#     if path:
#         for v in path[1:]:
#             visited[v] = 1
#     visited[s] = [s]

#     q = deque()
#     q.append(s)
#     while q:
#         v = q.popleft()
#         for w in adjLst[v]:
#             if not visited[w]:
#                 if w == e:
#                     return visited[v]
#                 visited[w] = visited[v] + [w]
#                 q.append(w)



# N, M = map(int, input().split())
# adjLst = [[] for _ in range(N+1)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     adjLst[a].append(b)
#     adjLst[b].append(a)

# for node in range(1, N + 1):
#     adjLst[node].sort()

# S, E = map(int, input().split())
# going_path = bfs(S, E, [])
# coming_path = bfs(S, E, going_path)
# print(len(going_path) + len(coming_path))