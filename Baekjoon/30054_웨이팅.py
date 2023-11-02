import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    time_list = [list(map(int, input().split())) for _ in range(N)]

    # sort by arrive -> reserve
    time_list.sort(key=lambda x: (x[1], x[0]))

    # check the person arrived earlier than reservation
    book = dict()
    for i in range(N):
        reserve, arrive = time_list[i]
        if arrive < reserve + 1:
            book[reserve] = (i, arrive)

    mx = 0
    idx = 0
    time = time_list[0][1]
    visited = [False] * N
    while idx < N:
        reserve, arrive = time_list[idx]

        # if already entered
        if visited[idx]:
            idx += 1
            continue

        # if there's reservation
        reserve_idx, reserve_arrive = book.get(time, (None, None))
        if reserve_idx and not visited[reserve_idx]:
            mx = max(mx, time - reserve_arrive)
            visited[reserve_idx] = True
            time += 1
            continue

        # if not arrived
        if time < arrive:
            time = arrive
            continue

        visited[idx] = True
        mx = max(mx, time - arrive)
        idx += 1
        time += 1

    print(mx)
