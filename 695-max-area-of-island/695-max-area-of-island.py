class UnionFind:
    def __init__(self):
        self.representative = {}
        self.rank = {}
    
    def find(self, i):
        r = self.representative[i]
        if r == i:
            return r
        self.representative[i] = self.find(r)
        return self.representative[i]
    
    def make_set(self, key):
        if key not in self.representative.keys():
            self.representative[key] = key
            self.rank[key] = 1
    
    def union(self, i, j):
        f1 = self.find(i)
        f2 = self.find(j)
        if f1 == f2:
            return
        
        r1 = self.rank[f1]
        r2 = self.rank[f2]
        if r1 == r2:
            self.representative[f2]= f1
            self.rank[f1] += 1
            return
        if r1 > r2:
            self.representative[f2] = f1
        else:
            self.representative[f1] = f2
        
    def toDict(self):
        dic = {}
        for i in self.representative.values():
            dic[i] = set((i,))
        for i in self.representative.keys():
            dic[self.find(i)].add(i)
        return dic


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0]) 
        union_find = UnionFind()
        direction_array = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        is_valid = lambda x, y: (0 <= x < row) and (0 <= y < column)
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    
                    union_find.make_set((i, j))
                    for x, y in direction_array:
                        i_neigh, j_neigh = i+x, j+y
                        if is_valid(i_neigh, j_neigh) and grid[i_neigh][j_neigh] == 1:
                            union_find.make_set((i_neigh, j_neigh))
                            union_find.union((i, j), (i_neigh, j_neigh))
                        
        max_area = 0
        di = union_find.toDict()
        
        for i in di.keys():
            max_area = max(max_area, len(di[i]))
        return max_area
        