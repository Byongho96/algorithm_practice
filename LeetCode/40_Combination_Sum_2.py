class Solution:
    answer = None
    candidates = None
    maxRemain = None 

    def init(self, N:int, candidates: List[int], target: int) -> None:
        self.answer = []

        candidates.sort()
        self.candidates = candidates

        self.maxRemain = [0] * N
        self.maxRemain[-1] = candidates[-1]
        for i in range(N - 2, -1, -1):
            self.maxRemain[i] = self.maxRemain[i + 1] + candidates[i]  

    def backtracking(self, N, idx, target, sm, path):
        if sm == target:
            self.answer.append(path)
            return
        if sm > target:
            return
        if idx > N - 1 or sm + self.maxRemain[idx] < target:
            return

        for nxt in range(idx, N):
            if nxt > idx and self.candidates[nxt] == self.candidates[nxt-1]:
                continue
            self.backtracking(N, nxt+1, target, sm+self.candidates[nxt], path+[self.candidates[nxt]])
        return

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        self.init(N, candidates, target)
        self.backtracking(N, 0, target, 0, [])

        return self.answer