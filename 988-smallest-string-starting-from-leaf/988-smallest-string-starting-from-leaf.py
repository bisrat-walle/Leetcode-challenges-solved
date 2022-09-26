# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root: return
        ans = []
        cache = {}
        def dfs(root, prev=()):
            if (root, prev) in cache:
                return
            if not root:
                return
            newPath = prev+(chr(97+root.val), )
            
            if (not root.left) and (not root.right):
                ans.append("".join(reversed(newPath)))
            
            dfs(root.left, newPath, )
            dfs(root.right, newPath)
            cache[(root, prev)] = True
        dfs(root)
        ans.sort()
        return ans[0]