class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        self.an=0
        visited=set()

        def helper(i,cur):
            if i in visited: 
                self.an=max(self.an,cur)
                return
            visited.add(i)
            helper(nums[i],cur+1)
        
        for i in range(len(nums)):
            helper(i,0)
        return self.an
                