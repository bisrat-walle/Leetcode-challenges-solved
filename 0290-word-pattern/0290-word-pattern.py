class Solution:
    def wordPattern(self, s: str, pattern: str) -> bool: # Paramters swapped
        forward_mapping = {}
        backward_mapping = {}
        words = pattern.split()
        if len(words) != len(s):
            return False
        index = 0
        for word in words:
            if s[index] in forward_mapping and forward_mapping[s[index]] != word:
                return False
            if word in backward_mapping and backward_mapping[word] != s[index]:
                return False
            
            forward_mapping[s[index]] = word
            backward_mapping[word] = s[index]
            index += 1
        
        return True