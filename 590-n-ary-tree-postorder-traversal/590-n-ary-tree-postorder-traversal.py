"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.postorder = []
        self.traverse(root)
        return self.postorder
    
    def traverse(self, root):
        if not root:
            return
        for i in root.children:
            self.traverse(i)
        self.postorder.append(root.val)