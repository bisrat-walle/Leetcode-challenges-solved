class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(set)
        for node, parent in enumerate(parent):
            graph[parent].add(node)
        
        self.ans = 0
        
        def dfs(node):
            left, right = 0, 0
            for neighbor in graph[node]:
                res = dfs(neighbor)
                if s[node] != s[neighbor]:
                    if res > right:
                        left, right = right, res
                    elif res > left:
                        left = res
            self.ans = max(self.ans, right+left+1)
            return right+1
        
        dfs(0)
        return self.ans