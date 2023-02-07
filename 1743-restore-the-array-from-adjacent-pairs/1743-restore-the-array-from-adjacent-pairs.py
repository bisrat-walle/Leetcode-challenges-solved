class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        counter = defaultdict(int)
        graph = defaultdict(set)
        
        for i, j in adjacentPairs:
            graph[i].add(j)
            graph[j].add(i)
            counter[i] += 1
            counter[j] += 1
        
        for key in counter:
            if counter[key] == 1:
                first = key
        visited = {first}
        arr = [first]
        
        def dfs(current):
            nonlocal arr
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    arr.append(neighbor)
                    dfs(neighbor)
        
        dfs(first)
        
        
        
        return arr