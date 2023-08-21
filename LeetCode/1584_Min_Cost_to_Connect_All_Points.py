import heapq

class Solution:
    def mst_prim(self, N, points, start):
        # make necessary variables
        INF= 2 * 2 * 1000000
        weight = [INF] * N
        visited = [False] * N
        heap = []

        # set the start point
        weight[start] = 0
        heapq.heappush(heap, (0, 0))
    
        # prim algorithm
        while heap:
            w, cur = heapq.heappop(heap)

            # pass the invalid data
            if weight[cur] < w:
                continue

            # connect to mst
            visited[cur] = True

            # travserse the adjacent nodes
            ci, cj = points[cur]
            for adj in range(N):
                # pass the already connected points
                if visited[adj]:
                    continue
                ai, aj  = points[adj]
                w = abs(ai - ci) + abs(aj - cj)
                if w < weight[adj]:
                    weight[adj] = w
                    heapq.heappush(heap, (w, adj))

        # return the sum of weight
        return sum(weight)


    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # run the prim algorithm
        N = len(points)
        answer = self.mst_prim(N, points, 0)
        return answer