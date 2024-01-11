import heapq


def solution(food_times, k):
    # filter invalid
    if sum(food_times) < k + 1:
        return -1

    # simulation by time
    heap = []
    for idx, time in enumerate(food_times):
        heapq.heappush(heap, (time, idx))

    n = len(food_times)
    prev_time = 0
    answer = 0
    while heap:
        time = (heap[0][0] - prev_time) * n

        if k > time:
            prev_time, _ = heapq.heappop(heap)
            k -= time
            n -= 1
            continue

        k %= n
        heap.sort(key=lambda x: x[1])
        answer = heap[k][1]
        break

    return answer + 1


solution([3, 1, 2], 5)
