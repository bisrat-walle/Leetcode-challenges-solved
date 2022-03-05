from heapq import *

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n-1 == 0:
            return 0
        visited = {(0, 0)}
        minheap = [[grid[0][0], 0, 0]]
        direction_array = [(1,0),(0,1),(-1,0),(0,-1)]   
        is_valid = lambda index: 0 <= index < n
        
        while minheap:
            height, r, c = heappop(minheap)
            
            if r == n-1 and c == n-1:
                return height
            for x, y in direction_array:
                next_r, next_c = r+x, c+y
                if is_valid(next_r) and is_valid(next_c) and \
                        (next_r, next_c) not in visited:
                    visited.add((next_r, next_c))
                    heappush(minheap, [ max(height, grid[next_r][next_c]), next_r, next_c])
                    
                    
    