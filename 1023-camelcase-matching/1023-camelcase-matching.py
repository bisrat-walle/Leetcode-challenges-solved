class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1
    def insert(self,word, index):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c]= TrieNode()
            cur = cur.children[c]
        cur.index = index

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        root = TrieNode()
        for index, query in enumerate(queries):
            root.insert(query, index)
        n = len(queries)
        ans = [False] * n
        
        def dfs(node, index):
            
            for child in node.children:
            
                if index >= len(pattern):
                    if child.isupper():
                        continue
                    if node.children[child].index !=-1:
                        ans[node.children[child].index] = True
                    dfs(node.children[child], index)
                    continue     
                if pattern[index] == child:
                    if node.children[child].index !=-1:
                        ans[node.children[child].index] = True
                    dfs(node.children[child], index+1)
                elif child.isupper():
                    continue
                else:
                    dfs(node.children[child], index)
            
        dfs(root, 0)
        
        return ans