class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        uniques = 0
        left = 0
        n = len(nums)
        counter = defaultdict(int)
        subarray_cnt = [1 for i in range(n)]
        ans = 0
        for right in range(n):
            counter[nums[right]] += 1
            if counter[nums[right]] == 1:
                uniques += 1
                
            while uniques > k:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    uniques -= 1
                left += 1
            
            while uniques == k and counter[nums[left]] > 1:
                counter[nums[left]] -= 1
                subarray_cnt[left+1] += subarray_cnt[left]
                left += 1
            
            if uniques == k:
                ans += subarray_cnt[left]
        
        return ans
                
                
            