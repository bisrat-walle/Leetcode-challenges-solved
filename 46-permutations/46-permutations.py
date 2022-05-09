class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        an = []
        def dfs(temp=[], current=nums):
            if not current:
                an.append(temp)
            for i in range(len(current)):
                dfs(temp+[current[i]], current[:i]+current[i+1:])
        dfs()
        return an