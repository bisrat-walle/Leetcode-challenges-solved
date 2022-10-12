class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colors = [-1]*n
        graph = defaultdict(set)
        for i, j in dislikes:
            graph[i-1].add(j-1)
            graph[j-1].add(i-1)
        
        possible = True
        for i in range(n):
            if not possible:
                break
            if colors[i] != -1:
                continue
            queue = deque([i])
            colors[i] = 0
            while queue and possible:
                for _ in range(len(queue)):
                    if not possible:
                        break
                    current = queue.popleft()
                    color = colors[current]
                    for neigh in graph[current]:
                        if colors[neigh] == -1:
                            colors[neigh] = 1-color
                            queue.append(neigh)
                        elif colors[neigh] == color:
                            possible = False
                            break
                            
        return possible
            
        