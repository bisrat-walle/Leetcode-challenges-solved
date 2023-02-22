class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping1 = defaultdict(lambda :"")
        mapping2 = defaultdict(lambda :"")
        n = len(s)
        for i in range(n):
            if (not mapping1[s[i]]) and (not mapping2[t[i]]):
                mapping1[s[i]] = t[i]
                mapping2[t[i]] = s[i]
            elif mapping1[s[i]] != t[i] and mapping2[t[i]] != s[i]:
                return False
        return True
            