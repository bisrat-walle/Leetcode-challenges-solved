class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def solve(index):
            if index >= len(questions):
                return 0
            score1 = solve(index+questions[index][1]+1) + questions[index][0]
            score2 = solve(index+1)
            return max(score1, score2)
        return solve(0)