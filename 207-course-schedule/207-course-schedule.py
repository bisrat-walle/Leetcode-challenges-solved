from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegrees = [0]*numCourses
        outgoing = defaultdict(set)
        for course, preq in prerequisites:
            outgoing[course].add(preq)
            inDegrees[preq] += 1
        
        queue = deque()
        for i in range(numCourses):
            if inDegrees[i] == 0:
                queue.append(i)
        count = 0
        while queue:
            current_course = queue.popleft()
            count += 1
            for nieghbor in outgoing[current_course]:
                inDegrees[nieghbor] -= 1
                if inDegrees[nieghbor] == 0:
                    queue.append(nieghbor)
        return count == numCourses
            
        
        