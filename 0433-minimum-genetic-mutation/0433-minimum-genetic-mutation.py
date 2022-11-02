class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        genes = ["A", "T", "C", "G"]
        queue = deque([start])
        n = 8 # length of the gene string
        visited = {start}
        mutuations = 0
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == end:
                    return mutuations
                for index in range(n):
                    for index2 in range(4):
                        # print(current, index, index2)
                        if current[index] != genes[index2]:
                            new_gene = current[:index] + genes[index2] + current[index+1:]
                            if new_gene in bank and new_gene not in visited:
                                # print(new_gene)
                                visited.add(new_gene)
                                queue.append(new_gene)
            mutuations += 1
        return -1