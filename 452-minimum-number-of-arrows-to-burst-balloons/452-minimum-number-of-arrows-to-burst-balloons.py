class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda k:k[1])
        an = 0
        arrow = 0
        for [start, end] in points:
            if an == 0 or start > arrow:
                an += 1
                arrow = end
        return an