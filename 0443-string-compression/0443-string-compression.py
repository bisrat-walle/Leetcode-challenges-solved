class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        current_index = 0
        index = 0
        while index < n:
            right = index
            while right < n and chars[right] == chars[index]:
                right += 1
            chars[current_index] = chars[index]
            current_index += 1
            ln = str(right-index)
            if ln != "1":
                for i in ln:
                    # print(current_index)
                    chars[current_index] = i
                    current_index += 1
            # print(chars[index], index, right)
            index = right
        
        return current_index