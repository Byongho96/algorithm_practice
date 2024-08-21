from typing import List

class Solution:
    operation = {
        '*': lambda a, b: a * b,
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b
    }
    memoization = {}

    def diffWaysToCompute(self, expression: str) -> List[int]:
        N = len(expression)

        if expression in self.memoization:
            return self.memoization[expression]

        if expression.isnumeric():
            return [int(expression)]

        results = []
        for i in range(1, N - 1):
            operator = expression[i]

            if operator not in self.operation:
                continue
                
            left_results = self.diffWaysToCompute(expression[:i])
            right_results = self.diffWaysToCompute(expression[i+1:])

            for left in left_results:
                for right in right_results:
                    results.append(self.operation[operator](left, right))
        
        self.memoization[expression] = results
        return results