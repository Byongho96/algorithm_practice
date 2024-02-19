class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_set = set()
        idx = 0
        cur = 0
        mx = 0
        

        for c in s:
            if c in c_set:
                while c in c_set:
                    c_set.remove(s[idx])
                    idx += 1
                    cur -= 1
                    
            c_set.add(c)
            cur += 1

            mx = max(mx, cur)
        
        return mx
