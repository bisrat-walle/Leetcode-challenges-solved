class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        max_freq = max(Counter(nums).values())
        left = 0
        counter = defaultdict(int)
        n = len(nums)
        ans = n
        for right in range(n):
            counter[nums[right]] += 1
            while nums[left] != nums[right] and counter[nums[right]] >= max_freq:
                counter[nums[left]] -= 1
                left += 1
            # print(left, right)
            if counter[nums[right]] == max_freq:
                # print(left, right, "sat")
                ans = min(ans, right-left+1)
        
        return ans