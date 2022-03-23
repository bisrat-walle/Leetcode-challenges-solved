# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def insert(self, val: int) -> int:
        if not self.root:
            self.root = TreeNode(val)
            return
        queue = [self.root]
        while queue:
            temp = []
            for i in queue:
                if not i.left:
                    i.left = TreeNode(val)
                    return i.val
                temp.append(i.left)
                if not i.right:
                    i.right = TreeNode(val)
                    return i.val
                temp.append(i.right)
            queue = temp
            
    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()