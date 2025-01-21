# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hashTree(self, tree: Optional[TreeNode]) -> str:
        if not tree:
            return "X"
        return f"#{tree.val} {self.hashTree(tree.left)} {self.hashTree(tree.right)}"
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rootHash = self.hashTree(root)
        subHash = self.hashTree(subRoot)
    
        return subHash in rootHash        
                
        
        
        
