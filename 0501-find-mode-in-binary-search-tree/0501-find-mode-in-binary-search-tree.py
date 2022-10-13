# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)
        def dfs(root):
            if  not root:
                return
            counter[root.val] += 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        mx_freq = max(counter.values())
        ans = []
        for i, j in counter.items():
            if j == mx_freq:
                ans.append(i)
        return ans