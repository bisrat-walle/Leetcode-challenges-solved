class UnionFind:
    def __init__(self, n):
        self.representative = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find(self, i):
        r = self.representative[i]
        if r == i:
            return i
        return self.find(r)
    
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

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        union_find = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union_find.union(i, j)
        reps = set()
        for i in range(n):
            reps.add(union_find.find(i))
        
        # print(union_find.representative)
        # print(reps)
        return len(reps)