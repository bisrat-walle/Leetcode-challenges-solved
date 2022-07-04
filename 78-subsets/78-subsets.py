class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        an = set()
        cache = set()
        def dfs(remaining=tuple(nums), prev=()):
            if (remaining, prev) in cache:
                return
            an.add(prev)
            for i in range(len(remaining)):
                new_remaining = remaining[:i]+remaining[i+1:]
                new_remaining = tuple(sorted(new_remaining))
                new_prev = tuple(sorted(prev+(remaining[i],)))
                dfs(new_remaining, new_prev)
            cache.add((remaining, prev))
        dfs()
        return list(map(list, an))
                
            
            