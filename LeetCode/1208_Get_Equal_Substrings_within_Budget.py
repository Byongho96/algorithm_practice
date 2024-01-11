class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)

        # Make diff array
        diff = [0] * N
        for i in range(N):
            diff[i] = abs(ord(s[i]) - ord(t[i]))

        # two pointer
        s, e = 0, 0
        curLen, maxLen = 0, 0
        curCost = 0
        while s < N and e < N:
            curCost += diff[e]
            curLen += 1

            # Move start
            while curCost > maxCost:
                curCost -= diff[s]
                s += 1
                curLen -= 1

            # Move End
            maxLen = max(maxLen, curLen)
            e += 1

        return maxLen
