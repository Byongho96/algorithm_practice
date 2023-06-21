from typing import List

class Solution:
    digit_to_letter = {
        '2': ('a', 'b', 'c'),
        '3': ('d', 'e', 'f'),
        '4': ('g', 'h', 'i'),
        '5': ('j', 'k', 'l'),
        '6': ('m', 'n', 'o'),
        '7': ('p', 'q', 'r', 's'),
        '8': ('t', 'u', 'v'),
        '9': ('x', 'y', 'z', 'w'),
    }

    def __init__(self):
        self.answer = []

    def backtracking(self, idx, digits: str) -> None:
        # 종료 조건
        if idx == len(digits):
            self.answer.append(digits)
            return
        
        # 후보군 출력
        for c in Solution.digit_to_letter[digits[idx]]:
            self.backtracking(idx+1, digits[:idx] + c + digits[idx+1:])

    def letterCombinations(self, digits: str) -> List[str]:
        # 초기화
        self.answer = []

        # 백트래킹
        if digits:
            self.backtracking(0, digits)

        return self.answer
    
solution = Solution()
print(solution.letterCombinations('23'))






















        # 1. DFS
        # 32ms
        # ref = {'2': ('a', 'b', 'c',), '3': ('d', 'e', 'f',), '4': ('g', 'h', 'i',), '5': ('j', 'k', 'l',),
        #        '6': ('m', 'n', 'o',), '7': ('p', 'q', 'r', 's',), '8': ('t', 'u', 'v',), '9': ('w', 'x', 'y', 'z',)}
        # def dfs(string, idx):
        #     if idx == len(digits):
        #         if string:
        #             ans.append(string)
        #         return
        #     for c in ref[digits[idx]]:
        #         dfs(string + c, idx + 1)
        #
        # ans = []
        # dfs('', 0)
        # return ans

        # 2. BFS
        # 28ms
        # ref = {'2': ('a', 'b', 'c',), '3': ('d', 'e', 'f',), '4': ('g', 'h', 'i',), '5': ('j', 'k', 'l',),
        #        '6': ('m', 'n', 'o',), '7': ('p', 'q', 'r', 's',), '8': ('t', 'u', 'v',), '9': ('w', 'x', 'y', 'z',)}
        # def bfs():
        #     q = deque()
        #     q.append(('', 0))

        #     while q:
        #         string, idx = q.popleft()
        #         if idx == len(digits):
        #             if string:
        #                 ans.append(string)
        #             continue
        #         for c in ref[digits[idx]]:
        #             q.append((string + c, idx + 1))

        # ans = []
        # bfs()
        # return ans
