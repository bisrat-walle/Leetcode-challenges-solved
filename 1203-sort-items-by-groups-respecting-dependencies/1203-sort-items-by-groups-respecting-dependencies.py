class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        # Assign group for those who don't have group to make implementation easier
        for index in range(n):
            if group[index] == -1:
                group[index] = m
                m += 1

        visited = set() # for handling multiple dependecies with two group
        
        # for group topological sort
        outgoing1 = defaultdict(set)
        inDegree1 = [0]*m
        
        # for items inside a group toploglical sort 
        outgoing2 = defaultdict(set)
        inDegree2 = [0]*n
        
        # count indegrees and build outgoing graph
        for i, j in enumerate(beforeItems):
            for k in j:
                # same group
                if group[i] == group[k]:
                    outgoing2[k].add(i)
                    inDegree2[i] += 1
                else: # across group
                    key = (group[k], group[i])
                    if key not in visited:
                        visited.add(key)
                        outgoing1[group[k]].add(group[i])
                        inDegree1[group[i]] += 1
                        
        # try sorting groups
        sorted_groups = []
        queue = deque()
        for i in range(m):
            if inDegree1[i] == 0:
                queue.append(i)
                
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                sorted_groups.append(current)
                for neigh in outgoing1[current]:
                    inDegree1[neigh] -= 1
                    if inDegree1[neigh] == 0:
                        queue.append(neigh)
        
        if len(sorted_groups) != m: # if the group has cycle
            return []
        
        # try sorting the members inside a group based on group sort
        
        graph = defaultdict(set)
        for i, j in enumerate(group):
            graph[j].add(i) 
        
        ans = []
        for i in sorted_groups:
            members = graph[i]
            queue = deque()
            temp = []
            for member in members:
                if inDegree2[member] == 0:
                    queue.append(member)
            while queue:
                for _ in range(len(queue)):
                    current = queue.popleft()
                    temp.append(current)
                    for neigh in outgoing2[current]:
                        inDegree2[neigh] -= 1
                        if inDegree2[neigh] == 0:
                            queue.append(neigh)
            if len(members) != len(temp): # if there is a cycle within a group
                return []
            ans.extend(temp) # update the answer
        
        return ans