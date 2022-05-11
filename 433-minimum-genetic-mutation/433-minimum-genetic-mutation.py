class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        options = ['A', 'T', 'C', 'G']
        bank = set(bank)
        if end not in bank:
            return -1
        queue = deque([(start, 0)])
        visited = set(start)
        while queue:
            current, step = queue.popleft()
            if current == end:
                return step
            for i in range(8):
                for j in options:
                    temp = current[:i]+j+current[i+1:]
                    if temp not in visited and temp in bank:
                        visited.add(temp)
                        queue.append((temp, step+1))
        return -1