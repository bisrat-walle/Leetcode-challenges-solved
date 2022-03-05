# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        queue = [root]
        an = []
        counter = 0
        while queue:
            if counter%2 == 0:
                an.append([i.val for i in queue])
            else:
                an.append(list(reversed([i.val for i in queue])))
            temp = []
            for i in queue:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            queue = temp
            counter += 1
        return an
        