# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        level = 0
        while queue:
            n = len(queue)
            even_level = level%2 == 0
            
            if even_level:
                if queue[0].val%2 == 0:
                    return False
            elif queue[0].val%2 != 0:
                return False
            
            for i in range(1, n):
                if even_level:
                    if queue[i].val%2 == 0 or queue[i].val <= queue[i-1].val:
                        return False
                elif queue[i].val%2 != 0 or queue[i].val >= queue[i-1].val:
                        return False
            
            for i in range(n):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            level += 1
        return True