# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        leaves = set()
        @lru_cache(None)
        def dfs(root, current=(), sm=0, prev=None):
            if not root:
                if sm == targetSum and prev in leaves:
                    ans.append(current)
                return
            if root.left == None and root.right == None:
                leaves.add(root)
            dfs(root.left, current+(root.val,), sm+root.val, root)
            dfs(root.right, current+(root.val,), sm+root.val, root)
        
        
        dfs(root)
        
        return ans
            