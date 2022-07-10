class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        even_an = 0
        odd_an = 0
        prev = nums[0]
        for index in range(1, len(nums), 2):
            if prev >= nums[index]:
                odd_an += prev-nums[index]+1
            if index != len(nums)-1:
                prev = nums[index+1]
                if prev >= nums[index]:
                    odd_an += prev-nums[index]+1
                    prev = nums[index]-1
        
        prev = None
        for index in range(0, len(nums), 2):
            if prev and prev >= nums[index]:
                even_an += prev-nums[index]+1
            if index != len(nums) - 1:
                prev = nums[index+1]
                # print(prev, nums[index+1])
                if prev >= nums[index]:
                    even_an += prev-nums[index]+1
                    prev = nums[index]-1
        # print(even_an, odd_an)
        return min(even_an, odd_an)
        
        