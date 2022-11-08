class Solution:
    def makeGood(self, s: str) -> str:
        arr = []
        for ch in s:
            if not arr or (arr[-1].islower() and arr[-1].upper() != ch) or \
               (arr[-1].isupper() and arr[-1].lower() != ch):
                arr.append(ch)
            else:
                arr.pop()
        
        return "".join(arr)