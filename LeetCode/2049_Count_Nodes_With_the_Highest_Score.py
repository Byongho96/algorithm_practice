from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        N = len(parents)

        # Make children array
        children = [[] for _ in range(N)]
        for idx, parent in enumerate(parents):
            if idx:
                children[parent].append(idx)

        # score = (N - sub_size[current]) * sub_size[child] * sub_size[child]
        scores = [1] * N

        def backtracking(cur: int):
            cur_size = 1

            for child in children[cur]:
                sub_size = backtracking(child)
                cur_size += sub_size
                scores[cur] *= sub_size

            scores[cur] *= (N - cur_size) or 1
            return cur_size

        backtracking(0)
        print(scores)

        return scores.count(max(scores))
