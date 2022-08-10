# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if not n: return None
        root_index = n // 2
        root = TreeNode(
            val = nums[root_index], 
            left = self.sortedArrayToBST(nums[:root_index]), \
            right = self.sortedArrayToBST(nums[root_index + 1 :])
        )
        return root