from collections import Counter, defaultdict

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        freqCnts = Counter(nums).values()
        counter = defaultdict(int, Counter(freqCnts))
        
        quantity.sort(reverse=True) # sort in descending order to reduce search space fast
        
        def rec(index):
            if index >= len(quantity):
                return True
            for key in list(counter.keys()):
                if counter[key] > 0 and key >= quantity[index]:
                    counter[key] -= 1
                    counter[key-quantity[index]] += 1
                    if rec(index+1):
                        return True
                    # if not successful backtrack
                    counter[key] += 1
                    counter[key-quantity[index]] -= 1
            return False
        
        return rec(0)
    