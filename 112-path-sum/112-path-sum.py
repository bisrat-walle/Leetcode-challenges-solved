# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        return self.dfs(root, targetSum)
    
    def dfs(self, node, targetSum, tot=0):
        if not node:
            return False
        
        if not node.left and not node.right:
            return tot+node.val == targetSum
        
        return self.dfs(node.left, targetSum, tot+node.val) or \
                self.dfs(node.right, targetSum, tot+node.val)