# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def preprocess(root):
            parent = {}
            depth = {}
            def dfs(node, par, d):
                if not node:
                    return
                parent[node] = par
                depth[node] = d
                dfs(node.left, node, d + 1)
                dfs(node.right, node, d + 1)
            dfs(root, None, 0)

            up = {node: [None] * 20 for node in parent}
            for node in parent:
                up[node][0] = parent[node]

            for j in range(1, 20):
                for node in parent:
                    if up[node][j-1]:
                        up[node][j] = up[up[node][j-1]][j-1]
            return up, depth

        up, depth = preprocess(root)
        if depth[p] < depth[q]:
            p, q = q, p
        diff = depth[p] - depth[q]
        for j in range(20):
            if diff & (1 << j):
                p = up[p][j]
        if p == q:
            return p
        for j in range(19, -1, -1):
            if up[p][j] != up[q][j]:
                p = up[p][j]
                q = up[q][j]
        return up[p][0]