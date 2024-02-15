from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = 0
        curMin = 0
        mx = nums[0]
        mn = nums[0]

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            mx = max(mx, curMax)
            mn = min(mn, curMin)

        # 최대 subArray / 전체 값 - 최소 subArray 
        return mx if mx < 0 else max(mx, sum(nums) - mn)

solution = Solution()
print(solution.maxSubarraySumCircular([-3,-2,-3]))