class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [nums[0]]
        backward = [nums[-1]]
        
        for index in range(1, len(nums)):
            forward.append(forward[-1]*nums[index])
        
        for index in range(len(nums)-2, -1, -1):
            backward.append(backward[-1]*nums[index])
        
        backward.reverse()
        
        ans = [None]*len(nums)
        # print(forward)
        # print(backward)
        for index in range(len(nums)):
            if index == 0:
                ans[index] = backward[index+1]
            elif index == len(nums)-1:
                ans[index] = forward[index-1]
            else:
                ans[index] = forward[index-1]*backward[index+1]
        return ans