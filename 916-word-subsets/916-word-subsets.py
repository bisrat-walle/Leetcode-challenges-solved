from collections import defaultdict

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        universal = []
        counter = defaultdict(int)
        for word in words2:
            temp_counter = defaultdict(int)
            for ch in word:
                temp_counter[ch] += 1
            for key, value in temp_counter.items():
                counter[key] = max(counter[key], value)
                
        for word in words1:
            is_universal = True
            temp_counter = defaultdict(int)
            for ch in word:
                temp_counter[ch] += 1
            for key, value in counter.items():
                if value > temp_counter[key]:
                    is_universal = False
                    break
            if is_universal:
                universal.append(word)
        
        return universal