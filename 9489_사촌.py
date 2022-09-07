# 1452ms
import sys
input = sys.stdin.readline

while True:
    N, K = map(int, input().split())
    if not (N or K):
        break
    nums = list(map(int, input().split()))

    # nums   = [1  3  4  5  8  9  15  30  31  32]
    # parent = [-1 0  0  0  1  1  2   3   3   3]
    # parent 리스트 만들기(인덱스 값을 기준으로)
    parent = [[] for _ in range(N)]
    parent[0] = -1
    parent_node = -1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1] + 1:
            parent_node += 1
        parent[i] = parent_node

    # 사촌 찾기
    k_idx = nums.index(K)   # 15 -> 6
    cnt =0
    for n in range(N):
        if parent[parent[n]] == parent[parent[k_idx]] and parent[n] != parent[k_idx]:
            cnt += 1

    print(cnt)

