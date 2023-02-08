class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)

        for (left, right), value in zip(equations, values):
            graph[left][right] = value
            graph[right][left] = 1/value

        ans = []
        for left, right in queries:
            visited = set()
            queue = collections.deque([(left, 1)])
            res = -1
            while queue:
                node, cost = queue.popleft()
                visited.add(node)
                if right in graph[node]:
                    res = cost * graph[node][right]
                    break
                
                for neighbor, new_cost in graph[node].items():
                    if neighbor not in visited:
                        queue.append((neighbor, cost * new_cost))
            ans.append(res)

        return ans