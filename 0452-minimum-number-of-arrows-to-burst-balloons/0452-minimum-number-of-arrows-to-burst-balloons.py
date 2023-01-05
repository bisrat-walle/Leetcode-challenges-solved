class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda k:k[1])
        ans = 0
        current = None

        for start, end in points:
            if current == None or start > current:
                ans += 1
                current = end
            
        
        return ans