class Solution:
    def longestValidParentheses(self, s: str) -> int:
        mx = 0
        stack = []
        
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                cnt = 0
                while stack:
                    pop = stack.pop()
                    if isinstance(pop, int):
                        cnt += pop
                    else:
                        cnt += 2
                        if stack and isinstance(stack[-1], int):
                            cnt += stack.pop()
                        stack.append(cnt)
                        mx = max(mx, cnt)
                        break
        
        return mx