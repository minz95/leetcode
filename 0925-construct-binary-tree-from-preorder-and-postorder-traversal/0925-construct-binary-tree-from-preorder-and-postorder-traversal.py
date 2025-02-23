# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        root = TreeNode(preorder.pop(0))
        if not preorder:
            return root
        left_subtree_size = postorder.index(preorder[0]) + 1

        root.left = self.constructFromPrePost(preorder[:left_subtree_size], postorder[:left_subtree_size])
        root.right = self.constructFromPrePost(preorder[left_subtree_size:], postorder[left_subtree_size:])
        return root
        