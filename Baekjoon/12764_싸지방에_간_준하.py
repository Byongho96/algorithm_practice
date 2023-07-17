import heapq

if __name__ == '__main__':
    N = int(input())

    people = [list(map(int, input().split())) for _ in range(N)]
    people.sort()

    num_computer = 1
    computer_used = [1] + [0] * (N - 1)  # 컴퓨터 별 사용 횟수
    end_time_heap = [(people[0][1], 0)]  # (종료시간, 컴퓨터 인덱스)
    available_computer_heap = [] # 사용 가능한 자리

    for  start, end in people[1:]:
        # 가능한 자리 확보
        while end_time_heap and end_time_heap[0][0] < start:
            _, idx = heapq.heappop(end_time_heap)
            heapq.heappush(available_computer_heap, idx)

        # 사용 가능한 자리가 있다면
        if available_computer_heap:
            idx =  heapq.heappop(available_computer_heap)
            heapq.heappush(end_time_heap, (end, idx))
            computer_used[idx] += 1
            continue

        # 사용 가능한 자리가 없다면
        heapq.heappush(end_time_heap, (end, num_computer))
        computer_used[num_computer] += 1
        num_computer += 1

    print(num_computer)
    print(*computer_used[:num_computer])
