class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_set = Counter(s)
        t_set = Counter(t)
        for ch in t_set:
            if ch not in s_set or t_set[ch] != s_set[ch]:
                return ch
        return "NEVER REACH HERE :) BW"