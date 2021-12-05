class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        res = 0
     
        for i in range(len(nums)):
            if nums[i] == 0:
                pos = neg = 0
     
            elif nums[i] > 0:
                pos += 1
                if neg != 0:
                    neg += 1
                res = res if res > pos else pos
            else:
                pos, neg = neg, pos
                neg += 1
     
                if pos != 0:
                    pos += 1
                res = res if res > pos else pos
                 
        return res
        