from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        an = []
        def bfs(root):
            if not root:
                return
            queue = deque([root])
            while queue:
                an.append(queue[-1].val)
                for _ in range(len(queue)):
                    current= queue.popleft()
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
        bfs(root)
        return an