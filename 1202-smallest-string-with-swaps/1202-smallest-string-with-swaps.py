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
        # Compression
        for i in self.representative.keys():
            self.find(i)
            
        for i in self.representative.values():
            dic[i] = {i}
        
        for i in self.representative.keys():
            rep = self.find(i)
            dic[rep].add(i)
        return dic

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        union_find = UnionFind()
        for i, j in pairs:
            union_find.make_set(i)
            union_find.make_set(j)
            union_find.union(i, j)
        
        d =  union_find.toDict()
        mapping = {}
        for group in d.values():
            sorted_group = sorted(group, key=lambda k:s[k])
            indexes = sorted(group)
            for i, index in enumerate(indexes):
                mapping[index] = sorted_group[i]
        ans = ""
        for index in range(len(s)):
            if index in mapping:
                ans += s[mapping[index]]
            else:
                ans += s[index]
        return ans