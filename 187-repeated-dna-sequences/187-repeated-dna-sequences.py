class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        candidates = []
        queue = deque(list(s[:10]))
        candidates.append(s[:10])
        for i in range(10, len(s)):
            queue.popleft()
            queue.append(s[i])
            candidates.append("".join(queue))
        ans = []
        counter = Counter(candidates)
        # print(counter)
        for key, value in counter.items():
            if len(key) == 10 and value > 1:
                ans.append(key)
        
        return ans
            
        