class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        primeter = sum(matchsticks)
        if primeter % 4 != 0:
            return False
        length = primeter // 4
        matchsticks.sort(reverse=True)
        @lru_cache(None)
        def is_possible(l1=0, l2=0, l3=0, l4=0, index=0):
            nonlocal length
            if l1 == l2 == l3 == l4 == length:
                return True
            if index > len(matchsticks) - 1:
                return False
            if l1 > length or l2 > length or l3 > length or l4 > length:
                return False
            return is_possible(l1 + matchsticks[index], l2, l3, l4, index + 1) or \
                    is_possible(l1, l2 + matchsticks[index] , l3, l4, index + 1) or \
                    is_possible(l1, l2, l3 + matchsticks[index], l4, index + 1) or \
                    is_possible(l1, l2, l3, l4 + matchsticks[index] , index + 1)
        
        return is_possible(0, 0, 0, 0, 0)