class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        comb = list(zip(ages, scores, range(n)))
        comb.sort()
        dp = [scores[comb[i][2]] for i in range(n)]
        for i in range(n):
            for j in range(i):
                if comb[i][1] >= comb[j][1]:
                    dp[i] = max(dp[i], dp[j] + scores[comb[i][2]])
        
        return max(dp)
        
        