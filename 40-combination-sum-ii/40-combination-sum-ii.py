class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        an = set()
        cache = {}
        def dp(cmb=(), sm=0, cand=tuple(candidates)):
            if (cmb, sm) in cache:
                return
            if sm == target:
                an.add(cmb)
            if sm > target:
                return
            cmb_temp = list(sorted(cmb))
            for index in range(len(cand)):
                num = cand[index]
                temp_tuple = cand[:index] + cand[index+1:]
                temp = cmb_temp + [num]
                temp.sort()
                temp = tuple(temp)
                temp_sm = sm + num
                dp(temp, temp_sm, temp_tuple)
            cache[(cmb, sm)] = True
        dp()
        
        return list(map(list, an))