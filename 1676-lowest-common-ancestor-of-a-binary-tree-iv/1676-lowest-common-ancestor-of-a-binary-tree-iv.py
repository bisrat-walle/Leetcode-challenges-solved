# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(map(lambda k:k.val, nodes))
        self.ans = None
        
        def dfs(node):
            if not node:
                return 0
            
            res = 1 if node.val in nodes else 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            res += left + right
            
            if res == len(nodes) and self.ans == None:
                self.ans = node
            
            return res
            
        
        dfs(root)
        
        return self.ans
                