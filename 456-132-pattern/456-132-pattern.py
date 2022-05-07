class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        monotonic_stack = []
        min_so_far = nums[0]
        for i in nums[1:]:
            while monotonic_stack and monotonic_stack[-1][0] <= i:
                monotonic_stack.pop()
            # print(monotonic_stack)
            if monotonic_stack and monotonic_stack[-1][1] < i:
                return True
            monotonic_stack.append((i,  min_so_far))
            min_so_far = min(min_so_far, i)
        return False
    
