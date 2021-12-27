class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = None
        n = len(heights)
        i = 0
        while i < n:
            if stack == [] or heights[i]>=heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                if stack:
                    area = heights[top] * (i-stack[-1]-1)
                else:
                    area = heights[top] * i
                if max_area:
                    max_area = max_area if max_area > area else area
                else:
                    max_area = area
        while stack:
            top = stack.pop()
            if stack:
                area = heights[top] * (i-stack[-1]-1)
            else:
                area = heights[top] * i
            if max_area:
                max_area = max_area if max_area > area else area
            else:
                max_area = area
        return max_area