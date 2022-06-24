class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heapq._heapify_max(target)
        s = sum(target)
        while target[0] != 1:
            sub = s - target[0]
            if sub == 0: 
                return False
            n = max((target[0] - 1) // sub, 1)
            s -= n * sub
            target0 = target[0] - n * sub
            if target0 < 1: 
                return False
            heapq._heapreplace_max(target, target0)

        return True