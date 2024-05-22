class Solution:
    INF = 2 * (10 ** 4) + 1
    OFFSET = 10 ** 4

    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # selection sort
        selection = [0] * self.INF
        for num in nums:
            selection[num + self.OFFSET] += 1

        # find answer
        cum = 0
        for num in range(self.INF - 1, -1, -1):
            cum += selection[num]
            if cum > k - 1:
                return num - self.OFFSET 