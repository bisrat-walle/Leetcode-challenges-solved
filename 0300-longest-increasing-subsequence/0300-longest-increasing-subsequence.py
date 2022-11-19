class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        arr = [nums[0]]
        for i in range(1, n):
            if nums[i] > arr[-1]:
                arr.append(nums[i])
            else:
                left = 0
                right = len(arr)-1
                while left < right:
                    mid = (left+right)//2
                    if arr[mid] >= nums[i]:
                        right = mid
                    else:
                        left = mid+1
                arr[left] = nums[i]
            # print(arr)
        return len(arr)