# DFS 
def find_farthest_node(start, adjLst):
    visited = [False] * (N + 1)

    visited[start] = True
    stack= [(start, 1, 0)]

    max_node = 0    # 가장 먼 노드
    max_num = 0     # 가장 먼 노드까지의 노드갯수
    min_time = {}   # 가장 먼 노드까지의 시간(가중치), 노드 갯수별로 저장

    while stack:
        node, num, time = stack.pop(0)
        if num >= max_num:  # 가장 먼 노드까지의 노드갯수가 더 크거나 같으면
            max_num = num       # 노드 갯수 업데이트
            if not min_time.get(num) or min_time[num] > time:   # (같은 노드 갯수에 대해서) 해당 노드까지의 시간이 더 작으면
                max_node = node                                     # 노드 업데이트
                min_time[num] = time                                # 노드까지의 시간 업데이트

        for adj, w in adjLst[node]:
            if not visited[adj]:
                visited[adj] = True
                stack.append((adj, num + 1, time + w))

    return max_node, max_num, min_time[max_num] # 가장 먼 노드, 가장 먼 노드까지의 갯수, 가장 먼 노드까지의 시간


if __name__ == '__main__':
    N, T = map(int, input().split())

    # 인접리스트 생성
    # { 노드 : [(인접노드, 가중치), (인접노드, 가중치), ...], ...}
    adjLst = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        i, j, w = map(int, input().split())
        adjLst[i].append((j, w))
        adjLst[j].append((i, w))

    # 트리의 지름 구하기 
    the_farthest_node, _, _ = find_farthest_node(1, adjLst) # 임의 노드에서 가장 먼 노드를 구함
    another_farthest_node, max_num, min_time = find_farthest_node(the_farthest_node, adjLst) # 가장 먼 모드에서 다른 가장 먼 노드를 구함 

    min_date = min_time // T + 1 if min_time % T else min_time // T # 최소 시간으로 최소 날짜를 계산
    print(min_date)