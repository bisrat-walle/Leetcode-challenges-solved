class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k or len(cardPoints) == 1:
            return sum(cardPoints)
        
        max_sum = sum(cardPoints[:k])
        current_sum = max_sum
        # print(cardPoints[:k])
        current_index = len(cardPoints) - 1
        for i in reversed(range(k)):
            current_sum = current_sum - cardPoints[i] + cardPoints[current_index]
            max_sum = max(max_sum, current_sum)
            # print("new_sum", new_sum, "max sum", max_sum, "added", cardPoints[current_index])
            current_index -= 1
        
        return max_sum
        