# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        label = defaultdict(list)
        
        def rec(root, row=0, col=0):
            label[(row, col)].append(root.val)
            if root.left:
                rec(root.left, row+1, col-1)
            if root.right:
                rec(root.right, row+1, col+1)
        
        rec(root)
        
        ans = []
        sorted_items = sorted(label.items(), key=lambda k:(k[0][1], k[0][0]))
        prev = None
        for key, value in sorted_items:
            # print(key, value)
            if prev == None or prev != key[1]:
                ans.append(sorted(value))
                prev = key[1]
            else:
                ans[-1].extend(sorted(value))
        
        return ans