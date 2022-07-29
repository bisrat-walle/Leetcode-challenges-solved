from collections import Counter

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            mapping = {}
            valid = True
            for index in range(len(word)):
                if word[index] in mapping:
                    if mapping[word[index]] != pattern[index]:
                        valid = False
                        break
                elif pattern[index] in mapping.values():
                    for key in mapping:
                        if mapping[key] == pattern[index]:
                            break
                            
                    if key != word[index]:
                        valid = False
                        break
                else:
                    mapping[word[index]] = pattern[index]
            # print(mapping)
            if valid: ans.append(word)
        
        return ans