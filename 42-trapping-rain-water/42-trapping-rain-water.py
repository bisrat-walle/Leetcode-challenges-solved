class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return 0

        an = 0
        n = len(height)
        i, j = 0, n-1
        level = 0
        
         
        while i < j:
            if height[i] <= height[j]:
                level = max(level, height[i])
                an += level - height[i]
                i += 1
                
                continue
            level = max(level, height[j])
            an += level - height[j]
            j -= 1
        return an