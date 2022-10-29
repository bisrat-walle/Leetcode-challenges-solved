class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for st in strs:
            key = "".join(sorted(st))
            group[key].append(st)
        
        return group.values()