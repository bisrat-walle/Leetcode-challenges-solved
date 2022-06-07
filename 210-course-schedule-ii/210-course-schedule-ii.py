from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0 for i in range(numCourses)]
        outgoing = defaultdict(set)
        
        for course, pre in prerequisites:
            outgoing[pre].add(course)
            inDegree[course] += 1
        
        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        an = []
        while queue:
            course = queue.popleft()
            for neigh in outgoing[course]:
                inDegree[neigh] -= 1
                if inDegree[neigh] == 0:
                    queue.append(neigh)
            an.append(course)
        
        return an if len(an) == numCourses else []
            
        
        