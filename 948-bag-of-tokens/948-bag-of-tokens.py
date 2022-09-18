class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens)-1
        ans = current_score = 0
        while left <= right and (power >= tokens[left] or current_score):
            while left <= right and power >= tokens[left]:
                power -= tokens[left]
                left += 1
                current_score += 1
            ans = max(ans, current_score)

            if left <= right and current_score:
                power += tokens[right]
                right -= 1
                current_score -= 1

        return ans