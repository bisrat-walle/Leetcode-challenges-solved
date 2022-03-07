# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder = []
        self.traverse(root)
        return self.inorder
    def traverse(self, root):
        if not root:
            return
        if root.left:
            self.traverse(root.left)
        self.inorder.append(root.val)
        if root.right:
            self.traverse(root.right)