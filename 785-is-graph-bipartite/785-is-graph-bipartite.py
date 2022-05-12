class UnionFind:
    def __init__(self, n):
        self.representative = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find(self, i):
        r = self.representative[i]
        if r == i:
            return r
        self.representative[i] = self.find(r)
        return self.representative[i]
    
    def make_set(self, key):
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
            self.rank[f1] += self.rank[f2]
            return
        if r1 > r2:
            self.representative[f2] = f1
            self.rank[f1] += self.rank[f2]
        else:
            self.representative[f1] = f2
            self.rank[f2] += self.rank[f1]
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        union_find = UnionFind(len(graph))
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                mainR, subp = union_find.find(i), union_find.find(graph[i][j])
                if mainR == subp: 
                    return False
                union_find.union(graph[i][0], graph[i][j])
        
        return True