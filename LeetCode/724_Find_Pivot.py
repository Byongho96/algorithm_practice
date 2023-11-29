class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)

        # find the pivot
        for i in range(len(nums)):
            right -= nums[i]

            # if found
            if left == right:
                return i

            left += nums[i]

        # can't find
        return -1
