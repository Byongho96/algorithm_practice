import sys
from collections import deque

input = sys.stdin.readline


def main(N: int, string: str):
    OFFSET = ord("a")
    TOTAL = ord("z") - OFFSET + 1

    cnt = [0] * TOTAL
    queue_list = [deque() for _ in range(TOTAL)]

    mn, mx = 10001, 0
    for i, chr in enumerate(string):
        n = ord(chr) - OFFSET

        # update data
        cnt[n] += 1
        queue_list[n].append(i)

        # update answer
        if cnt[n] > N - 1:
            first = queue_list[n].popleft()
            mn = min(mn, i - first + 1)
            mx = max(mx, i - first + 1)

    if not mx:
        print(-1)
    else:
        print(mn, mx)


if __name__ == "__main__":
    for _ in range(int(input())):
        string = input().rstrip()
        N = int(input())
        main(N, string)
