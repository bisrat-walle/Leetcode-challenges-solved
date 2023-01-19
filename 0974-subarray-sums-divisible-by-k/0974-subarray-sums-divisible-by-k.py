class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int, {0: 1})
        runningSum = 0
        ans = 0
        for num in nums:
            runningSum += num
            rem = runningSum%k
            ans += counter[rem]
            counter[rem] += 1
                
        return ans