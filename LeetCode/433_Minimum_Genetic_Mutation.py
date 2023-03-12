from typing import List
from collections import deque

# 20ms
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # 2-2. BFS with Boolean ref
        ref = {'A': ('C', 'G', 'T',), 'C': ('A', 'G', 'T',), 'G': ('A', 'C', 'T',), 'T': ('A', 'C', 'G',)}
        def bfs(start):
            visited = {gene: True for gene in bank}

            q = deque()
            q.append((start, 0))

            while q:
                string, cnt = q.popleft()
                if string == end:
                    return cnt
                for idx in range(8):
                    for c in ref[string[idx]]:
                        middle = string[:idx] + c + string[idx+1:]
                        if visited.get(middle):
                            visited[middle] = False
                            q.append((middle, cnt+1))
            return 9

        mn = bfs(start)
        if mn == 9:
            return -1
        else:
            return mn
# # 62ms
# class Solution:
#     def minMutation(self, start: str, end: str, bank: List[str]) -> int:
#         # 2-1. BFS with num ref
#         ref = {'A': ('C', 'G', 'T',), 'C': ('A', 'G', 'T',), 'G': ('A', 'C', 'T',), 'T': ('A', 'C', 'G',)}
#         def bfs(start):
#             visited = {gene: 0 for gene in bank}
#             visited[start] = 1
#
#             q = deque()
#             q.append(start)
#
#             while q:
#                 string = q.popleft()
#                 if string == end:
#                     return visited[string] - 1
#                 for idx in range(8):
#                     for c in ref[string[idx]]:
#                         middle = string[:idx] + c + string[idx+1:]
#                         if visited.get(middle) == 0:
#                             visited[middle] = visited[string] + 1
#                             q.append(middle)
#             return 9
#
#         mn = bfs(start)
#         if mn == 9:
#             return -1
#         else:
#             return mn

# # 33ms
# class Solution:
#     def minMutation(self, start: str, end: str, bank: List[str]) -> int:
#         # 1. backtracking
#         ref = {'A': ('C', 'G', 'T',), 'C': ('A', 'G', 'T',), 'G': ('A', 'C', 'T',), 'T': ('A', 'C', 'G',)}
#         def backtracking(string, cnt):
#             nonlocal mn
#             # 종료조건
#             if string == end:
#                 mn = min(mn, cnt)
#                 return
#             # 가지치기
#             if cnt >= mn:
#                 return
#             if mn == MIN:
#                 return
#             # 재귀호출
#             for idx in nodes:
#                 for c in ref[string[idx]]:
#                     middle = string[:idx] + c + string[idx+1:]
#                     if bank.get(middle):
#                         bank[middle] = False            # It should be changed before the recursive
#                         backtracking(middle, cnt + 1)
#
#         # 속도를 높이기 위한 작업. 없으면 59ms
#         different = []
#         same = []
#         MIN = 0
#         for i in range(8):
#             if start[i] != end[i]:
#                 MIN += 1
#                 different.append(i)
#                 continue
#             same.append(i)
#         nodes = different + same
#
#         bank = {gene: True for gene in bank}
#         mn = 9
#         backtracking(start, 0)
#
#         # 프린트
#         if mn == 9:
#             return -1
#         else:
#             return mn

s = Solution()
print(s.minMutation(start = "AACCGGTT", end = "AACCGCTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]))