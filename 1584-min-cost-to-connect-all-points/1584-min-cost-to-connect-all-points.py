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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        points = [tuple(i) for i in points]
        
        def manhattan(firstpoint, secondpoint):
            return abs(firstpoint[0]-secondpoint[0]) + abs(firstpoint[1]-secondpoint[1])
        
        n = len(points)
        possible_connections = []
        for i in range(n):
            for j in range(i+1, n):
                first_point = points[i]
                second_point = points[j]
                weight = manhattan(first_point, second_point)
                possible_connections.append((weight, first_point, second_point))
        possible_connections.sort()
        union_find = UnionFind()
        an = 0
        
        for i in points:
            union_find.make_set(i)
        
        for wieght, first, second in possible_connections:
            
            if union_find.find(first) != union_find.find(second):
                union_find.union(first, second)
                an += wieght
        
        return an
                
                
                
                
                
        