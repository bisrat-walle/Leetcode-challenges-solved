# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        def dfs(root):
            if not root:
                ans.append("1001")
                return
            ans.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return " ".join(ans)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "1001" or data == "":
            return
        arr = list(map(int, data.split()))
        idx = 0
        ans = TreeNode()
        current = ans
        def dfs(current):
            nonlocal idx
            if not current or arr[idx] == 1001:
                return
            current.val = arr[idx]
            idx += 1
            current.left = dfs(TreeNode())
            idx += 1
            current.right = dfs(TreeNode())
            
            return current
        
        dfs(ans)
        return ans
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))