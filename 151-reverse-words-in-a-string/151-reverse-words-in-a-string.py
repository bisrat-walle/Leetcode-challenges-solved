class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(list(map(lambda a:a.strip(), s.split()))))
