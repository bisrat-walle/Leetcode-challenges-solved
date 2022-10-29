# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def rec(root):
            if not root:
                return 0
            left = rec(root.left)
            right = rec(root.right)
            # print(self.ans, left, right, root.val)
            self.ans = max(self.ans, 1+left+right)
            return 1+max(left, right)
        
        rec(root)
        
        return self.ans-1