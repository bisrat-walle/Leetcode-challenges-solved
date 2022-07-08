class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) >= len(haystack):
            return 0 if needle == haystack else -1
        index = 0
        for index in range(len(haystack)):
            current = index
            index2 = 0
            is_substring = True
            while index2 < len(needle) and current < len(haystack):
                if needle[index2] != haystack[current]:
                    is_substring = False
                    break
                index2 += 1
                current += 1
                
            if is_substring and index2 == len(needle):
                return index
            index += 1
            
        return -1