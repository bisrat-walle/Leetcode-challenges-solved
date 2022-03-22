class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurences = {}
        for i in range(len(s)):
            last_occurences[s[i]] = i
        length = 0
        end = 0
        an = []
        for i in range(len(s)):
            length += 1
            end = max(last_occurences[s[i]], end)
            if end == i:
                an.append(length)
                length = 0
        return an
            
                