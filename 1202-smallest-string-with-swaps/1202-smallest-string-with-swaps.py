from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = defaultdict(set)
        for i, j in pairs:
            graph[i].add(j)
            graph[j].add(i)
        
        visited = set()
        def dfs(i, group):
            for neigh in graph[i]:
                if neigh not in visited:
                    visited.add(neigh)
                    group.add(neigh)
                    dfs(neigh, group)
            return group
        
        mapping = {}
        for index in range(len(s)):
            if index not in visited:
                visited.add(index)
                group = dfs(index, {index})
                # print(group)
                sorted_indexes = sorted(group, key=lambda k:s[k])
                indexes = sorted(group)
                for i, j in enumerate(indexes):
                    mapping[j] = sorted_indexes[i]
        ans = []
        for index in range(len(s)):
            if index in mapping:
                ans.append(s[mapping[index]])
            else:
                ans.append(s[index])
        return "".join(ans)