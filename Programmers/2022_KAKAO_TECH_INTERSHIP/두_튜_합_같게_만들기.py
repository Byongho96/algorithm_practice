def solution(queue1, queue2):
    # remember the queue1 length
    Q1 = len(queue1)
    sm = sum(queue1)

    # merge the queues
    queue1.extend(queue2)
    Q = len(queue1)
    SUM = sum(queue1)

    # filter the invalid case
    if SUM % 2:
        return -1
    SUM //= 2

    # two pointer
    # WARNING: The end condition is not the one iteration
    start, end = 0, Q1 - 1
    answer = 0
    for _ in range(2 * Q):
        if sm < SUM:
            end = (end + 1) % Q
            answer += 1
            sm += queue1[end]
        elif sm > SUM:
            sm -= queue1[start]
            start = (start + 1) % Q
            answer += 1
        else:
            return answer

    return -1
