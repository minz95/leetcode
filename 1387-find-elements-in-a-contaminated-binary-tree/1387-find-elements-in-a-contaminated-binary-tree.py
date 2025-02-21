# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        def make(node):
            if not node:
                return node
            if node.left:
                node.left.val = node.val * 2 + 1
                node.left = make(node.left)
            if node.right:
                node.right.val = node.val * 2 + 2
                node.right = make(node.right)
            return node
        if root:
            root.val = 0
        self.root = make(root)
        

    def find(self, target: int) -> bool:
        def help(target, node):
            if not node:
                return False
            if target == node.val:
                return True
            return help(target, node.left) or help(target, node.right)
        return help(target, self.root)
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)