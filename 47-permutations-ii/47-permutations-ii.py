class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        an = set()
        @lru_cache(None)
        def dfs(arr=(), prev=()):
            all_none = True
            for i in range(len(arr)):
                temp_value = arr[i]
                if temp_value != None:
                    all_none = False
                    temp_arr = arr[:i]+(None,)+arr[i+1:]
                    # print(temp_arr, "***")
                    temp_prev = prev + (temp_value,)
                    dfs(temp_arr, temp_prev)
            if all_none:
                # print("Appended", prev)
                an.add(prev)
        
        dfs(tuple(nums))
        return list(map(list, an))
            