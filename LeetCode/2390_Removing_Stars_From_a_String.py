class Solution:
    def removeStars(self, s: str) -> str:
        cnt = 0
        answer = []

        for c in s[::-1]:
            if c == '*':
                cnt += 1
                continue
            if cnt:
                cnt -= 1
                continue
            answer.append(c)
        
        return ''.join(answer[::-1])