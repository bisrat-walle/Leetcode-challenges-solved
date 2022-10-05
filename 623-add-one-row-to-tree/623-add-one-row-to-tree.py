# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        queue = deque([root])
        current_depth = 1
        while queue:
            # print(list(map(lambda k: k.val, queue)), dept)
            if current_depth == depth-1:
                for _ in range(len(queue)):
                    current = queue.popleft()
                    right = current.right
                    left = current.left
                    new_left = TreeNode(val)
                    new_right = TreeNode(val)
                    new_left.left = left
                    new_right.right = right
                    current.left = new_left
                    current.right = new_right
                    
                break
            for _ in range(len(queue)):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            current_depth += 1
        return root