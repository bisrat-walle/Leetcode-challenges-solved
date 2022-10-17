# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans = 0
        
        def dfs(root):
            left, right = 0, 0
            if root.left:
                res = dfs(root.left)
                if root.left.val == root.val:
                    left = res
            
            if root.right:
                res = dfs(root.right)
                if root.right.val == root.val:
                    right = res
            self.ans = max(self.ans, right+left+1)
            return 1+max(right, left)
        
        dfs(root)
        return self.ans-1