from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = [False for i in range(len(graph))]
        graph = list(map(set, graph))
        reverse_graph = [set() for i in range(len(graph))]
        
        queue = deque()
        
        for index, adj in enumerate(graph):
            if not adj:
                queue.append(index)
            for neigh in adj:
                reverse_graph[neigh].add(index)
        
        while queue:
            current = queue.popleft()
            safe[current] = True
            for neigh in reverse_graph[current]:
                graph[neigh].discard(current)
                if not graph[neigh]:
                    queue.append(neigh)
        
        return [i for i in range(len(safe)) if safe[i]]
                