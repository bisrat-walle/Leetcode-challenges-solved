# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.arr1 = []
        self.arr2 = []
        
        def compare(p, q):
            if not p and not q:
                return True
            if (not p and q) or (p and not q) or (p.val != q.val):
                return False
            
            return compare(p.left,q.left) and compare(p.right, q.right)
        return compare(p, q)
    