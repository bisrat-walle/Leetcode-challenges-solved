from itertools import accumulate

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix_sum = list(accumulate(nums))
        min_diff = float('inf')
        an = 0
        for i in range(len(nums)):
            
            curr_diff = abs(prefix_sum[i]//(i+1)-((prefix_sum[-1]-prefix_sum[i])//\
                            (len(nums)-i-1) if i!=len(nums)-1 else 0))
            if min_diff > curr_diff:
                # '>' not '>=' because I wanna keep minimum index BW
                min_diff = curr_diff
                an = i
        return an