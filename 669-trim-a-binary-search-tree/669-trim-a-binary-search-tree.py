# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def rec(root):
            if not root:
                return
            if low > root.val:
                return rec(root.right)
            if high < root.val:
                return rec(root.left)
            root.left = rec(root.left)
            root.right = rec(root.right)
            return root
        return rec(root)
        
        
                
        