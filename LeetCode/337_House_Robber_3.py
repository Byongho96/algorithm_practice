class Solution:
    def divide_conquer(self, cur):
        left, right = [0, 0], [0, 0]

        # traverse the child nodes
        if cur.left:
            left = self.divide_conquer(cur.left)
        if cur.right:
            right = self.divide_conquer(cur.right)

        # return the for the two cases
        withRoot = cur.val + left[1] + right[1]
        withoutRoot = max(left) + max(right)
        return [withRoot, withoutRoot]

    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.divide_conquer(root)) if root else 0
