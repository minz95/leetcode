# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def path(node):
            if not node:
                return 0
            nonlocal diameter

            left = path(node.left)
            right = path(node.right)
            diameter = max(diameter, left + right)

            return max(left, right) + 1
        path(root)
        return diameter