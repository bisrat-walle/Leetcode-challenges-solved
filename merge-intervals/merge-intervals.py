class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        an = [intervals[0]]
        for i in range(1, len(intervals)):
            x, y = intervals[i]
            if an[-1][1] < x:
                an.append([x, y])
            elif an[-1][1] < y:
                an[-1][1] = y
        return an