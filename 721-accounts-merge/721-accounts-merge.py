class UnionFind:
    def __init__(self, n):
        self.representative = [i for i in range(n)]
        self.n = n
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
        
    def toDict(self):
        dic = {}
        for i in range(self.n):
            f = self.find(i)
            if f not in dic.keys():
                dic[f] = set()
            if f != i:
                dic[f].add(i)
        return dic

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        union_find = UnionFind(n)
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    temp = set(accounts[i][1:])
                    for k in accounts[j][1:]:
                        if k in temp:
                            union_find.union(i, j)
        
        
        di = union_find.toDict()
        for i, j in di.items():
            temp1 = set(accounts[i][1:])
            temp2 = set()
            for m in j:
                temp2 = temp2.union(set(accounts[m][1:]))
            for k in temp2:
                if k not in temp1:
                    accounts[i].append(k)
        
        # print(accounts)
        
        an = []
        for i in range(n):
            if i not in di.keys():
                continue
            
            an.append([accounts[i][0]])
            
            an[-1].extend(list(sorted(set(accounts[i][1:]))))
        
        return an
         