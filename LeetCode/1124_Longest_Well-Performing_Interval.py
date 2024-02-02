from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        min_idx = {}
        ans, sm = 0, 0

        # cululative sum
        for idx, hour in enumerate(hours):
            sm += 1 if hour > 8 else -1
            min_idx[sm] = min_idx.get(sm, idx)

            if sm > 0:
                # longest day
                ans = idx + 1
            else:
                # find longest day
                ans = max(ans, idx - min_idx.get(sm - 1, idx))

        return ans
