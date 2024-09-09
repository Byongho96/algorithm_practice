from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def possible_subtrees(self, s: int, e: int) -> List[TreeNode]:
        if s > e:
            return [None]

        trees = []
        for cur in range(s, e + 1):
            left_subtrees = self.possible_subtrees(s, cur - 1)
            right_subtrees = self.possible_subtrees(cur + 1, e)

            for l in left_subtrees:
                for r in right_subtrees:
                    root = TreeNode(cur) 
                    root.left = l
                    root.right = r
                    trees.append(root)

        return trees
                    

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        nodes = [i for i in range(1, n + 1)]

        answer = self.possible_subtrees(1, n)
        return answer
        