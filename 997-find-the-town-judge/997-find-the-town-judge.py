class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        di1 = defaultdict(int)
        di2 = defaultdict(int)
        for i, j in trust:
            di1[i] += 1
            di2[j] += 1
            if j not in di1:
                di1[j] = 0
            if i not in di2:
                di2[i] = 0
        
        # print(di1, di2)
        for i in di1:
            if di1[i] == 0 and di2[i] == n-1:
                return i
        
        return -1