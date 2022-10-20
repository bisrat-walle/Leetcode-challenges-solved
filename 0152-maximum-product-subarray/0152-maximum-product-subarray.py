class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = max_prod = 1
        ans = max(nums)
        for num in nums:
            temp = min_prod
            min_prod = min(min_prod*num, max_prod*num, num)
            max_prod = max(temp*num, max_prod*num, num)
            ans = max(ans, max_prod)
            # print(ans, num, min_prod, max_prod, "Hfdls")
        return ans
                