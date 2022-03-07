# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        height = 1
        queue = [root]
        while queue:
            has_no_children = False
            temp = []
            for i in queue:
                
                if not i.left and not i.right:
                    has_no_children = True
                    break
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)   
            if has_no_children:
                break
            height += 1
            queue = temp
        return height