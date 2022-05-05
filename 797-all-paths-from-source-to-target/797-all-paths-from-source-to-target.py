class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        an = []
        # visited = set()
        queue = deque([(0, [0])])
        
        while queue:
            current, path = queue.popleft()
            if current == len(graph)-1:
                an.append(path)
            # visited.add(current)
            for i in graph[current]:
                # if i not in visited:
                    queue.append((i, path+[i]))
                    # visited.add(i)
        
        return an