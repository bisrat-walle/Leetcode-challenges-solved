# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        def dfs(root):
            if not root:
                return 0
            left_height = 1 + dfs(root.left)
            right_height = 1 + dfs(root.right)
            
            if max(left_height, right_height) > min(left_height, right_height)+1:
                self.ans = False
            
            return max(left_height, right_height)
        
        dfs(root)
        
        return self.ans