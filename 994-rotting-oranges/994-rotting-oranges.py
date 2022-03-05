class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directional_array = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        is_valid = lambda x,y : 0<=x<len(grid) and 0<=y<len(grid[0])
        rotten = []
        fresh = []
        visited = set()
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.append((i, j))
                if grid[i][j] == 2:
                    visited.add((i, j))
                    rotten.append((i, j))
        # print("fresh", fresh)
        
        if len(fresh) == 0:
            return 0
        
        queue = [i for i in rotten]
        
        time = 0
        fresh_rotten = []
        while queue:
            # print(queue)
            temp = []
            for i in queue:
                for x, y in directional_array:
                    r, c = i[0]+x, i[1]+y
                    if (r, c) not in visited:
                        if is_valid(r, c):
                            if grid[r][c] == 1:
                                temp.append((r, c))
                                grid[r][c] = 2
                                visited.add((r, c))
                                fresh_rotten.append((r, c))
            time += 1
            # print(queue, temp)
            queue = temp
        
        # print("Stat", set(fresh_rotten), fresh)
        
        if len(fresh_rotten) != len(fresh):
            return -1
        return time-1
        