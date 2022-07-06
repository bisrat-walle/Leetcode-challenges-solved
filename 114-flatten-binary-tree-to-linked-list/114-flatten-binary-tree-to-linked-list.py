# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        traversal = []
        def dfs(root):
            if not root:
                return
            traversal.append(root)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        
        dfs(root)
        # print(traversal)
        for index in range(len(traversal)-1):
            traversal[index].right = traversal[index+1]
            traversal[index].left = None
                