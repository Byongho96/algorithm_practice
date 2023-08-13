from collections import defaultdict

class Solution:
    def stringInfo(self, word: str) -> string:
        # Count each character
        dic = defaultdict(int)
        for c in word:
            dic[c] += 1

        # Extract only the number info from the dict'
        nums = list(dic.values())
        nums.sort()
        return nums


    def closeStrings(self, word1: str, word2: str) -> bool:
        # Filter the invalid data
        if set(word1) != set(word2):
            return False
        
        w1 = self.stringInfo(word1)
        w2 = self.stringInfo(word2)
        return w1 == w2
