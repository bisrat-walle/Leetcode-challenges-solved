# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.root_index = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        inorder_index_map = dict(zip(inorder, range(len(inorder))))
        
        def construct_tree(left=0, right=len(preorder)-1):
            
            if left > right: 
                return
            
            root_value = preorder[self.root_index]
            root = TreeNode(root_value)
            
            self.root_index += 1
            root.left = construct_tree(left, inorder_index_map[root_value] - 1)
            root.right = construct_tree(inorder_index_map[root_value] + 1, right)

            return root


        return construct_tree()