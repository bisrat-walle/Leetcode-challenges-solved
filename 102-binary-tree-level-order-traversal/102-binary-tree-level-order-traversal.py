# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelOrderTraversal = []
        if not root:
            return levelOrderTraversal
        
        queue = [root]
        
        while queue:
            levelOrderTraversal.append([i.val for i in queue])
            temp = []
            for i in queue:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            queue = temp
        
        return levelOrderTraversal