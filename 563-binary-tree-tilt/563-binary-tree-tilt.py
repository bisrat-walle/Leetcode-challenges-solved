# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        return self.findSumTotal(root)
        
    def findSum(self, node):
        if not node:
            return 0
        return node.val + self.findSum(node.left) + self.findSum(node.right)
    
    def findSumTotal(self, node):
        if not node:
            return 0
        left_sum = self.findSum(node.left)
        right_sum = self.findSum(node.right)
        # print("For", node.val, "left", left_sum, "right", right_sum)
        tilt = int(math.fabs(left_sum - right_sum))
        return   tilt + self.findSumTotal(node.left) + self.findSumTotal(node.right)
