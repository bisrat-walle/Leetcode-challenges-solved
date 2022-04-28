class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0, 0, 0)]
        row = len(heights)
        column = len(heights[0])
        target = (row - 1, column -1)
        is_valid = lambda i, j: 0 <= i < row and 0 <= j < column
        direction_array = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        while heap:
            w, i, j = heappop(heap)
            if (i, j) in visited:
                continue
            if (i, j) == target:
                return w
            visited.add((i, j))
            for i_dir, j_dir in direction_array:
                current_i, current_j = i+i_dir, j + j_dir
                if is_valid(current_i, current_j):
                    w_ = max(w, abs(heights[current_i][current_j]-heights[i][j]))
                    heappush(heap, (w_, current_i, current_j))