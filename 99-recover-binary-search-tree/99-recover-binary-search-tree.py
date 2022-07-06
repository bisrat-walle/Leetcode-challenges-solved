# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder_traversal = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            inorder_traversal.append(root)
            inorder(root.right)
            
        
        inorder(root)
        index = 0
        for num in sorted(map(lambda a:a.val, inorder_traversal)):
            inorder_traversal[index].val = num
            index += 1
        