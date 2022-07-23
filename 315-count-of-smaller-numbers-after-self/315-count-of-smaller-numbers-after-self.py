class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        ans = []
        
        for num in nums:
            left, right = 0, len(arr) - 1
            while left < right:
                mid = (left+right)//2
                if arr[mid] < num:
                    left = mid+ 1
                else:
                    right = mid
            
            
            ans.append(right)
            del arr[right]               
            
        return ans  