class Solution:
    def PredictTheWinner(self, nums: List[int], player1 = 0, player2 = 0, current = 0) -> bool:
        memo = {}
        def dp(start, end, turn):
            if start > end:
                return 0
            if (start+1, end) not in memo:
                memo[(start+1,end)] = dp(start+1, end, not turn)
            if (start, end-1) not in memo:
                memo[(start,end-1)] = dp(start, end-1, not turn)
            option1 = nums[start] + memo[(start+1,end)]
            option2 = nums[end] + memo[(start,end-1)]
            if turn:
                memo[(start, end)] = max(option1, option2)
            else:
                memo[(start, end)] = min(memo[(start+1,end)], memo[(start,end-1)])
            return memo[(start, end)]
        
        p1_score = dp(0, len(nums)-1, True)
        p2_score = sum(nums)-p1_score
        return p1_score >= p2_score
            
            
        
                
            
            