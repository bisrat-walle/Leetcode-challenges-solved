class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = defaultdict(list)
        for i in strs:
            key = tuple(sorted(list(i)))
            di[key].append(i)
        an = []
        
        for i in di.values():
            an.append(i)
        return an