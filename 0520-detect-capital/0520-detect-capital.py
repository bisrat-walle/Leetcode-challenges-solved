class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1 or word == word.upper() or word == word.lower():
            return True
        if word[0].upper() != word[0]:
            return False
        for i in range(1, len(word)):
            if word[i] != word[i].lower():
                return False
        return True