# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans  = None
        def dfs(root):
            if not root:
                return 0
            count = 0
            if root in [p,q]:
                count = 1
            count += dfs(root.left) + dfs(root.right)
            
            if not self.ans and count == 2:
                self.ans = root
            return count
        dfs(root)
        return self.ans
            