import sys
import heapq
from typing import List
input = sys.stdin.readline

def solution(N: int, arr:List[int]) -> List[int]:
    min_heap = []
    max_heap = [-arr[0]]
    mid = [arr[0]]


    for i in range(1, N):
        num = arr[i]

        if num < mid[-1]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        # balance the heaps
        if len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        elif len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        # find the mid
        mid.append(-max_heap[0])

    return mid

if __name__ =="__main__":
    N = int(input())
    arr = [int(input()) for _ in range(N)]

    answer =solution(N, arr)
    print(*answer, sep='\n')