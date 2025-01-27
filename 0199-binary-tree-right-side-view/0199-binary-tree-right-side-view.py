# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        q = deque([(root, 0)])

        level = 0
        while q:
            while q and q[0][-1] == level:
                node = q.popleft()
                if node[0].left:
                    q.append((node[0].left, level+1))
                if node[0].right:
                    q.append((node[0].right, level+1))
            result.append(node[0].val)
            level += 1

        return result   
