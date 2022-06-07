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
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        M = 2 * (N+1)
        tree = UnionFind(M)
        for dis in dislikes:
            tree.union(dis[0], dis[1]+N+1 )
            tree.union(dis[0]+N+1, dis[1])
        for i in range(1,N+1):
            if tree.find(i) == tree.find(i+N+1):
                return False
        return True