class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)
        prev = 0
        l1, h1 = float("-inf"), float("-inf")
        for index in range(len(horizontalCuts)):
            l1 = max(l1, horizontalCuts[index]-prev)
            prev = horizontalCuts[index]
        
        prev = 0
        for index in range(len(verticalCuts)):
            h1 = max(h1, verticalCuts[index]-prev)
            prev = verticalCuts[index]
        
        return (h1 * l1) % (10**9 + 7)
        