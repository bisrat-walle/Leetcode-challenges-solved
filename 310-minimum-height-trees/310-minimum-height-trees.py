from collections import deque, defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 3: return range(n)
        
        inDegrees = [0 for _ in range(n)]
        graph = defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
            inDegrees[i] += 1
            inDegrees[j] += 1
        
        queue = deque()
        for i in range(n):
            if inDegrees[i] == 1:
                queue.append(i)
        
        currentNodeCount = n
        
        while currentNodeCount > 2:
            currentNodeCount -= len(queue)
            for _ in range(len(queue)):
                current = queue.popleft()
                for neigh in graph[current]:
                    inDegrees[neigh] -= 1
                    if inDegrees[neigh] == 1:
                        queue.append(neigh)
                        
        return queue