class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        m = len(min(strs, key=len))
        prefix = strs[0]
        for i in range(m):    
            for myStr in strs:
                if myStr[i] != prefix[i]:
                    return prefix[:i]
        return prefix[:m]