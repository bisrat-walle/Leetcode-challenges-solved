class Solution:
    def maxEnvelopes(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda k: (k[0], -k[1]))
        # print(nums)
        n = len(nums)
        ans = 1
        arr = [nums[0][1]]
        for i in range(1, n):
            w, h = nums[i]
            index = bisect_left(arr, h)
            if index == len(arr):
                arr.append(h)
            else:
                arr[index] = h
                
        return len(arr)