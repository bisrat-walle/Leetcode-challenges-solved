# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = [None]
        
        def dfs(node):
            if not node:
                return 0
            res = dfs(node.left) + dfs(node.right)
            if node in (p, q):
                res += 1
                
            if res == 2 and not ans[0]:
                ans[0] = node
            
            return res
        
        dfs(root)
            
            
        
        return ans[0]