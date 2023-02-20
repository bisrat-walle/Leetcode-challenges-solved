class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def stretchyWord(s: str, word: str) -> bool:
            i, j, m, n = 0, 0, len(s), len(word)
            while i < m and j < n:
                if s[i] != word[j]:
                    return False
                start_i, start_j = i, j
                while i < m and s[i] == s[start_i]:
                    i += 1
                while j < n and word[j] == word[start_j]:
                    j += 1
                len_i, len_j = i - start_i, j - start_j
                if len_i < len_j or (len_i < 3 and len_i != len_j):
                    return False
            return i == m and j == n
        
        count = 0
        for word in words:
            if len(word) > len(s):
                continue
            if stretchyWord(s, word):
                count += 1
        return count
    
    