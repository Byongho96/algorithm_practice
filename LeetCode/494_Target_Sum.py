from typing import List
from collections import defaultdict


class Solution:
    def __backtracking(self, n: int, value: int) -> int:
        # Base condition
        if n == self.N:
            if value == self.target:
                return 1
            else:
                return 0

        # Fill memoization
        key1 = (n + 1, value + self.nums[n])
        key2 = (n + 1, value - self.nums[n])
        if key1 not in self.memoization:
            self.memoization[key1] = self.__backtracking(*key1)
        if key2 not in self.memoization:
            self.memoization[key2] = self.__backtracking(*key2)

        return self.memoization[key1] + self.memoization[key2]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.N = len(nums)
        self.nums = nums
        self.target = target

        # memoization array
        self.memoization = {}

        # fill the memoization array
        answer = self.__backtracking(0, 0)

        # return answer
        return answer
