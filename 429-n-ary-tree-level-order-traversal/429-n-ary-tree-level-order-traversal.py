"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        level = []
        queue = [root]
        while queue:
            level.append([i.val for i in queue])
            temp = []
            for i in queue:
                for j in i.children:
                    temp.append(j)
            queue = temp
        return level