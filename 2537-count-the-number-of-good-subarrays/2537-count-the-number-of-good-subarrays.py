class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        n = len(nums)
        counter = defaultdict(int)
        pairs = 0
        ans = 0
        for right in range(n):
            pairs += counter[nums[right]]
            counter[nums[right]] += 1
            while pairs >= k:
                counter[nums[left]] -= 1
                pairs -= counter[nums[left]]
                ans += n-right
                left += 1
        
        return ans