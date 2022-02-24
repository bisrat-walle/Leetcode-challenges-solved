class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self.find_duplicate(nums, min(nums), max(nums))
        
    def find_duplicate(self, arr, start, end):
        if start == end:
                return start
        mid = start + (end-start)//2
        counter = 0
        for i in arr:
            if i in range(start, mid+1):
                counter += 1
        # print(start, mid, end, counter)
        if counter > mid-start+1:
            return self.find_duplicate(arr, start, mid)
        return self.find_duplicate(arr, mid+1, end)