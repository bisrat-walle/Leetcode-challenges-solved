class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        mapping = defaultdict(int)
        for i, j in matches:
            if i not in mapping:
                mapping[i] = 0
            mapping[j] += 1
        
        ans = [[],[]]
        for key in mapping:
            if mapping[key] == 0:
                ans[0].append(key)
            if mapping[key] == 1:
                ans[1].append(key)
        
        ans[0].sort()
        ans[1].sort()
        
        return ans