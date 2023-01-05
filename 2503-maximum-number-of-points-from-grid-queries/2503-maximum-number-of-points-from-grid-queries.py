class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        n, k = len(grid), len(grid[0])
        is_valid = lambda i, j: 0 <= i < n and 0 <= j < k
        m = len(queries)
        sorted_order = []
        heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while heap:
            val, i, j = heappop(heap)
            sorted_order.append(val)
            for i_drn, j_drn in directions:
                new_i, new_j = i + i_drn, j + j_drn
                if is_valid(new_i, new_j) and (new_i, new_j) not in visited:
                    visited.add((new_i, new_j))
                    heappush(heap, (grid[new_i][new_j], new_i, new_j))
        
        
        for i in range(1, len(sorted_order)):
            sorted_order[i] = max(sorted_order[i], sorted_order[i-1])

        # print(sorted_order)

        ans = []

        for query in queries:
            left, right = 0, len(sorted_order) - 1
            while left < right:
                mid = (left+right+1)//2
                if sorted_order[mid] >= query:
                    right = mid-1
                else:
                    left = mid
            if sorted_order[left] < query:
                ans.append(left+1)
            else:
                ans.append(0)
        
        return ans

