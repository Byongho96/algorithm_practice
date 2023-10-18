import sys
from collections import defaultdict

input = sys.stdin.readline


def count_sub_sum_mod_by_M(M, nums):
    remain_prefix = defaultdict(int)

    count = 0
    remain = 0
    for num in nums:
        remain = (remain + num) % M
        remain_prefix[remain] += 1

        # update count referring prefix
        count += remain_prefix[remain]

        # adjust value
        if remain:
            count -= 1

    return count


if __name__ == "__main__":
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    answer = count_sub_sum_mod_by_M(M, nums)
    print(answer)
