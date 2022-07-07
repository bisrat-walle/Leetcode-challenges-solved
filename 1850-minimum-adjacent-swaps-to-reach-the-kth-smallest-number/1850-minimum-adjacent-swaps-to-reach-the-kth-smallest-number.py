from collections import defaultdict

class Solution:
    def nextPermutation(self, num: List[int]) -> List[int]:
        nums = num
        
        def reverse(index):
            left, right = index, len(nums)-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        index = len(nums) - 2
        while index > -1 and not nums[index+1] > nums[index]:
            index -= 1
        
        if index != -1:
            index2 = len(nums) - 1
            while nums[index2] <= nums[index]:
                index2 -= 1
            nums[index2], nums[index] = nums[index], nums[index2]
        
        reverse(index+1)
        return nums
    
    
    def getMinSwaps(self, num: str, k: int) -> int:
        k_th = list(num)
        for _ in range(k):
            k_th = self.nextPermutation(k_th)
        
        indexes = defaultdict(list)
        for index, value in enumerate(num):
            indexes[value].append(index)
        
        num = list(num)
        an = 0
        
        for i in range(len(num)):
            if num[i] != k_th[i]:
                
                j=i
                while num[j]!=k_th[i]:
                    j+=1
                    
                while j>i:
                    num[j-1],num[j]=num[j],num[j-1]
                    an += 1
                    j -= 1 
        return an