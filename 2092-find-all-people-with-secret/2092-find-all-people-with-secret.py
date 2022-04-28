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
    def make_set(self, i):
        self.representative[i] = i
    
    def getFamily(self, i):
        rep = self.find(i)
        an = []
        for j in range(len(self.representative)):
            if self.find(j) == rep:
                an.append(j)
        return an


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        simult = {}
        for meeting1, meeting2, time in meetings:
            if time not in simult:
                simult[time] = {(meeting1, meeting2)}
            else:
                simult[time].add((meeting1, meeting2))
            
        union_find = UnionFind(n)
        union_find.union(0, firstPerson)
        sor_time = sorted(simult.keys())
        for i in sor_time:
            added = set()
            for j, k in simult[i]:
                added.add(j)
                added.add(k)
                union_find.union(j, k)
            
            for j in added:
                if union_find.find(j) != union_find.find(firstPerson):
                    union_find.make_set(j)
                
        return union_find.getFamily(firstPerson)
        