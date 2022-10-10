class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for i, j in redEdges:
            graph[i].add((j, True))
        for i, j in blueEdges:
            graph[i].add((j, False))
        ans = [-1]*n
        level = 0
        queue = deque([(0, True),(0, False)])
        visited = {(0, True),(0, False)}
        while queue:
            # print(queue, level)
            for _ in range(len(queue)):
                node, red = queue.popleft()
                if ans[node] == -1:
                    ans[node] = level
                for neigh, color in graph[node]:
                    if color != red and (neigh, color) not in visited:
                        visited.add((neigh, color))
                        queue.append((neigh, color))
            level += 1
        
        return ans
        