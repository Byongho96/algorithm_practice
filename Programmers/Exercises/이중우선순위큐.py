import heapq
from collections import defaultdict


def solution(operations):
    min_heap = []
    max_heap = []
    existing = defaultdict(int)

    for operation in operations:
        typ, num = operation.split()
        num = int(num)

        # insert number
        if typ == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            existing[num] += 1

        # delete max number
        elif num == 1:
            # synchronize before deletion
            while max_heap and not existing[-max_heap[0]]:
                heapq.heappop(max_heap)
            if max_heap:
                existing[-heapq.heappop(max_heap)] -= 1

        # delete min number
        else:
            # synchronize before deletion
            while min_heap and not existing[min_heap[0]]:
                heapq.heappop(min_heap)
            if min_heap:
                existing[heapq.heappop(min_heap)] -= 1

    # synchronization
    while max_heap and not existing[-max_heap[0]]:
        heapq.heappop(max_heap)
    while min_heap and not existing[min_heap[0]]:
        heapq.heappop(min_heap)

    # return answer
    if max_heap:
        return [-max_heap[0], min_heap[0]]
    else:
        return [0, 0]
