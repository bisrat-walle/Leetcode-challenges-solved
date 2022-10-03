class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        @lru_cache(None)
        def dfs(arr=tuple(nums), cur=()):
            ans.append(cur)
            for index in range(len(arr)):
                num = arr[index]
                new_cur = tuple(sorted(cur+(num,)))
                dfs(arr[:index]+arr[index+1:], new_cur)
        dfs()
        return ans
            