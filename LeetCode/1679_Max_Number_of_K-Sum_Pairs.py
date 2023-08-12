class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        answer = 0

        # Sort the nums
        nums.sort()

        # Set the initial two pointer
        N = len(nums)
        i, j = 0, N-1

        # Two pointer
        while i < j:
            sm = nums[i] + nums[j]
            if sm == k:
                answer += 1
                i += 1
                j -= 1
            elif sm < k:
                i += 1
            else:
                j -= 1
        
        return answer
                