from collections import deque


def solution(priorities, location):
    record = [0] * 10
    queue = deque()

    for index, priority in enumerate(priorities):
        queue.append((priority, index))
        record[priority] += 1

    cnt = 0
    r_idx = 9
    while queue:
        # find the current max priority
        while not record[r_idx]:
            r_idx -= 1

        # pop the process
        priority_index = queue.popleft()

        # run the process
        if priority_index[0] == r_idx:
            record[r_idx] -= 1
            cnt += 1

            # find the answer
            if priority_index[1] == location:
                return cnt

            continue

        # re-push the process
        queue.append(priority_index)
