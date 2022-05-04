class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 0
        while right < len(chars):
            chars[left] = chars[right]
            count = 1
            
            while right + 1 < len(chars) and chars[right] == chars[right + 1]:
                count += 1
                right += 1
            
            if count > 1:
                for c in str(count):
                    left += 1
                    chars[left] = c
                    
            left += 1
            right += 1
            
        return left