# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return
        ans = []
        cache = {}
        def dfs(root, prev=()):
            if (root, prev) in cache:
                return
            if not root:
                return
            newPath = prev+(str(root.val), )
            
            if (not root.left) and (not root.right):
                ans.append("->".join(newPath))
            
            dfs(root.left, newPath, )
            dfs(root.right, newPath)
            cache[(root, prev)] = True
        
        dfs(root)
        return ans