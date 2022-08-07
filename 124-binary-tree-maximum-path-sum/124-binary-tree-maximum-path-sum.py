# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")
        @lru_cache(None)
        def dfs(root):
            if not root:
                return 0
            nonlocal ans
            option1 = dfs(root.left)
            option2 = dfs(root.right)
            ans = max(ans, option1+option2+root.val)
            return max(option1+root.val, option2+root.val, 0)
            
        dfs(root)
        return ans