class UnionFind:
    def __init__(self):
        self.representative = {}
        self.rank = {}
    
    def make_set(self, val):
        if val in self.representative:
            return
        self.representative[val] = val
        self.rank[val] = 1
    
    def find(self, val):
        self.make_set(val)
        rep = self.representative[val]
        if rep == val:
            return val
        self.representative[val] = self.find(rep)
        return self.representative[val]
    
    def union(self, val1, val2):
        self.make_set(val1)
        self.make_set(val2)
        rep1 = self.find(val1)
        rep2 = self.find(val2)
        if rep1 == rep2:
            return
        rank1 = self.rank[rep1]
        rank2 = self.rank[rep2]
        if rank1 < rank2:
            self.representative[rep1] = rep2
            self.rank[rep2] += rank1
        else:
            self.representative[rep2] = rep1
            self.rank[rep1] += rank2
        


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        union_find = UnionFind()
        for equation in equations:
            x, *op, y = list(equation)
            if op[0] == "=":
                union_find.union(x, y)
        for equation in equations:
            x, *op, y = list(equation)
            if op[0] == "!":
                if union_find.find(x) == union_find.find(y):
                    return False
        return True