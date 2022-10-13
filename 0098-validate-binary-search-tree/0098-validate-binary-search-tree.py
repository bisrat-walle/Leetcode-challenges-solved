# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        def dfs(root):
            if (not root.left) and (not root.right):
                return (root.val, root.val)
            if not root.left:
                left, right = dfs(root.right)
                if root.val >= left:
                    self.ans = False
                return (root.val, max(right, root.val))
            if not root.right:
                left, right = dfs(root.left)
                if root.val <= right:
                    self.ans = False
                return (min(left, root.val), root.val)
            left1, right1 = dfs(root.right)
            left2, right2 = dfs(root.left)
            if root.val >= right1 or root.val >= left1 or \
                    root.val <= right2 or root.val <= left2:
                self.ans = False
            return (min(right2, left2, root.val), max(right1, left1, root.val))
        
        dfs(root)
        return self.ans
            