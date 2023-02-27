class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        n = 2050 - 1949
        popn = [0 for i in range(n)]
        for birth, death in logs:
            for i in range(birth, death):
                popn[i-1950] += 1
                
        for i in range(n):
            if max(popn) == popn[i]:
                return 1950 + i
            
            