class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        an = set()
        cache = {}
        def dp(cmb=(), sm=0):
            if (cmb, sm) in cache:
                return
            if sm == target:
                an.add(cmb)
            if sm > target:
                return
            cmb_temp = list(sorted(cmb))
            for num in candidates:
                temp = cmb_temp + [num]
                temp.sort()
                temp = tuple(temp)
                temp_sm = sm + num
                dp(temp, temp_sm)
            cache[(cmb, sm)] = True
        dp()
        
        return list(map(list, an))