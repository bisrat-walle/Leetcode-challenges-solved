# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        traversal = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            traversal.append(root.val)
            inorder(root.right)
        inorder(root)
        traversal.sort()
        smallest = traversal[0]
        
        # print(traversal)
        for index in range(1, len(traversal)):
            if traversal[index] != smallest:
                return traversal[index]
        return -1
        