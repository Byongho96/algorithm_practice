from typing import List
from collections import defaultdict

class Solution:
    adjacencyList = defaultdict(list)

    def dfs(self, source, target):
        if source not in self.adjacencyList or target not in self.adjacencyList:
            return -1

        stack = [(source, 1)]
        visited = set()
        visited.add(source) # visited.set(source) 

        while stack:
            cur, answer = stack.pop()

            if cur == target:
                return answer

            for adj, weight in self.adjacencyList[cur]:
                if adj in visited:
                    continue
                
                stack.append((adj, answer * weight))
                visited.add(adj)
        
        return -1


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.adjacencyList.clear()

        for (u, v), val in zip(equations, values):
            self.adjacencyList[u].append((v, val))
            self.adjacencyList[v].append((u, 1 / val))

        return [self.dfs(a, b) for a, b in queries] 