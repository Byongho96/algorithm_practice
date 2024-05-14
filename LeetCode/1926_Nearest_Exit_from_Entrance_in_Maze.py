from typing import List
from collections import deque

class Solution:
    DIRECTION = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        N = len(maze)
        M = len(maze[0])

				# Set the start
        [si, sj]  = entrance    
        visited = [[False] * M for _ in range(N)]
        visited[si][sj] = True

				# Set the adjacent nodes from the start
        queue = deque()
        for di, dj in self.DIRECTION:
            ni = si + di
            nj = sj + dj
            if ni < 0 or ni > N - 1 or nj < 0 or nj > M - 1:
                continue
            if maze[ni][nj] == '+':
                continue
            queue.append((ni, nj, 1))
            visited[ni][nj] = True

				# BFS
        while queue:
            i, j, dis = queue.popleft()

						# Find answer
            if i == 0 or i == N - 1 or j == 0 or j == M - 1:
                return dis

            for di, dj in self.DIRECTION:
                ni = i + di
                nj = j + dj
                if maze[ni][nj] == '+' or visited[ni][nj]:
                    continue
                visited[ni][nj] = True
                queue.append((ni, nj, dis + 1))

        return -1