class Solution:
    def backtracking(self, n, s, value, visited):
        # end condition
        if n == self.N:
            if value == self.target:
                lst = []
                for i in range(1, 10):
                    if visited >> i & 1:
                        lst.append(i)
                self.answer.append(lst)
            return

        # pruning
        if (10 - s) < (self.N - n):
            return

        if value + ((s + self.N - n - 1 + s) * (self.N - n)) / 2 > self.target:
            return

        if value + ((9 + self.N - n - 1 + 9) * (self.N - n)) / 2 < self.target:
            return

        # traverse candidates
        for num in range(s, 10):
            self.backtracking(n + 1, num + 1, value + num, visited | 1 << num)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.N = k
        self.target = n

        self.answer = []
        self.backtracking(0, 1, 0, 0)

        return self.answer
