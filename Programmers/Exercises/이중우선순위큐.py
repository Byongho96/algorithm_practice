from collections import defaultdict
import heapq

def solution(operations):
    
    max_heap = []
    min_heap = []
    exist = defaultdict(int)    # 최대힙과 최소힙 동기화를 위한 기록용 dictionary
    
    for operation in operations:
        typ, num = operation.split()
        num = int(num)
        if typ == 'I':
            heapq.heappush(max_heap, -num)  # heapq는 기본적으로 최소 힙
            heapq.heappush(min_heap, num)
            exist[num] += 1
        elif num == 1:
            while max_heap and not exist[-max_heap[0]]: # 최소힙과 동기화
                heapq.heappop(max_heap)
            if max_heap:
                exist[-heapq.heappop(max_heap)] -= 1
        else:
            while min_heap and not exist[min_heap[0]]:  # 최대힙과 동기화
                heapq.heappop(min_heap)
            if min_heap:
                exist[heapq.heappop(min_heap)] -= 1
    
    while max_heap and not exist[-max_heap[0]]: # 마지막 동기화
        heapq.heappop(max_heap)
    while min_heap and not exist[min_heap[0]]:  # 마지막 동기화
        heapq.heappop(min_heap)

    if max_heap:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        return [0, 0]