class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        @lru_cache(None)
        def rec(index, prev=None, cur=None):
            if index >= n:
                return 0
            ans = rec(index+1, prev, cur)
            if cur == None:
                if prev == None:
                    ans = max(ans, 1+rec(index+1, nums[index], cur))
                elif prev != nums[index]:
                    ans = max(ans, 1+rec(index+1, nums[index], nums[index]-prev > 0))
            else:
                if cur and prev > nums[index]:
                    ans = max(ans, 1+rec(index+1, nums[index], False))
                elif (not cur) and prev < nums[index]:
                    ans = max(ans, 1+rec(index+1, nums[index], True))
            return ans
        
        return rec(0)