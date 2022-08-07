# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root, current_num=""):
            if not root:
                return
            nonlocal ans
            if (not root.left) and not root.right:
                ans += int(current_num+str(root.val))
                return
            dfs(root.left, current_num+str(root.val))
            dfs(root.right, current_num+str(root.val))
        dfs(root)
        return ans