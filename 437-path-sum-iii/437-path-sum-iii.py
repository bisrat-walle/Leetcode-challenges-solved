# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefixSums = defaultdict(int)
        
        self.res = 0
        prefixSums[0] += 1
        
        def dfs(node, sm):
            if node is None:
                return
            sm += node.val
            self.res += prefixSums[sm - targetSum]
            prefixSums[sm] += 1
            
            dfs(node.left, sm)
            dfs(node.right, sm)
            
            prefixSums[sm] -= 1 # backtrack
            
        dfs(root, 0)
        return self.res