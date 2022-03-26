class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 1 if nums[1] == nums[0] else 0
        
        di_even = {}
        di_odd = {}
        
        i = 0
        while i < len(nums):
            if nums[i] in di_even.keys():
                di_even[nums[i]] += 1
            else:
                di_even[nums[i]] = 1
            i += 2
        
        i = 1
        while i < len(nums):
            if nums[i] in di_odd.keys():
                di_odd[nums[i]] += 1
            else:
                di_odd[nums[i]] = 1
            i += 2
        
        # print(di_even, di_odd)
         
        max_even_freqs = list(sorted(di_even.items(), key=lambda k:k[1], reverse = True))
        max_odd_freqs = list(sorted(di_odd.items(), key=lambda k:k[1], reverse = True))
        half = len(nums)//2
        
        # print(max_even_freqs, max_odd_freqs)
        
        
        if max_even_freqs[0][0] != max_odd_freqs[0][0]:
            max_even_freq = max_even_freqs[0][1]
            max_odd_freq = max_odd_freqs[0][1]
        elif len(max_even_freqs) == len(max_odd_freqs) == 1:
            return half
        else:
            if len(max_even_freqs) == 1:
                max_even_freq = max_even_freqs[0][1]
                max_odd_freq = max_odd_freqs[1][1]
            elif len(max_odd_freqs) == 1:
                max_even_freq = max_even_freqs[1][1]
                max_odd_freq = max_odd_freqs[0][1]
            else:
                if max_even_freqs[0][1] + max_odd_freqs[1][1] > \
                        max_even_freqs[1][1] + max_odd_freqs[0][1]:
                    max_even_freq = max_even_freqs[0][1]
                    max_odd_freq = max_odd_freqs[1][1]
                else:
                    max_even_freq = max_even_freqs[1][1]
                    max_odd_freq = max_odd_freqs[0][1]
        
        if len(nums) % 2 != 0:
            return 2*half + 1 - max_even_freq - max_odd_freq
        return 2*half  - max_even_freq - max_odd_freq