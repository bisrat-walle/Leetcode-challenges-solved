"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
    

    

class Solution:
    
    def __init__(self):
        self.height = 0
    
    
    def maxDepth(self, root: 'Node') -> int:
        
        
        
        def find_max_depth(root, h=1):
            if not root:
                return
            
            self.height = max(h, self.height)

            
            for i in root.children:
                find_max_depth(i, h+1)
        
        find_max_depth(root)
                
        
        return self.height