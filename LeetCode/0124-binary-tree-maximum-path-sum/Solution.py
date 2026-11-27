# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        ans = float('-inf')
        def solve(node):
            nonlocal ans
            if node is None: return 0
            ls = solve(node.left)
            rs = solve(node.right)
            if ls < 0:
                ls = 0
            if rs < 0:
                rs = 0
            cs = node.val + ls + rs
            if cs > ans:
                ans = cs
            return node.val + max(ls, rs)
        solve(root)
        return ans