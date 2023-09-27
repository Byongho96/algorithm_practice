class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_dict = Counter([tuple(row) for row in grid])

        answer = 0
        for col in zip(*grid):
            answer += row_dict[col]

        return answer
