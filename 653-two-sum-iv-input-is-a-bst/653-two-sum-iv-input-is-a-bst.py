# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        values = set()
        def dfs(root):
            if not root:
                return False
            if k-root.val in values:
                return True
            values.add(root.val)
            return dfs(root.left) or dfs(root.right)
        return dfs(root)
            