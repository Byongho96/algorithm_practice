from typing import List
from collections import Counter

def solution(N, nums: List[int]) -> List[int]:
    counter = Counter(nums)

    stack = []
    answer = []
    for i in range(N - 1, -1, -1):
        num = nums[i]
        while stack and counter[stack[-1]] < counter[num] + 1:
            stack.pop()
        answer.append(stack[-1] if stack else -1)
        stack.append(num)

    return answer[::-1]


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))

    answer = solution(N, nums)
    print(*answer)

