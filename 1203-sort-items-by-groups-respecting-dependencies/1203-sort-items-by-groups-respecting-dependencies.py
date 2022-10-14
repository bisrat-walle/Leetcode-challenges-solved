class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for index in range(n):
            if group[index] == -1:
                group[index] = m
                m += 1
        # print("Gr", group)
        visited = set()
        outgoing1 = defaultdict(set)
        inDegree1 = [0]*m
        outgoing2 = defaultdict(set)
        inDegree2 = [0]*n
        
        for i, j in enumerate(beforeItems):
            for k in j:
                if group[i] == group[k]:
                    outgoing2[k].add(i)
                    inDegree2[i] += 1
                else:
                    key = (group[k], group[i])
                    if key not in visited:
                        visited.add(key)
                        outgoing1[group[k]].add(group[i])
                        inDegree1[group[i]] += 1
        sorted_groups = []
        queue = deque()
        for i in range(m):
            if inDegree1[i] == 0:
                queue.append(i)
        # print(inDegree1)
        # print(inDegree2)
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                sorted_groups.append(current)
                for neigh in outgoing1[current]:
                    inDegree1[neigh] -= 1
                    if inDegree1[neigh] == 0:
                        queue.append(neigh)
        
        if len(sorted_groups) != m:
            return []
        
        
        graph = defaultdict(set)
        for i, j in enumerate(group):
            graph[j].add(i)
        # print(sorted_groups)
        # print(graph)  
        
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
            if len(members) != len(temp):
                # print(members, temp, i, "Ok")
                return []
            ans.extend(temp)
        
        return ans