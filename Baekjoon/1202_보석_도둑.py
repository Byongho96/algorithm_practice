import sys
import heapq

input = sys.stdin.readline

# 1. 작은 가방 부터 시작해서
# 2. 가방에 넣을 수 있는 보석 중 가장 비싼 보석을 넣는다.
def solution(N, K, jewels, bags):
    jewels.sort() # 무게 순으로 오름차순 정렬
    bags.sort()

    sm = 0
    idx = 0
    value_heap = []
    for bag in bags:
        # 가능한 보석을 모두 힙에 넣는다.
        while idx < N and jewels[idx][0] < bag + 1:
            heapq.heappush(value_heap, -jewels[idx][1])
            idx += 1
        # 가장 비싼 보석을 꺼낸다.
        if value_heap:
            sm -= heapq.heappop(value_heap)

    return sm

if __name__ == "__main__":
    N, K = map(int, input().split())

    jewels = [list(map(int, input().split())) for _ in range(N)]
    bags = [int(input()) for _ in range(K)]

    answer = solution(N, K, jewels, bags)
    print(answer)