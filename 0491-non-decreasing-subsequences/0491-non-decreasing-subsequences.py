class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = set()
        n = len(nums)
        def dfs(index):
            if len(path) > 1:
                ans.add(tuple(path))
            if index >= n:
                return
            dfs(index+1)
            if (not path) or path[-1] <= nums[index]:
                path.append(nums[index])
                dfs(index+1)
                path.pop()
        
        dfs(0)
        
        return ans