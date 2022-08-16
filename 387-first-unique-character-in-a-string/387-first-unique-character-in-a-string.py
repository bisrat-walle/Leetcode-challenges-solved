class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(list(s))
        for index in range(len(s)):
            if counter[s[index]] == 1:
                return index
        return -1
            