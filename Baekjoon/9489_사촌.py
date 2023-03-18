while True:
    N, target = map(int, input().split())

    if N==0:    # 종료 조건
        break

    nums = [0] + list(map(int, input().split()))    # 리스트 첫번째 노드에 0을 추가

    # 숫자에 대한 인덱스를 파악할 수 있는 딕셔너리 작성
    # [0, 1, 5, 11] = { 1: 1, 5: 2, 11: 3}
    num_to_index = {}
    for idx in range(1, N + 1):
        num_to_index[nums[idx]] = idx

    # 각 노드 "인덱스"에 대한 부모 노드 "인덱스"
    parents = [0] * (N + 1)
    parent = 0
    for idx in range(2, N + 1):
        if nums[idx] > nums[idx -1] + 1:
            parent += 1
        parents[idx] = parent

    # 사촌 찾기
    cousins = 0
    parent = parents[num_to_index[target]]
    grand_parent = parents[parent]

    if grand_parent == 0:   # 할아버지 노드가 0 이면 존재하지 않음
        print(0)
        continue

    for idx in range(N + 1):
        if parents[idx] != parent and parents[parents[idx]] == grand_parent:
            cousins += 1

    print(cousins) # 자기 자신은 제외

# # 1104ms
# import sys
# input = sys.stdin.readline

# while True:
#     N, K = map(int, input().split())
#     if not N:
#         break

#     item = list(map(int, input().split()))
#     L = len(item)
#     par = [-1] * L

#     par_ptr = -1
#     for i in range(1, L):
#         if item[i] > item[i-1] + 1:
#             par_ptr += 1
#         par[i] = par_ptr

#     idx = item.index(K)
#     grand_pr = par[par[idx]]
#     pr = par[idx]
#     cnt = 0
#     for i in range(1, N):
#         if par[par[i]] == grand_pr and par[i] != pr:
#             cnt += 1

#     print(cnt)