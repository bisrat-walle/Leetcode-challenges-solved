class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        ans = [None]*2
        for i in range(1, len(nums)+1):
            if i not in counter:
                ans[1] = i
            if counter[i] == 2:
                ans[0] = i
        return ans