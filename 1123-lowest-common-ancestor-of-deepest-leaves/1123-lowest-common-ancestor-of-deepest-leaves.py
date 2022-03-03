# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.max_depth = 0
        self.lca = None
        
        self.dfs(root)
        
        return self.lca
        
    def dfs(self, node, height=0):
        if not node:
            return height

        left_depth = self.dfs(node.left, height + 1)
        right_depth = self.dfs(node.right, height + 1)

        self.max_depth = max(self.max_depth, max(left_depth, right_depth))

        if left_depth == right_depth == self.max_depth:
            self.lca = node

        return max(left_depth, right_depth)
        
        
