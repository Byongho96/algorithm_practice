from collections import deque

class Solution:

    def decodeStack(self):
				# 문자 단위 추출
        unit_s = deque()
        while True:
            char = self.stack.pop()
            if char == '[':
                break
            unit_s.appendleft(char)
        unit_s = ''.join(unit_s)

				# 반복할 횟수 추출
        num = deque()
        while True:
            if not self.stack:
                break
            if not self.stack[-1].isnumeric():
                break
            n = self.stack.pop()
            num.appendleft(n)
        num = int(''.join(num))

        self.stack.append(num * unit_s)


    def decodeString(self, s: str) -> str:
        self.stack = []
				
				# 스택 연산
        for char in s:
            if char != ']':
                self.stack.append(char)
            else:
                self.decodeStack()

        answer = ''.join(self.stack)
        return answer