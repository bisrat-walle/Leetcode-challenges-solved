class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        path = [0]
        visited = {0}
        ans = []
        def dfs(node):
            # print(node)
            if node == n-1:
                ans.append(path.copy())
                return
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    path.append(neighbor)
                    dfs(neighbor)
                    visited.discard(neighbor)
                    path.pop()
        dfs(0)
        print(ans)
        return ans