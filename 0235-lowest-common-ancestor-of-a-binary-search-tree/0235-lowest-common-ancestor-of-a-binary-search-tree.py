# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = deque([root])
        mn = min(p.val, q.val)
        mx = max(p.val, q.val)
        
        ans = None
        
        while queue:
            current = queue.popleft()
            if mn <= current.val <= mx and not ans:
                ans = current

            if current.left and current.val > mn:
                queue.append(current.left)
            if current.right and current.val < mx:
                queue.append(current.right)

        return ans 
            