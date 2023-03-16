class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        if len(cookies) == k:
            return max(cookies)
         
        self.ans = float("inf")
        visited = set()
        ass = [0] * k
        
        self.mask = 0
        
        def backtrack(index):
            if (index, self.mask) in visited:
                return
            if index >= len(cookies):
                self.ans = min(self.ans, max(ass))
                return
            
            if self.ans <= max(ass):
                return
            
            for i in range(k):
                ass[i] += cookies[index]
                self.mask |= 1 << index
                visited.add((index, self.mask))
                backtrack(index+1)
                self.mask &= ~(1 << index)
                ass[i] -= cookies[index]
        
        backtrack(0)
        
        return self.ans