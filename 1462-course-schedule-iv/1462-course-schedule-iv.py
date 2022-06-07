class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        def dfs(i, visited=set()):
            visited.add(i)
            for j in graph[i]:
                if j not in visited:
                    dfs(j, visited)
        
        graph = {}
        for i in range(numCourses):
            graph[i] = set()
        
        for preq, course in prerequisites:
            graph[preq].add(course)
        an = []
        for preq, course in queries:
            vis = set()
            dfs(preq, vis)
            if course in vis:
                an.append(True)
            else:
                an.append(False)
        return an
            
            
            