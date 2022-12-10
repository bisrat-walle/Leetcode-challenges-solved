# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        graph = defaultdict(list)
        queue = deque([root])
        leaves = set()
        
        while queue:
            current = queue.popleft()
            if (not current.left) and (not current.right):
                leaves.add(current.val)
            if current.left:
                graph[current.val].append(current.left.val)
                graph[current.left.val].append(current.val)
                queue.append(current.left)
            if current.right:
                graph[current.val].append(current.right.val)
                graph[current.right.val].append(current.val)
                queue.append(current.right)
        
        
        queue = deque([k])
        visited = {k}
        
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current in leaves:
                    return current
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        
        return -1 # Impossible
                
            