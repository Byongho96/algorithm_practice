import sys
from collections import defaultdict, deque

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())

    answer = 0

    cul = 0
    friends = deque()
    name_len_dict = defaultdict(int)
    for _ in range(N):
        # delete the friend
        if cul == M + 1:
            name = friends.popleft()

            # update record
            name_len_dict[len(name)] -= 1
            cul -= 1

        # add the friend
        name = input().rstrip()
        friends.append(name)

        answer += name_len_dict[len(name)]

        # update record
        name_len_dict[len(name)] += 1
        cul += 1

    print(answer)
