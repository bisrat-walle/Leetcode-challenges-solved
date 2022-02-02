class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        cm = [0]*n
        cm[0] = nums[0]
        for i in range(1, n):
            cm[i] = cm[i-1]+nums[i]
            
        print(cm)
        
        if cm[-1] - cm[0] == 0:
            return 0
        
        an = None
        
        for i in range(1, n-1):
            if cm[i-1] == cm[n-1]-cm[i]:
                an = i
                break
        if an == None:
            if cm[-2] == 0:
                return n-1
            return -1
        return an
        