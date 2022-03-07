# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.level = []
        self.levelOrder(root)
        self.level.reverse()
        return self.level
    
    def levelOrder(self, root):
        if not root:
            return
        queue = [root]
        while queue:
            self.level.append([i.val for i in queue])
            temp = []
            for i in queue:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            queue = temp