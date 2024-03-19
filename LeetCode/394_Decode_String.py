class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c.isdigit():
                if stack and stack[-1].isdigit():
                    stack[-1] += c
                else: 
                    stack.append(c)
                continue

            if c == '[':
                stack.append(c)
                continue

            if c == ']':
                c = stack.pop()
                stack.pop() # pop out '['
                c *= int(stack.pop())

            if stack and not stack[-1].isdigit() and stack[-1] != '[':
                stack[-1] += c
            else:
                stack.append(c)

        return stack[0]
        