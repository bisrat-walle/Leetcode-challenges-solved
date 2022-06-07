class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(set)
        for i in range(n):
            if i != headID:
                graph[manager[i]].add((i, informTime[manager[i]]))
        
        queue = deque([(headID, 0)])
        visited = set([headID])
        an = 0
        while queue:
            for _ in range(len(queue)):
                current, res = queue.popleft()
                an = max(res, an)
                for neigh, inf_time in graph[current]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append((neigh, res+inf_time))
        return an