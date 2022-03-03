import random


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        return self.dfs(root, root)
        
        
    def dfs(self, left_subtree, right_subtree):
        if not left_subtree and not right_subtree:
            return True
        if (not left_subtree and right_subtree) or (left_subtree and not right_subtree):
            return False
        
        if left_subtree.val != right_subtree.val:
            return False
        return self.dfs(left_subtree.left, right_subtree.right) and \
                        self.dfs(left_subtree.right, right_subtree.left)
        
        