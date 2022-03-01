# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        isEven = lambda a: a%2 == 0
        
        def dfs(node, parent=None, grand=None):
            
            if not node:
                return
            
            if grand and isEven(grand.val):
                self.total += node.val

            if node.left or node.right:
                return dfs(node.left, node, parent) or dfs(node.right, node, parent)
            
        dfs(root)    
        
        return self.total