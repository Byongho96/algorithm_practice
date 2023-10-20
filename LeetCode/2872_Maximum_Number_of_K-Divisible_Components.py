from collections import deque, defaultdict


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # filter edge case
        if n == 1:
            return 0 if values[0] % k else 1

        # make adjacent node list
        adjLst = [[] for _ in range(n)]
        adjNum = defaultdict(int)
        for i, j in edges:
            adjLst[i].append(j)
            adjLst[j].append(i)
            adjNum[i] += 1
            adjNum[j] += 1

        # find the leaf dnoes
        queue = deque()
        for i in range(n):
            if len(adjLst[i]) == 1:
                queue.append(i)

        # set the required data
        count = 0
        sm_values = [0] * n
        visited = [False] * n

        # traverse from the leaf
        while queue:
            cur = queue.popleft()

            # filter invalid
            if visited[cur]:
                continue

            # visit the current node
            visited[cur] = True
            sm_values[cur] += values[cur]

            # if the sub-tree is divided by k
            if not sm_values[cur] % k:
                count += 1

            # find parent node
            for par in adjLst[cur]:
                if visited[par]:
                    continue
                # if the sub-tree is not divided by k
                if sm_values[cur] % k:
                    sm_values[par] += sm_values[cur]
                # cut the edge
                adjNum[par] -= 1
                # add queue if the parent node is a leaf node
                if adjNum[par] == 1:
                    queue.append(par)
                break

        return count
