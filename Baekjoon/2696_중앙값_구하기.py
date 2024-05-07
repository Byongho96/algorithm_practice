
import heapq
import sys
input = sys.stdin.readline

def solution(N, nums):
    min_heap = []
    max_heap = [-nums[0]]
    mid = [nums[0]]

    for i in range(1, N):
        num = nums[i]

        if num < mid[-1]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        # balance the heaps : max 에 하나가 더 많도록
        if len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        elif len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        # find the mid
        if i % 2 == 0:
            mid.append(-max_heap[0])

    answer = []
    for i in range(len(mid) // 10 + 1):
        answer.append(' '.join(map(str, mid[i * 10: (i + 1) * 10])))
    return answer


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        N = int(input())
        nums = []
        for _ in range(N // 10 + 1):
            nums.extend(map(int, input().split()))

        answer = solution(N, nums)

        print(N // 2 + 1, *answer, sep='\n')
