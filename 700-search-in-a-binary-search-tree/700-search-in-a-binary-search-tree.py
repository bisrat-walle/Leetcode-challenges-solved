# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.search(root, val)
        
    def search(self, root, val):
        if root == None:
            return
        if val == root.val:
            return root
        if val > root.val:
            return self.search(root.right, val)
        return self.search(root.left, val)
        